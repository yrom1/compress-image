set -x
mypy .
usort format .
black .
