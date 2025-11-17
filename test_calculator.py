import unittest
import calculator
import math

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-5, -5), -10)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(10, 5), 50)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(5, 0), 0)

    def test_divide(self):
        self.assertAlmostEqual(calculator.div(10, 5), 2)
        self.assertAlmostEqual(calculator.div(-1, 1), -1)
        self.assertAlmostEqual(calculator.div(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(10, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(1), 0)
        self.assertAlmostEqual(calculator.logarithm(math.e), 1)
        self.assertAlmostEqual(calculator.logarithm(100), 4.605170185988092)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)
        self.assertAlmostEqual(calculator.hypotenuse(8, 15), 17)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(16), 4)
        self.assertAlmostEqual(calculator.square_root(100), 10)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()