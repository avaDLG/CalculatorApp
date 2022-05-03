import math


def area_of_circle(radius):
    if radius <= 0:
        raise ValueError
    return math.pi * math.pow(radius, 2)


def area_of_square(side_length):
    if type(side_length) != int and type(side_length) != float:
        raise TypeError
    if side_length <= 0:
        raise ValueError
    return math.pow(side_length, 2)


def area_of_triangle(base, height):
    if type(base) != int and type(base) != float and type(height) != int and type(height) != float:
        raise TypeError
    if base <= 0 or height <= 0:
        raise ValueError
    return 0.5 * base * height


def area_of_rectangle(base, height):
    if type(base) != int and type(base) != float and type(height) != int and type(height) != float:
        raise TypeError
    if base <= 0 or height <= 0:
        raise ValueError
    return base * height


def exponent(base, power):
    if type(base) != int and type(base) != float and type(power) != int and type(power) != float:
        raise TypeError
    if base <= 0 or power <= 0:
        raise ValueError
    if power == 1:
        return base
    else:
        return base * exponent(base, power-1)


def factorial(num):
    if num <= 0:
        raise ValueError
    if num == 1:
        return num
    else:
        return num * factorial(num-1)


def permutation(num1, num2):
    if num1 <= 0 or num2 <= 0:
        raise ValueError
    elif num1 < num2:
        return 0
    elif num1 == num2:
        return factorial(num1)
    else:
        return factorial(num1) / factorial(num1 - num2)


def combination(num1, num2):
    if num1 <= 0 or num2 <= 0:
        raise ValueError
    if num1 < num2:
        return 0
    elif num1 == num2:
        return 1
    else:
        return factorial(num1) / (factorial(num2) * factorial(num1 - num2))

