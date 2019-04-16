#!/bin/bash

set -e

while sleep 1; do
    mem=$(ps -o rss --no-headers $1)
    echo "$(date +"%s") $mem"
done
