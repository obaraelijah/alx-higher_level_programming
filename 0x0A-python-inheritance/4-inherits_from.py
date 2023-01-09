#!/usr/bin/python3
"""4-inherits_from.py """


def inherits_from(obj, a_class):
    """
    Returns True if the obj is an instance of a class that
    inherited from the specified class
    otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
