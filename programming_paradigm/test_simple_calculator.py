import unittest
from simple_calculator import SimpleCalculator



class TestSimpleCalculator(unittest.TestCase):
    """
    A Test Class for Simple Calulator Class
    """
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """tests add function"""
        self.assertEqual(self.calc.add(4, 6), 10)
        self.assertEqual(self.calc.add(-6, -2), -8)
        with self.assertRaises(TypeError):
            self.calc.add('hi', 5)

    def test_subtract(self):
        """tests subtract function"""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(-8, -4), -4)
        with self.assertRaises(TypeError):
            self.calc.subtract('5', 5)

    def test_multiply(self):
        """tests multiply function"""
        self.assertEqual(self.calc.multiply(4, 6), 24)
        self.assertEqual(self.calc.multiply(-6, -2), 12)
       

    def test_divide(self):
        """tests divide function"""
        self.assertEqual(self.calc.divide(10, 4), 2.5)
        self.assertEqual(self.calc.divide(-8, -4), 2)
        self.assertEqual(self.calc.divide(4, 0), None)
        with self.assertRaises(TypeError):
            self.calc.divide('5', 5)


if __name__ == '__main__':
    unittest.main()
