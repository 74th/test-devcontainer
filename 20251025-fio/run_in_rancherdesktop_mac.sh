#!/bin/bash
set -ex

docker context use rancher-desktop
docker run --rm \
    -e NAME=rancher_desktop_mac \
    --mount type=bind,source=$(pwd),target=/workspace \
    -w /workspace \
    fio-devcontainer \
    bash ./test_fio.sh
