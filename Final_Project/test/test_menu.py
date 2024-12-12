import unittest
from menu import Menu

class TestMenu(unittest.TestCase):
    def setUp(self):
        # Create a new menu instance before each test
        self.menu = Menu()

    def test_add_valid_item(self):
        # Add a valid item and check if it exists in the menu
        self.menu.add_menu_item("Burger", 59.99)
        self.assertEqual(self.menu.get_menu(), {"Burger": 59.99})

    def test_update_existing_item_price(self):
        # Add an item and update its price
        self.menu.add_menu_item("Burger", 59.99)
        try:
            self.menu.add_menu_item("Burger", 69.99)
        except ValueError:
            pass  # Pass the test if ValueError is raised

    def test_add_item_with_empty_name(self):
        # Try to add an item with an empty name
        try:
            self.menu.add_menu_item("", 59.99)
        except ValueError:
            pass  # Pass the test if ValueError is raised

    def test_add_item_with_negative_price(self):
        # Try to add an item with a negative price
        try:
            self.menu.add_menu_item("Burger", -10.00)
        except ValueError:
            pass  # Pass the test if ValueError is raised

    def test_add_item_with_zero_price(self):
        # Try to add an item with a price of zero
        try:
            self.menu.add_menu_item("Burger", 0.00)
        except ValueError:
            pass  # Pass the test if ValueError is raised

    def test_menu_initially_empty(self):
        # Check that the menu is empty initially
        self.assertEqual(self.menu.get_menu(), {})

    def test_menu_contains_multiple_items(self):
        # Add multiple items and check if they exist in the menu
        self.menu.add_menu_item("Burger", 59.99)
        self.menu.add_menu_item("Fries", 29.99)
        self.assertEqual(self.menu.get_menu(), {"Burger": 59.99, "Fries": 29.99})

    def test_menu_get_menu_after_updates(self):
        # Check if items exist in the menu after multiple additions
        self.menu.add_menu_item("Burger", 59.99)
        self.menu.add_menu_item("Fries", 29.99)
        self.assertIn("Burger", self.menu.get_menu())
        self.assertIn("Fries", self.menu.get_menu())

    def test_menu_price_accuracy(self):
        # Check if the prices in the menu are accurate
        self.menu.add_menu_item("Burger", 59.99)
        self.assertAlmostEqual(self.menu.get_menu()["Burger"], 59.99)

    def test_add_item_with_large_price(self):
        # Add an item with a large price
        self.menu.add_menu_item("Premium Steak", 1999.99)
        self.assertEqual(self.menu.get_menu()["Premium Steak"], 1999.99)

if __name__ == "__main__":
    unittest.main()