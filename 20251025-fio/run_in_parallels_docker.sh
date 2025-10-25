#!/bin/bash
set -ex

docker run --rm \
    -e NAME=parallels_docker \
    --mount type=bind,source=$(pwd),target=/workspace \
    -w /workspace \
    fio-devcontainer \
    bash ./test_fio.sh