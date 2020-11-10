#!/usr/bin/env bash

set -e

if [ -z "$1" ]
  then
    echo "ERROR: Pass the target build stage as the first positional argument." >&2
    exit 1
fi

SCRIPT_DIR="$(cd -- "$(dirname -- "$0")" && pwd)"
BASE_DIR="$(dirname -- "$SCRIPT_DIR")"

docker build -t flask-mega-tutorial:$1 -f "$BASE_DIR/docker/Dockerfile" --target $1 "$BASE_DIR"
