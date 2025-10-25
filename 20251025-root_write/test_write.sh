#!/bin/bash
set -ex
CONTAINER_UID=`id -u`
CONTAINER_GID=`id -g`
echo hoge > ./${TARGET}
chown ${CONTAINER_UID}:${CONTAINER_GID} ./${TARGET}
ls -al ./tmp
