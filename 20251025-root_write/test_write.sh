#!/bin/bash
set -ex
echo hoge > ./${TARGET}
chown `id -u`:`id -g` ./${TARGET}
ls -al ./tmp/
