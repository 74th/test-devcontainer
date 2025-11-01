#!/bin/bash
podman build -t test .
podman run --rm test test.sh
