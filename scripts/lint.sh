#!/usr/bin/env bash

SCRIPT_DIR="$(cd -- "$(dirname -- "$0")" && pwd)"
BASE_DIR="$(dirname -- "$SCRIPT_DIR")"

isort --settings-path "$BASE_DIR/pyproject.toml" "$BASE_DIR"
