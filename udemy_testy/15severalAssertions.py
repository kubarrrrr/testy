import unittest
import math


def perimeter(radius):
    """The function returns the length of the circle."""

    if not (isinstance(radius, (int, float))):
        raise TypeError('The radius must be of type int or float.')

    if not radius > 0:
        raise ValueError('The radius must be positive.')

    return 2 * math.pi * radius


# enter your solution here

class TestPerimeter(unittest.TestCase):

    def test_ValueError(self):
        self.assertRaises(TypeError, perimeter, '6')
        self.assertAlmostEqual(perimeter(1), 6.283185307179586, 6)
        self.assertTrue()


if __name__ == '__main__':
    unittest.main()
