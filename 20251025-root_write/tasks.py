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

def write(c: Context, target_name: str, docker_command: str="docker"):
    c.run(f"{docker_command} run --rm -v $(pwd):/workspace -e TARGET=tmp/{target_name}.txt -w /workspace debian bash test_write.sh")

def test(c: Context, target_name: str, docker_command: str="docker", compose_command: str="docker compose"):
    c.run("sudo rm -rf tmp/*.txt", warn=True)

    local_uid, local_gid = get_local_uid_gid(c)

    write(c, target_name, docker_command=docker_command)

    stat = os.stat(f"tmp/{target_name}.txt")

    if stat.st_uid != local_uid:
        print(f"- Test1: ❌ Error UID mismatch! local_uid={local_uid} uid={stat.st_uid}")
    else:
        print(f"- Test1: ✅ used same UID: local_uid={local_uid} uid={stat.st_uid}")



    c.run(f"{docker_command} run --rm -d -p 8080:80 --name nginx-test nginx:latest")

    time.sleep(2)

    r = c.run("curl -s http://localhost:8080", warn=True)
    assert r
    if r.ok:
        print("- Test2: ✅ can access nginx by localhost:8080")
    else:
        print("- Test2: ❌ Error: cannot access nginx by localhost:8080")

    c.run(f"{docker_command} rm -f nginx-test")


    c.run(f"{compose_command} up -d")

    time.sleep(2)

    r = c.run("curl -s http://localhost:8080", warn=True)
    assert r
    if r.ok:
        print("- Test3: ✅ can access nginx by http://localhost:8080")
    else:
        print("- Test3: ❌ Error: cannot access nginx by http://localhost:8080")

    r = c.run(f"{compose_command} exec -it dev curl -s http://nginx", warn=True)
    assert r
    if r.ok:
        print("- Test4: ✅ can access nginx by http://nginx inside dev container")
    else:
        print("- Test4: ❌ Error: cannot access nginx by http://nginx inside dev container")

    c.run(f"{compose_command} down")
    c.run(f"{compose_command} rm")


@task
def run_docker_desktop(c: Context):
    c.run("docker context use desktop-linux")

    test(c, "docker-desktop")

@task
def run_podman(c: Context):
    test(c, "podman", docker_command="podman", compose_command="PODMAN_COMPOSE_PROVIDER=podman-compose podman compose")

@task
def run_rancher_desktop(c: Context):
    c.run("docker context use rancher-desktop")

    test(c, "rancher-desktop")

@task
def run_colima(c: Context):
    c.run("docker context use colima")

    test(c, "rancher-desktop")