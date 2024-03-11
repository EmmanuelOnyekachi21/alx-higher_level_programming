#!/usr/bin/python3
"""Defines a square class"""
class Square:
    """A square class
    
    Attributes:
    __size (int): Private attribute representing the size of the square.
    
    Methods:
    __init__(self , size):
    initializes a square instance with a given size.
    """
    def __init__(self, size=0) -> None:
        self.set_size(size)
        
    def get_size(self):
        return self.__size
    
    def set_size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
