#!/usr/bin/env python3
"""
    Purpose:
        Test File for create_exceptions.py
"""

# Python Library Imports
import os
import sys
import pytest
from unittest import mock

# Import File to Test
# BASE_PROJECT_PATH = f"{os.path.dirname(os.path.realpath(__file__))}/../"
# sys.path.insert(0, BASE_PROJECT_PATH)
import exception_helpers.create_exceptions as create_exceptions
from exception_helpers.unsupported_exception import UnsupportedException


###
# Fixtures
###


@pytest.fixture
def available_exceptions():
    """
    Purpose:
        Available Exceptions That Can Be Generated
    Args:
        N/A
    Return:
        available_exceptions (Pytest Fixture (Dict of Exceptions)): Available
            Exceptions That Can Be Generated
    """

    return {
        "ZeroDivisionError": ZeroDivisionError,
        "OverflowError": OverflowError,
        "TypeError": TypeError,
        "AssertionError": AssertionError,
        "AttributeError": AttributeError,
        "NameError": NameError,
        "IndexError": IndexError,
        "KeyError": KeyError,
        "UnboundLocalError": UnboundLocalError,
    }


@pytest.fixture
def unsupported_exception():
    """
    Purpose:
        Unsupported Exception That Cannot Be Generated
    Args:
        N/A
    Return:
        unsupported_exceptions (Pytest Fixture (Dict of Exception)): Unsupported
            Exception
    """

    return ["UnsupportedException", UnsupportedException]


###
# Mocked Functions
###


# N/A


###
# Test Payload
###


def test_create_and_throw_exception_specifid(available_exceptions):
    """
    Purpose:
        Tests that create_and_throw_exception returns all known exceptions
        when each is specified when calling the function
    Args:
        available_exceptions (Pytest Fixture (List of Exceptions)): Available
            Exceptions That Can Be Generated
    Return:
        N/A
    """

    for exception_name, exception_type in available_exceptions.items():
        with pytest.raises(exception_type):
            create_exceptions.create_and_throw_exception(exception_name)


def test_create_and_throw_exception_not_specified(available_exceptions):
    """
    Purpose:
        Tests that create_and_throw_exception returns a known exceptions
        when no specific exception is specified
    Args:
        available_exceptions (Pytest Fixture (List of Exceptions)): Available
            Exceptions That Can Be Generated
    Return:
        N/A
    """

    possible_exceptions = tuple(
        [
            available_exceptions[exception_name]
            for exception_name in available_exceptions
        ]
    )

    with pytest.raises(possible_exceptions):
        create_exceptions.create_and_throw_exception()


def test_create_and_throw_exception_unsupported(unsupported_exception):
    """
    Purpose:
        Tests that create_and_throw_exception fails when an unknown exception
        is specified
    Args:
        unsupported_exceptions (Pytest Fixture (Dict of Exception)): Unsupported
            Exception
    Return:
        N/A
    """

    with pytest.raises(unsupported_exception[1]):
        create_exceptions.create_and_throw_exception(unsupported_exception[0])


def test_create_zero_division_exception():
    """
    Purpose:
        Tests that create_zero_division_exception returns a ZeroDivisionError
    Args:
        N/A
    Return:
        N/A
    """

    with pytest.raises(ZeroDivisionError):
        create_exceptions.create_zero_division_exception()


def test_create_overflow_exception():
    """
    Purpose:
        Tests that create_overflow_exception returns a OverflowError
    Args:
        N/A
    Return:
        N/A
    """

    with pytest.raises(OverflowError):
        create_exceptions.create_overflow_exception()


def test_create_type_exception():
    """
    Purpose:
        Tests that create_type_exception returns a TypeError
    Args:
        N/A
    Return:
        N/A
    """

    with pytest.raises(TypeError):
        create_exceptions.create_type_exception()


def test_create_assertion_exception():
    """
    Purpose:
        Tests that create_assertion_exception returns a AssertionError
    Args:
        N/A
    Return:
        N/A
    """

    with pytest.raises(AssertionError):
        create_exceptions.create_assertion_exception()


def test_create_attribute_exception():
    """
    Purpose:
        Tests that create_attribute_exception returns a AttributeError
    Args:
        N/A
    Return:
        N/A
    """

    with pytest.raises(AttributeError):
        create_exceptions.create_attribute_exception()


def test_create_name_exception():
    """
    Purpose:
        Tests that create_name_exception returns a NameError
    Args:
        N/A
    Return:
        N/A
    """

    with pytest.raises(NameError):
        create_exceptions.create_name_exception()


def test_create_index_exception():
    """
    Purpose:
        Tests that create_index_exception returns a IndexError
    Args:
        N/A
    Return:
        N/A
    """

    with pytest.raises(IndexError):
        create_exceptions.create_index_exception()


def test_create_key_exception():
    """
    Purpose:
        Tests that create_key_exception returns a KeyError
    Args:
        N/A
    Return:
        N/A
    """

    with pytest.raises(KeyError):
        create_exceptions.create_key_exception()


def test_create_unbound_local_exception():
    """
    Purpose:
        Tests that create_unbound_local_exception returns a UnboundLocalError
    Args:
        N/A
    Return:
        N/A
    """

    with pytest.raises(UnboundLocalError):
        create_exceptions.create_unbound_local_exception()
