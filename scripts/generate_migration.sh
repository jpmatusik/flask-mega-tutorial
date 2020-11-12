#!/usr/bin/env bash

set -e

ORIGINAL_PWD=$PWD
SCRIPT_DIR="$(cd -- "$(dirname -- "$0")" && pwd)"
BASE_DIR="$(dirname -- "$SCRIPT_DIR")"

function cleanup {
  cd $ORIGINAL_PWD
}

trap cleanup EXIT

ARGS="--help"
if [ -n "$1" ]
  then
    ARGS="$@"
fi

cd $BASE_DIR
echo INFO: starting the database
docker-compose up -d postgres
echo INFO: running exiting migrations
docker-compose run --rm app flask db upgrade
echo INFO: running migration entrypoint
docker-compose run --rm --entrypoint /usr/local/bin/migration-entrypoint.sh app "$ARGS"
