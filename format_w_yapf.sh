#!/usr/bin/env bash

#
# Test making the wheel and then installing it
#

set -e

#
# Use yapf to format source code
#

set +e
yapf --in-place --recursive setup.py  bootstrap-vz-server  bootstrap-vz bootstrap-vz-remote bootstrapvz
set -e

make clean
make unit_tests
