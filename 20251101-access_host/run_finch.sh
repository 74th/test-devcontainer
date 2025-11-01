#!/bin/bash
finch build -t test .
finch run --rm test test.sh
