#!/usr/bin/python3
"""
This module describes a function that
lists available attributes and methods
"""


def lookup(obj):
    """Returns a list of available attributes and methods.
    Args: obj - an object
    """

    return dir(obj)
