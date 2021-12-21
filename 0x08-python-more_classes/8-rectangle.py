#!/usr/bin/python3
"""Rectangle class that defines a rectangle"""


class Rectangle:
    """Represent a rectangle class
    Defined by width and height

    Attributes:
         number_of_instances: number of Rectangle instances,
         increments with every instantiation,
         decrements with every deletion,
     """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialise the attribute width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += str(self.print_symbol)
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a Rectangle instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """Sets the height of a Rectangle instance"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        """sets the height of a rectangle instance"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    """Create public instance method: area"""
    def area(self):
        return (self.__height * self.__width)

    """Create public instance method: perimeter"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method that returns the biggest rectangle based on the area

        Ärgs:
            rect_1: Rectangle instance
            rect_2: rectangle instance different from rect_1

        Returns:
            The instance with the biggest area,
            or rect_1 if both rectangles have the same area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() 0r rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
