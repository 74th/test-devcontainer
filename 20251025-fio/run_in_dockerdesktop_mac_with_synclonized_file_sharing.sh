#!/bin/bash
set -ex

docker context use desktop-linux
docker run --rm \
    -e NAME=dockerdesktop_mac_with_synclonized_file_sharing \
    --mount type=bind,source=$(pwd),target=/workspace \
    -w /workspace \
    fio-devcontainer \
    bash ./test_fio_no_direct.sh
