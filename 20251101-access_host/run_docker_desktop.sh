#!/bin/bash
docker context use desktop-linux

docker build -t test .
docker run --rm test test.sh
