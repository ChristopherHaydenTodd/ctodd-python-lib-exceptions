# Christopher H. Todd's PROJECT_STRING_NAME

The PROJECT_GIT_NAME project is responsible for ...

The library ...

## Table of Contents

- [Dependencies](#dependencies)
- [Libraries](#libraries)
- [Example Scripts](#example-scripts)
- [Notes](#notes)
- [TODO](#todo)

## Dependencies

### Python Packages

- N/A

## Libraries

### [create_exceptions.py](https://github.com/ChristopherHaydenTodd/ctodd-python-lib-exceptions/blob/master/exceptions_helpers/create_exceptions.py]create_exceptions.py)

Exception Helpers. This file shows exception types in Python and function calls for generating specific exceptions. This can be useful for unittesting, debugging, and other tasks that might call for purposefully breaking parts of your code.

Functions:

```
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
```

```
def create_zero_division_exception():
    """
        Purpose:
            Throw ZeroDivisionError Exception
        Args:
            N/A
        Returns:
            N/A
    """
```

```
def create_overflow_exception():
    """
        Purpose:
            Throw OverflowError Exception
        Args:
            N/A
        Returns:
            N/A
    """
```

```
def create_type_exception():
    """
        Purpose:
            Throw TypeError Exception
        Args:
            N/A
        Returns:
            N/A
    """
```

```
def create_assertion_exception():
    """
        Purpose:
            Throw AssertionError Exception
        Args:
            N/A
        Returns:
            N/A
    """
```

```
def create_attribute_exception():
    """
        Purpose:
            Throw AttributeError Exception
        Args:
            N/A
        Returns:
            N/A
    """
```

```
def create_name_exception():
    """
        Purpose:
            Throw NameError Exception
        Args:
            N/A
        Returns:
            N/A
    """
```

```
def create_index_exception():
    """
        Purpose:
            Throw IndexError Exception
        Args:
            N/A
        Returns:
            N/A
    """
```

```
def create_key_exception():
    """
        Purpose:
            Throw KeyError Exception
        Args:
            N/A
        Returns:
            N/A
    """
```

```
def create_unbound_local_exception():
    """
        Purpose:
            Throw UnboundLocalError Exception
        Args:
            N/A
        Returns:
            N/A
    """
```

### [unsupported_exception.py](https://github.com/ChristopherHaydenTodd/ctodd-python-lib-exceptions/blob/master/exceptions_helpers/create_exceptions.py]unsupported_exception.py)

UnsupportedException Class. Currently Does Nothing, but allows for sepcific callouts of failures in create_exceptions

Classes:

```
class UnsupportedException(Exception):
    """
    Purpose:
        An Unsupported Exception is raised when the lib is asked to try
        and raise an exception that has yet to be programmed. this way,
        som exception is raised, but it can be handled in a way that
        knows the specified exception isn't raised
    """
```

## Example Scripts

Example executable Python scripts/modules for testing and interacting with the library. These show example use-cases for the libraries and can be used as templates for developing with the libraries or to use as one-off development efforts.

### N/A

## Notes

 - Relies on f-string notation, which is limited to Python3.6.  A refactor to remove these could allow for development with Python3.0.x through 3.5.x

## TODO

 - Unittest framework in place, but lacking tests
