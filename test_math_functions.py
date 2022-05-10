import unittest
from math_functions import *


class MyTestCase(unittest.TestCase):
    """
    class to test the functions of the math_functions module
    """

    def test_area_of_circle(self):
        """
        to test the area_of_circle function
        """
        self.assertAlmostEqual(area_of_circle(1), 3.14, delta=0.002)
        self.assertAlmostEqual(area_of_circle(1.0), 3.14, delta=0.002)
        with self.assertRaises(TypeError):
            area_of_circle('1')
        with self.assertRaises(ValueError):
            area_of_circle(-1)
            area_of_circle(0)

    def test_area_of_square(self):
        """"
        to test the area_of_square function
        """
        self.assertEqual(area_of_square(2), 4.0)
        self.assertEqual(area_of_square(2.0), 4.0)
        with self.assertRaises(TypeError):
            area_of_square('1')
        with self.assertRaises(ValueError):
            area_of_square(-1)
            area_of_square(0)

    def test_area_of_triangle(self):
        """
        to test the area_of_triangle function
        """
        self.assertEqual(area_of_triangle(1, 2), 1.0)
        self.assertEqual(area_of_triangle(1.0, 2), 1.0)
        self.assertEqual(area_of_triangle(2.0, 1), 1.0)
        self.assertEqual(area_of_triangle(2.0, 1.0), 1.0)
        with self.assertRaises(TypeError):
            area_of_triangle(1, '2')
            area_of_triangle('1', 2)
            area_of_triangle('1', '2')
        with self.assertRaises(ValueError):
            area_of_triangle(-1, 2)
            area_of_triangle(1, -2)
            area_of_triangle(-1, -2)
            area_of_triangle(0, 2)
            area_of_triangle(1, 0)
            area_of_triangle(0, 0)

    def test_area_of_rectangle(self):
        """
        to test the area_of_rectangle function
        """
        self.assertEqual(area_of_rectangle(1, 2), 2.0)
        self.assertEqual(area_of_rectangle(1.0, 2), 2.0)
        self.assertEqual(area_of_rectangle(1, 2.0), 2.0)
        self.assertEqual(area_of_rectangle(1.0, 2.0), 2.0)
        with self.assertRaises(TypeError):
            area_of_rectangle(1, '2')
            area_of_rectangle('1', 2)
            area_of_rectangle('1', '2')
        with self.assertRaises(ValueError):
            area_of_rectangle(-1, 2)
            area_of_rectangle(1, -2)
            area_of_rectangle(-1, -2)
            area_of_rectangle(0, 2)
            area_of_rectangle(1, 0)
            area_of_rectangle(0, 0)

    def test_exponent(self):
        self.assertEqual(exponent(1, 2), 1)
        self.assertEqual(exponent(1.0, 2), 1)
        self.assertEqual(exponent(1, 2.0), 1)
        self.assertEqual(exponent(1.0, 2.0), 1)
        self.assertEqual(exponent(1, 1.5), 1)
        self.assertEqual(exponent(-1, 1), -1)
        self.assertEqual(exponent(1, -1), 1)
        self.assertEqual(exponent(-1, -1), -1)
        with self.assertRaises(TypeError):
            exponent('1', 1)
            exponent(1, '1')
            exponent('1', '1')

    def test_factorial(self):
        """
        to test the factorial function
        """
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1.0), 1.0)
        with self.assertRaises(TypeError):
            factorial('1')
            factorial('-1')
            factorial(2.5)
        with self.assertRaises(ValueError):
            factorial(-1)
            factorial(-2)

    def test_permutation(self):
        """
        to test the permutation function
        """
        self.assertEqual(permutation(1, 1), 1)
        self.assertEqual(permutation(0, 1), 0)
        self.assertEqual(permutation(1, 0), 1)
        self.assertEqual(permutation(0, 0), 1)
        self.assertEqual(permutation(1.0, 1), 1)
        self.assertEqual(permutation(1, 1.0), 1)
        self.assertEqual(permutation(1.0, 1.0), 1)
        self.assertEqual(permutation(5, 2), 20)
        with self.assertRaises(TypeError):
            permutation('1', 1)
            permutation(1, '1')
            permutation('1', '1')
        with self.assertRaises(ValueError):
            permutation(-1, 1)
            permutation(1, -1)
            permutation(-1, -1)

    def test_combination(self):
        """
        to test the combination function
        """
        self.assertEqual(combination(1, 1), 1)
        self.assertEqual(combination(0, 1), 0)
        self.assertEqual(combination(1, 0), 1)
        self.assertEqual(combination(0, 0), 1)
        self.assertEqual(combination(1.0, 1), 1)
        self.assertEqual(combination(1, 1.0), 1)
        self.assertEqual(combination(1.0, 1.0), 1)
        self.assertEqual(combination(5, 2), 10)
        with self.assertRaises(TypeError):
            combination('1', 1)
            combination(1, '1')
            combination('1', '1')
        with self.assertRaises(ValueError):
            combination(-1, 1)
            combination(1, -1)
            combination(-1, -1)


if __name__ == '__main__':
    unittest.main()

