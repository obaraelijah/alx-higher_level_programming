#!/usr/bin/python3
""" This defines a class-checking function."""


def is_same_class(obj, a_class):
    """check if an object is exactly an instance of a given class.
    Args:
        obj (any): The object to check
        a_class (type): the class to match the type of obj
    Returns:
        If obj is exactly an instance of a_class - True
        Otherwise - False
    """
    if type(obj) == a_class:
        return True
    return False
