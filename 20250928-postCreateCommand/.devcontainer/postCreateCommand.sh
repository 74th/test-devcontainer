#!/bin/bash

echo "Running postCreateCommand.sh"

LOGFILE=/home/vscode/postCreateCommand.log

echo "uid:" `id` 2>&1 | tee -a $LOGFILE
echo "time:" `time` 2>&1 | tee -a $LOGFILE
