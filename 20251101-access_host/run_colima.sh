#!/bin/bash
docker context use colima

docker build -t test .
docker run --rm test test.sh
