#!/usr/bin/python3
"""This is a module housing the Square class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square clas inherits from the Rectangle class

    The Square is a unique rectangle that has both width == height

    Attributes:
        size: the size of the square denoting both its width and height
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates the square class.

        Args:
            size: Size of the square
            x (int, optional): horizontal spacing when displaying square
            y (int, optional): vertical spacing when displaying square
            id (optional): unique id of instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """updates the value of size which is the width and height of parent

        size must be an integer and be greater than 0 else a TypeError and
        Valueerror is raised respectively.
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        attribute_value = ["id", "size", "x", "y"]

        if args:
            for attribute, value in zip(attribute_value, args):
                setattr(self, attribute, value)

        elif kwargs:
            for attribute, value in kwargs.items():
                setattr(self, attribute, value)
