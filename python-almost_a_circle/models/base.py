#!/usr/bin/python3
"""Module the "base" class"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
