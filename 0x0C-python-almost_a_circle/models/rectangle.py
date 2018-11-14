#!/usr/bin/python3
'''New inheriting class for Base'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class that inherits from base class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''init method that calls parent init'''
        super().__init__()
        if id is not None:
            self.id = id
        self.integer_validator1("width", width)
        self.integer_validator1("height", height)
        self.integer_validator2("x", x)
        self.integer_validator2("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def integer_validator1(self, name, value):
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be > 0".format(name))

    def integer_validator2(self, name, value):
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        '''Private width attribute getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Private width attribute setter'''
        self.integer_validator1("width", value)
        self.__width = value

    @property
    def height(self):
        '''Private height attribute getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Private height attribute setter'''
        self.integer_validator1("height", value)
        self.__height = value

    @property
    def x(self):
        '''Private x attribute getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Private x attribute setter'''
        self.integer_validator2("x", value)
        self.__x = value

    @property
    def y(self):
        '''Private y attribute getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Private y attribute setter'''
        self.integer_validator2("y", value)
        self.__y = value