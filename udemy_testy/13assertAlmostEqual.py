import unittest
import math


def area(radius):
    """The function returns the area of the circle."""

    if not (isinstance(radius, (int, float))):
        raise TypeError('The radius must be of type int or float.')

    if not radius > 0:
        raise ValueError('The radius must be positive.')

    return math.pi * radius ** 2
    

# enter your solution here
class TestArea(unittest.TestCase):
    
    def test_circle_area_with_radius_three(self):
        self.assertAlmostEqual(area(1), 3.14159265359, 5)



if __name__ == "__main__":
    unittest.main()