
# Makefile setup

SHELL := /bin/bash

SRCDIR = bootstrapvz
TEST_SRCDIR = tests

PYC_FILES := $(shell find ./$(MAIN_SRCDIR) -name "*.pyc")
TEST_PYC_FILES := $(shell find ./$(TEST_SRCDIR) -name "*.pyc.*")

## Python Environments

DEFAULT_PY_ENV ?= py27
TOXENV = $(DEFAULT_PY_ENV)

.DEFAULT_GOAL := all
.PHONY: all clean unit_tests integration_tests

all: clean lint unit_tests integration_tests format_with_yapf

clean:
	-rm -r $(PYC_FILES) $(TEST_PYC_FILES)
	-rm $(shell find . -name '*.log')
	-rm -r .tox_output
	-rm -r .tox

pylint:
	set -o pipefail; pylint --rcfile pylintrc bootstrap-vz-server  bootstrap-vz bootstrap-vz-remote bootstrapvz | tee ./pylint.log

unit_tests:
	@echo "Run Unit Tests"
	tox -e unit


integration_tests:
	@echo "Run Unit Tests"
	tox -e integration

format_with_yapf:
	./format_w_yapf.sh
