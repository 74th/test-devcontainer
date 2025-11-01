#!/bin/bash
docker context use rancher-desktop

docker build -t test .
docker run --rm test test.sh
