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

    @property
    def size(self):
        '''Getter for public attribute size'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setting the variables to equal size'''
        self.integer_validator1("width", value)
        self.width = value

    def integer_validator1(self, name, value):
        '''Checks integer value for height or width'''
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be > 0".format(name))
#
