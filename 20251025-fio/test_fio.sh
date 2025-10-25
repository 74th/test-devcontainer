#!/bin/bash
set -ex

DATA_DIR="./tmp"
NAME=${NAME:-"__"}

fio -io_size=10g \
    -runtime=10 \
    -direct=1 \
    -invalidate=1 \
    -ioengine=posixaio \
    -iodepth=1 \
    -group_reporting \
    -rw=read \
    -size=10g \
    -directory=${DATA_DIR} \
    -bs=20m \
    -numjobs=1 \
    -name=sequential-read \
    -output=results/${NAME}-sequential-read.txt

fio -io_size=10g \
    -runtime=10 \
    -direct=1 \
    -invalidate=1 \
    -ioengine=posixaio \
    -iodepth=1 \
    -group_reporting \
    -rw=write \
    -size=10g \
    -directory=${DATA_DIR} \
    -bs=20m \
    -numjobs=1 \
    -name=sequential-write \
    -output=results/${NAME}-sequential-write.txt

fio -io_size=1g \
    -runtime=10 \
    -direct=1 \
    -invalidate=1 \
    -ioengine=posixaio \
    -iodepth=1 \
    -group_reporting \
    -rw=randread \
    -size=1g \
    -directory=${DATA_DIR} \
    -bs=4k \
    -numjobs=16 \
    -name=random-read-4KB-16Thread \
    -output=results/${NAME}-random-read-4K-16Thread.txt

fio -io_size=1g \
    -runtime=10 \
    -direct=1 \
    -invalidate=1 \
    -ioengine=posixaio \
    -iodepth=1 \
    -group_reporting \
    -rw=randwrite \
    -size=1g \
    -directory=${DATA_DIR} \
    -bs=4k \
    -numjobs=16 \
    -name=random-read-4KB-16Thread \
    -output=results/${NAME}-random-write-4K-16Thread.txt
