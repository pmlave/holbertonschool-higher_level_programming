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

    def integer_validator1(self, name, value):
        '''Checks integer value for height or width'''
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be > 0".format(name))

    @property
    def size(self):
        '''Getter for public attribute size'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setting the variables to equal size'''
        self.integer_validator1("width", value)
        self.width = value

    def update(self, *args, **kwargs):
        '''Setting variables based on args passed in'''
        if args and len(args) >= 1:
            print(len(args))
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
