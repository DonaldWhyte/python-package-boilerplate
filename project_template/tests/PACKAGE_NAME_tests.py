from nose.tools import *
import PACKAGE_NAME


def setup():
    print "SETUP!"


def teardown():
    print "TEAR DOWN!"


def test_basic():
    PACKAGE_NAME.hello()
