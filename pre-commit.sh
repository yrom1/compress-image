#!/bin/sh
set -x
mypy .
usort format .
black .
