#!/bin/sh
set -e
mypy .
usort format .
black .
