#!/bin/bash
docker context use default

docker build -t test .
docker run --rm test test.sh
