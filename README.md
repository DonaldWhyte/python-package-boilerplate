# python-package-boilerplate

Simple boilerplate for Python packages and applications.

Features:

* `bin/` directory to store executable and installable scripts
* empty package generation
* unit test boilerplate
* .travis.yml file
    - builds against 2.7 and all 3.0+ versions
* .gitignore file
* `validate.sh` script for running unit tests and pep8 and pep257 validators
    - run in Travis build
* `setup.py` to install package and scripts

## How to Generate Boilerplate

Clone this repository and run:

```
cd python-package-boilerplate
./generate.py PROJECT_NAME
```

where `PROJECT_NAME` is the name of your Python project/package.

## Running Unit Tests in Generate Project

Run PEP8 and PEP257 validations and unit tests by executing the generated `validate.sh` script.

## Installing Generated Projects

Use the generated `setup.py` script to install packages/scripts generated from the boilerplate like so:

```
python setup.py install
```
