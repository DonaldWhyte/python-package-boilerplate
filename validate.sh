#/usr/bin/env sh
# Script which runs a set of validations and tests against the codebase.

set -e

# Ensure all code is pep8 compliant 
pep8 proj
pep8 tests

# Run all unit tests
nosetests
