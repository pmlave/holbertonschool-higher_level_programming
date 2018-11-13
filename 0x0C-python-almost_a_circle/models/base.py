#!/usr/bin/python3
"""Base for all other classes and methods"""


class Base:
    """Base class beginning"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor for base"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
