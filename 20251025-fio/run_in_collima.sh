#!/bin/bash
set -ex

docker context use colima
docker run --rm \
    -e NAME=colima \
    --mount type=bind,source=$(pwd),target=/workspace \
    -w /workspace \
    fio-devcontainer \
    bash ./test_fio.sh
