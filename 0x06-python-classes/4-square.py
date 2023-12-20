#!/usr/bin/python3

""" Define the square class """

class Square:

    """ represent an object """
    def __init__(self, size=0):

        """ Intialize the attribute [size] """
        self.__size = size

    @property
    def size(self):
        """ Return the size  attribute"""
        return (self.__size)


    @size.setter
    def size(self, value):
        """ setting value to the size attribute """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """ Returing the area of the square """
        return (self.__size * self.__size)
