import unittest
from calculator import *


class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(0, 5), 0)

        # Перевірка на викидання винятку для ділення на нуль
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_multiply_list(self):
        self.assertEqual(multiply_list([1, 2, 3]), 6)

        self.assertEqual(multiply_list([2, 2, 2]), 8)

if __name__ == '__main__':
    unittest.main()
