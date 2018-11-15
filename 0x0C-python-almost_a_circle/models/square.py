#!/usr/bin/python3
'''New square class that inherits from rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''New class Square'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y)
        self.size = size
        if id is not None:
            self.id = id

    def __str__(self):
        return "[{}] ({}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.size)


#
