#!/bin/bash
set -x

echo "test host.docker.internal"
curl -s http://host.docker.internal:8080/

export HOST_IP=$(ip route | awk '/default/ {print $3}')
echo "test $HOST_IP"
curl -s http://${HOST_IP}:8080/
