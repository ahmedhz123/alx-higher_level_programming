#!/usr/bin/python3

""" define a square class """

class Square:
    """ represent a square """


    def __init__(self, size=0):

        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
        """ define a function that returns the area of the square """
        def area(self):
            return (self.__size * self.__size)
