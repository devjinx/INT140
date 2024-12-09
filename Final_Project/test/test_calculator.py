import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_calculate_total(self):
        menu = {"Burger": 5.99, "Fries": 2.99}
        total = Calculator.calculate_total(["Burger", "Fries"], menu)
        self.assertEqual(total, 8.98)

    def test_item_not_in_menu(self):
        menu = {"Burger": 5.99}
        with self.assertRaises(ValueError):
            Calculator.calculate_total(["Pizza"], menu)