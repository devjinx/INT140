import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_calculate_total_with_quantity(self):
        menu = {"Burger": 59.99, "Fries": 29.99}
        order = {"Burger": 2, "Fries": 1}
        total = Calculator.calculate_total_with_quantity(order, menu)
        self.assertEqual(total, 149.97)

    def test_item_not_in_menu(self):
        menu = {"Burger": 59.99}
        order = {"Pizza": 1}
        with self.assertRaises(ValueError):
            Calculator.calculate_total_with_quantity(order, menu)
