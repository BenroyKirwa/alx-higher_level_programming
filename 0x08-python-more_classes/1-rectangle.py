#!/usr/bin/python3
"""
Creating class Rectangle
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle by width and height
    """

    def __init__(self,width=0,height=0):
        """
        Instantiation with optional width and height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        method that return value of width
        """
        return self.__width

    @width.setter
    def width(self,value):
        """
        Method to set the width of a rectangle
        """
        if not isinstance(value,int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """
        Sets the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self,value):
        """
        method to set the length of a rectangle
        """
        if not isinstance(value,int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
