#!/usr/bin/python3
"""
Creating class Rectangle
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle by width and height
    """

    def width(self,value):
        """
        Attribute to set the width of a rectangle
        """
        if not isinstance(value,int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")

    def height(self,value):
        """
        Attribute to set the length of a rectangle
        """
        if not isinstance(value,int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")

    number_of_instances = 0

    def __init__(self,width=0,height=0):
        """
        Instantiation with optional width and height
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
        print_symbol = "#"

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
        if self.width == 0:
            print()
        elif self.height == 0:
            print()
        else:
            for i in range(0,self.height):
                for k in range(self.width):
                    print("#",end='')
                print()
            return str()

    def __repr__(self):
        return "Rectangle({:d},{:d})".format(self.width,self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
