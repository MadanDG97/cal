import unittest
from calculator import add, subtract, multiply

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

if __name__ == '__main__':
    unittest.main()
