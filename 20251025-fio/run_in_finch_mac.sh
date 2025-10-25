#!/bin/bash
set -ex

finch build -t fio-devcontainer .
finch run --rm \
    -e NAME=finch_mac \
    --mount type=bind,source=$(pwd),target=/workspace \
    -w /workspace \
    fio-devcontainer \
    bash ./test_fio.sh
