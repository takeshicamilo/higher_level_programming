#!/usr/bin/python3
""" square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ init method """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str method """

        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x, self.y, self.width))

    @property
    def size(self):
        """ size method """
        return self.width

    @size.setter
    def size(self, size):
        """ size setter method """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update method """

        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]

        else:
            if len(kwargs) > 0:
                keys = kwargs.keys()
                for i in keys:
                    if i == 'id':
                        self.id = kwargs['id']
                    if i == 'size':
                        self.width = kwargs['size']
                        self.height = kwargs['size']
                    if i == 'x':
                        self.x = kwargs['x']
                    if i == 'y':
                        self.y = kwargs['y']

    def to_dictionary(self):
        """ dictionary method """

        new_dictionary = {}
        new_dictionary["id"] = self.id
        new_dictionary["size"] = self.width
        new_dictionary["x"] = self.x
        new_dictionary["y"] = self.y
        return new_dictionary
