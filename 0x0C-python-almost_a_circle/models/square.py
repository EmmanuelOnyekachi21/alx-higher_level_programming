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
