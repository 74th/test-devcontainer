import os
import time
from invoke.context import Context
from invoke.tasks import task


def get_local_uid_gid(c: Context) -> tuple[int, int]:
    r = c.run("id -u")
    assert r
    local_uid = int(r.stdout.strip())
    r = c.run("id -g")
    assert r
    local_gid = int(r.stdout.strip())
    return local_uid, local_gid


def test(
    c: Context,
    target_name: str,
    docker_command: str = "docker",
    compose_command: str = "docker compose",
    run_only: str | None = None,
):
    _run_only = run_only if run_only is None else int(run_only)

    if _run_only is None or _run_only == 1:
        c.run("sudo rm -rf tmp/*.txt", warn=True)

        local_uid, local_gid = get_local_uid_gid(c)

        c.run(
            f"{docker_command} run --rm -v $(pwd):/workspace -e TARGET=tmp/{target_name}.txt -w /workspace debian bash test_write.sh"
        )

        stat = os.stat(f"tmp/{target_name}.txt")

        if stat.st_uid != local_uid:
            print(
                f"- Test1-1: ❌ Error UID mismatch! local_uid={local_uid} uid={stat.st_uid}"
            )
        else:
            print(
                f"- Test1-1: ✅ used same UID: local_uid={local_uid} uid={stat.st_uid}"
            )

        c.run("sudo rm -rf tmp/*.txt", warn=True)

        r = c.run(
            f"{docker_command} run --rm --user {local_uid}:{local_gid} -v $(pwd):/workspace -e TARGET=tmp/{target_name}.txt -w /workspace debian bash test_write.sh",
            warn=True,
        )
        assert r is not None

        if r.ok:
            stat = os.stat(f"tmp/{target_name}.txt")

            if stat.st_uid != local_uid:
                print(
                    f"- Test1-2: ❌ Error UID mismatch! local_uid={local_uid} uid={stat.st_uid}"
                )
            else:
                print(
                    f"- Test1-2: ✅ used same UID: local_uid={local_uid} uid={stat.st_uid}"
                )
        else:
            print("- Test1-2: ❌ cannot write using local_uid, local_gid")

    if _run_only is None or _run_only == 2:
        c.run(f"{docker_command} run -d -p 8080:80 --name nginx-test nginx:latest")

        time.sleep(2)

        r = c.run("curl -s http://localhost:8080")
        assert r
        if r.ok:
            print("- Test2: ✅ can access nginx by localhost:8080")
        else:
            print("- Test2: ❌ Error: cannot access nginx by localhost:8080")

        c.run(f"{docker_command} rm -f nginx-test")

    if _run_only is None or _run_only in (3, 4):
        c.run(f"{compose_command} up -d")

        time.sleep(2)

        if _run_only is None or _run_only == 3:
            r = c.run("curl -s http://localhost:8080")
            assert r is not None
            if r.ok:
                print("- Test3: ✅ can access nginx by http://localhost:8080")
            else:
                print("- Test3: ❌ Error: cannot access nginx by http://localhost:8080")

        if _run_only is None or _run_only == 4:
            r = c.run(f"{compose_command} exec -it dev curl -s http://nginx")
            assert r is not None
            if r.ok:
                print(
                    "- Test4: ✅ can access nginx by http://nginx inside dev container"
                )
            else:
                print(
                    "- Test4: ❌ Error: cannot access nginx by http://nginx inside dev container"
                )

        c.run(f"{compose_command} down")
        c.run(f"{compose_command} rm")

    if _run_only is None or _run_only == 5:
        r = c.run(f"{docker_command} run --rm --platform linux/amd64 debian uname -a")
        assert r is not None
        if r.ok and r.stdout.count("x86_64"):
            print("- Test5: ✅ can run amd64 container")
        else:
            print("- Test5: ❌ Error: cannot run amd64 container")


@task
def run_docker_desktop(c: Context, run_only: str | None = None):
    c.run("docker context use desktop-linux")

    test(c, "docker-desktop", run_only=run_only)


@task
def run_podman(c: Context, run_only: str | None = None):
    test(
        c,
        "podman",
        docker_command="podman",
        compose_command="podman compose",
        run_only=run_only,
    )


@task
def run_rancher_desktop(c: Context, run_only: str | None = None):
    c.run("docker context use rancher-desktop")

    test(c, "rancher-desktop", run_only=run_only)


@task
def run_colima(c: Context, run_only: str | None = None):
    c.run("docker context use colima")

    test(c, "collima", run_only=run_only)


@task
def run_finch(c: Context, run_only: str | None = None):
    print(f"runonly: {run_only}")
    test(
        c,
        "finch",
        docker_command="finch",
        compose_command="finch compose",
        run_only=run_only,
    )
