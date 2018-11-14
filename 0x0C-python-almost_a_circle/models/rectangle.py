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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''Private width attribute getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Private width attribute setter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Private height attribute getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Private height attribute setter'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        '''Private x attribute getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Private x attribute setter'''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Private y attribute getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Private y attribute setter'''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
