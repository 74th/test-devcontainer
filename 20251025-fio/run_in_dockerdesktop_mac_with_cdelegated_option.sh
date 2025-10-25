#!/bin/bash
set -ex

docker run --rm \
    -e NAME=dockerdesktop_mac_with_delegated_option \
    --mount type=bind,source=$(pwd),target=/workspace,consistency=delegated \
    -w /workspace \
    fio-devcontainer \
    bash ./test_fio.sh