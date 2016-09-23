#/usr/bin/env bash
# Script which runs a set of validations and tests against the codebase.

set -e

# Ensure all code is pep8 compliant
pep8 proj
pep8 tests

# Ensure production code is pep257 (docstring) compliant
pep257 proj

# Run all unit tests
nosetests
