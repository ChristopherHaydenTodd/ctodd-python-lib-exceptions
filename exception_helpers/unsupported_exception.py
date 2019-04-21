"""
    Purpose:
        UnsupportedException Class. Currently Does Nothing, but allows
        for sepcific callouts of failures in create_exceptions
"""


class UnsupportedException(Exception):
    """
    Purpose:
        An Unsupported Exception is raised when the lib is asked to try
        and raise an exception that has yet to be programmed. this way,
        som exception is raised, but it can be handled in a way that
        knows the specified exception isn't raised
    """

    pass
