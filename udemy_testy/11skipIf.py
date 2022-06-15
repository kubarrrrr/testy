from datetime import date
import unittest


class Container:

    def __init__(self):
        if date.today().day % 2 == 0:
            self.code = 'XC-0'
        else:
            self.code = 'XC-1'


class TestContainer(unittest.TestCase):
    
    @unittest.skipIf(date.today().day % 2 != 0, "Skipping odd days.")
    def test_skipping_odd_days(self):
        c = Container()
        self.assertTrue(c.code.endswith('0'), 'Invalid code attribute.')
    
    @unittest.skipIf(date.today().day % 2 == 0, "Skipping even days.")
    def test_skipping_even_days(self):
        c = Container()
        self.assertTrue(c.code.endswith('1'), 'Invalid code attribute.')

if __name__ == '__main__':
    unittest.main()