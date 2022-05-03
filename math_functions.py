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
    return math.pow(side_length, 2)


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


def exponent(base, power):
    if type(base) != int and type(base) != float and type(power) != int and type(power) != float:
        raise TypeError("Not numerical data")
    if base <= 0 or power <= 0:
        raise ValueError("Not positive length")
    if power == 1:
        return base
    else:
        return base * exponent(base, power-1)


def factorial(num):
    if type(num) != int and type(num) != float:
        raise TypeError("Not numerical data")
    if num <= 0:
        raise ValueError("Not a positive length")
    if num == 1:
        return num
    else:
        return num * factorial(num)


def permutation(num1, num2):
    if type(num1) != int and type(num2) != int:
        raise TypeError("Not whole numerical data")
    if num1 <= 0 or num2 <= 0:
        raise ValueError("Not a positive length")
    return factorial(num1) / factorial(num1 - num2)


def combination(num1, num2):
    if type(num1) != int and type(num2) != int:
        raise TypeError("Not whole numerical data")
    if num1 <= 0 or num2 <= 0:
        raise ValueError("Not a positive length")
    return factorial(num1) / (factorial(num2) * factorial(num1 - num2))

