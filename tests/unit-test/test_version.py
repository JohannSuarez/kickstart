"""
Showcasing two different ways to properly test your code

1. By importing the package in directly.
2. By passing in a function fixture defined in conftest.py
"""
import kickstart as ks


def test_version():
    """
    testing version from importing it
    """
    assert ks.__version__ == '1.0.0'


def test_version_using_fixture(version_test):
    """
    testing version from passing the module
    in as a fixture
    """
    assert version_test.__version__ == '1.0.0'


def test_pkgname_using_fixture(version_test):
    """
    testing pkgname from passing the module
    in as a fixture
    """
    assert version_test.__package__ == 'kickstart'
