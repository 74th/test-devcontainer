#!/bin/bash
set -ex

docker run --rm \
    -e NAME=linux_host_docker \
    -e RESULTS_DIR=results_linux_host \
    --mount type=bind,source=$(pwd),target=/workspace \
    -w /workspace \
    fio-devcontainer \
    bash ./test_fio.sh
