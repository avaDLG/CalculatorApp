import math


def area_of_circle(radius):
    if type(radius) != int and type(radius) != float:
        raise TypeError("Not numerical input")
    if radius <= 0:
        raise ValueError("Not a positive length")
    return math.pi * math.pow(radius, 2)


def area_of_square(side_length):
    if type(side_length) != int and type(side_length) != float:
        raise TypeError("Not numerical data")
    if side_length <= 0:
        raise ValueError("Not a positive length")
    return math.pow(side_length, 2.0)


def area_of_triangle(base, height):
    if type(base) != int and type(base) != float and type(height) != int and type(height) != float:
        raise TypeError("Not numerical data")
    if base <= 0 or height <= 0:
        raise ValueError("Not positive length")
    return 0.5 * base * height


def area_of_rectangle(base, height):
    if type(base) != int and type(base) != float and type(height) != int and type(height) != float:
        raise TypeError("Not numerical data")
    if base <= 0 or height <= 0:
        raise ValueError("Not positive length")
    return base * height
