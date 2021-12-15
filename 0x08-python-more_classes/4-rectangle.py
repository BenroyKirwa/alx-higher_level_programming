#!/usr/bin/python3
"""
Creating class Rectangle
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle by width and height
    """

    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    number_of_instances = 0
    print_symbol = "#"

    @property
    def width(self):
        """ method that returns the value of the width

        Returns:
            width of the rectangle


        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Attribute to set the width of a rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """ method that returns the value of the height

        Returns:
            height of the rectangle


        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Attribute to set the length of a rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """
        Method that returns the rectangle area
        area = width * height
        """
        return(self.width * self.height)

    def perimeter(self):
        """
        Method that returns the rectangle perimeter
        perimeter = 2(width + height)
        """
        if self.width == 0:
            return 0
        elif self.height == 0:
            return 0
        else:
            return((self.width + self.height)*2)

    def __str__(self):
        """
        Prints the rectangle with the character #
        """
        spc = ""
        if self.width == 0:
            return spc
        elif self.height == 0:
            return spc
        else:
            for i in range(self.height):
                spc += (str(self.print_symbol)*self.width) + "\n"
            return str(spc[:-1])

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
