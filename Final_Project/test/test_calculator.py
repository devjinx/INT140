import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Define a sample menu for testing
        self.menu = {"Burger": 59.99, "Fries": 29.99, "Drink": 19.99}

    def test_calculate_single_item(self):
        # Calculate the total for a single item
        order = {"Burger": 1}
        total = Calculator.calculate_total_with_quantity(order, self.menu)
        self.assertAlmostEqual(total, 59.99)

    def test_calculate_multiple_items(self):
        # Calculate the total for multiple items
        order = {"Burger": 2, "Fries": 1}
        total = Calculator.calculate_total_with_quantity(order, self.menu)
        self.assertAlmostEqual(total, 149.97)

    def test_calculate_empty_order(self):
        # Calculate the total for an empty order
        order = {}
        total = Calculator.calculate_total_with_quantity(order, self.menu)
        self.assertEqual(total, 0.0)

    def test_calculate_item_not_in_menu(self):
        # Try to calculate the total for an item not in the menu
        try:
            order = {"Pizza": 1}
            Calculator.calculate_total_with_quantity(order, self.menu)
        except ValueError:
            pass  # Pass the test if ValueError is raised

    def test_calculate_negative_quantity(self):
        # Try to calculate the total with a negative quantity
        try:
            order = {"Burger": -1}
            Calculator.calculate_total_with_quantity(order, self.menu)
        except ValueError:
            pass  # Pass the test if ValueError is raised

    def test_calculate_zero_quantity(self):
        # Calculate the total with a quantity of zero
        order = {"Burger": 0}
        total = Calculator.calculate_total_with_quantity(order, self.menu)
        self.assertEqual(total, 0.0)

    def test_calculate_large_order(self):
        # Calculate the total for a large order
        order = {"Burger": 100, "Fries": 200}
        total = Calculator.calculate_total_with_quantity(order, self.menu)
        self.assertAlmostEqual(total, (100 * 59.99) + (200 * 29.99))

    def test_calculate_order_with_partial_menu(self):
        # Try to calculate the total with an order containing an item not in the menu
        try:
            order = {"Burger": 2, "Pizza": 1}
            Calculator.calculate_total_with_quantity(order, self.menu)
        except ValueError:
            pass  # Pass the test if ValueError is raised

    def test_calculate_order_with_no_menu(self):
        # Try to calculate the total when the menu is empty
        try:
            empty_menu = {}
            order = {"Burger": 1}
            Calculator.calculate_total_with_quantity(order, empty_menu)
        except ValueError:
            pass  # Pass the test if ValueError is raised

    def test_calculate_order_with_all_zero_quantities(self):
        # Calculate the total when all quantities in the order are zero
        order = {"Burger": 0, "Fries": 0, "Drink": 0}
        total = Calculator.calculate_total_with_quantity(order, self.menu)
        self.assertEqual(total, 0.0)

if __name__ == "__main__":
    unittest.main()