#!/usr/bin/env bash

set -e

. "$VIRTUAL_ENV"/bin/activate

export FLASK_APP=flask_mega_tutorial.wsgi

flask db upgrade

exec tini -- flask db migrate "$@"
