#!/bin/bash
set -ex

docker run --rm \
    -e NAME=dockerdesktop_mac_with_consistent \
    --mount type=bind,source=$(pwd),target=/workspace \
    -w /workspace \
    fio-devcontainer \
    bash ./test_fio.sh