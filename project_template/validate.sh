#/usr/bin/env bash
# Script which runs a set of validations and tests against the codebase.

set -e

# Ensure all code is pep8 compliant
pep8 PACKAGE_NAME
pep8 tests

# Ensure production code is pep257 (docstring) compliant
pep257 PACKAGE_NAME

# Run all unit tests
nosetests
