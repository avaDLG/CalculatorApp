import math


def area_of_circle(radius) -> float:
    """
    method to calculate the area of a circle
    :param radius: the circles radius
    :return: the area of the circle
    """
    if radius <= 0:
        raise ValueError
    return math.pi * math.pow(radius, 2)


def area_of_square(side_length) -> float:
    """
    method to calculate the area of a square
    :param side_length: side length of the square
    :return: the area of the square
    """
    if type(side_length) != int and type(side_length) != float:
        raise TypeError
    if side_length <= 0:
        raise ValueError
    return math.pow(side_length, 2)


def area_of_triangle(base, height) -> float:
    """
    method to calculate the area of a triangle
    :param base: the base of the triangle
    :param height: the height of the triangle
    :return: the area of the triangle
    """
    if type(base) != int and type(base) != float and type(height) != int and type(height) != float:
        raise TypeError
    if base <= 0 or height <= 0:
        raise ValueError
    return 0.5 * base * height


def area_of_rectangle(base, height) -> float:
    """
    method to calculate the area of a rectangle
    :param base: the base of the rectangle
    :param height: the height of the rectagle
    :return: the area of a rectangle
    """
    if type(base) != int and type(base) != float and type(height) != int and type(height) != float:
        raise TypeError
    if base <= 0 or height <= 0:
        raise ValueError
    return base * height


def exponent(base, power) -> float:
    """
    method to calculate exponents
    :param base: the base of the equation (what is being multiplied)
    :param power: the power of the equation (how many times it is multiplied)
    :return: the value of the base to the power
    """
    if type(base) != int and type(base) != float and type(power) != int and type(power) != float:
        raise TypeError
    else:
        return math.pow(base, power)


def factorial(num) -> float:
    """
    method to calculate factorials
    :param num: the number to calculate the factorial (multiply by all whole numbers less than num greater than 0)
    :return: the value of num!
    """
    if type(num) == str or (int(num) != float(num)):
        raise TypeError
    if num < 0:
        raise ValueError
    if num == 0:
        return 1
    if num == 1:
        return num
    else:
        return num * factorial(num-1)



def permutation(num1, num2) -> float:
    """
    method to calculate permutations
    :param num1: the first whole number
    :param num2: the second whole number
    :return: the result num1 P num2 (num1 permutation num2)
    """
    if num1 < 0 or num2 < 0:
        raise ValueError
    elif num2 == 0:
        return 1
    elif num1 < num2:
        return 0
    elif num1 == num2:
        return factorial(num1)
    else:
        return factorial(num1) / factorial(num1 - num2)


def combination(num1, num2) -> float:
    """
    method to calculate combinations
    :param num1: the first whole number
    :param num2: the second whole number
    :return: the result num1 C num2 (num1 combination num2)
    """
    if num1 < 0 or num2 < 0:
        raise ValueError
    elif num1 == 0 and num2 == 0:
        return 1
    elif num1 == 0:
        return 0
    elif num1 < num2:
        return 0
    elif num1 == num2:
        return 1
    else:
        return factorial(num1) / (factorial(num2) * factorial(num1 - num2))

