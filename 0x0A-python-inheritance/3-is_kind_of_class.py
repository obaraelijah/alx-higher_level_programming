#!/usr/bin/python3
""" This defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an inherited instance of class
    Args:
        obj (any): Object to check
        a_class (type): class to match object type to
    Returns:
        If obj is an inherited instance of a_class - True
        Otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
