"""
    Purpose:
        Exception Helpers. This file shows exception types in Python and function
        calls for generating specific exceptions. This can be useful for
        unittesting, debugging, and other tasks that might call for purposefully
        breaking parts of your code.
"""

# Python Library Imports
import logging
import random

# Local Library Imports
from exception_helpers.unsupported_exception import UnsupportedException


###
# Exception Generator
###


def create_and_throw_exception(exception_name=None):
    """
        Purpose:
            Create and Throw an exception from the exception
            types in the file. if exception_name is passed in,
            throw that specific exception if it has been
            coded in the library
        Args:
            exception_name (String ExceptionType): Type of exception
                to throw
        Returns:
            N/A: should never return, should always raise
    """

    exception_types = {
        "ZeroDivisionError": create_zero_division_exception,
        "OverflowError": create_overflow_exception,
        "TypeError": create_type_exception,
        "AssertionError": create_assertion_exception,
        "AttributeError": create_attribute_exception,
        "NameError": create_name_exception,
        "IndexError": create_index_exception,
        "KeyError": create_key_exception,
        "UnboundLocalError": create_unbound_local_exception,
    }

    if not exception_name:
        exception_name, exception_func = random.choice(list(exception_types.items()))
    else:
        exception_func = exception_types.get(exception_name, None)
        if not exception_func:
            raise UnsupportedException(f"Library does not support {exception_name} yet")

    try:
        logging.info(f"Throwing {exception_name} Exception")
        exception_func()
    except Exception as err:
        logging.info(f"{exception_name} Exception Captured: {err}")
        raise err


###
# Throw Specific Exception
###


def create_zero_division_exception():
    """
        Purpose:
            Throw ZeroDivisionError Exception
        Args:
            N/A
        Returns:
            N/A
    """

    2 / 0


def create_overflow_exception():
    """
        Purpose:
            Throw OverflowError Exception
        Args:
            N/A
        Returns:
            N/A
    """

    pi = 0
    for k in range(350):
        pi += (
            4.0 / (8.0 * k + 1.0) - 1.0 / (8.0 * k + 5.0) - 1.0 / (8.0 * k + 6.0)
        ) / 16.0 ** k


def create_type_exception():
    """
        Purpose:
            Throw TypeError Exception
        Args:
            N/A
        Returns:
            N/A
    """

    10 / "a"


def create_assertion_exception():
    """
        Purpose:
            Throw AssertionError Exception
        Args:
            N/A
        Returns:
            N/A
    """

    assert False


def create_attribute_exception():
    """
        Purpose:
            Throw AttributeError Exception
        Args:
            N/A
        Returns:
            N/A
    """

    class TestClass:
        def __init__(self):
            pass

    test_class_object = TestClass()
    x = test_class_object.some_missing_property


def create_name_exception():
    """
        Purpose:
            Throw NameError Exception
        Args:
            N/A
        Returns:
            N/A
    """

    test_class_object = TestClass()


def create_index_exception():
    """
        Purpose:
            Throw IndexError Exception
        Args:
            N/A
        Returns:
            N/A
    """

    test_list = [0, 1, 2, 3, 4]
    test_list[5]


def create_key_exception():
    """
        Purpose:
            Throw KeyError Exception
        Args:
            N/A
        Returns:
            N/A
    """

    test_dict = {"name": "chris"}
    test_dict["height"]


def create_unbound_local_exception():
    """
        Purpose:
            Throw UnboundLocalError Exception
        Args:
            N/A
        Returns:
            N/A
    """

    print(hello_message)
    hello_message = "Setting Value After Usage"
