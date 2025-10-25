#!/bin/bash
set -ex

podman build -t fio-devcontainer .
podman run --rm \
    -e NAME=podman_mac \
    --mount type=bind,source=$(pwd),target=/workspace \
    -w /workspace \
    fio-devcontainer \
    bash ./test_fio.sh
