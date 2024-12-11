import unittest
from menu import Menu

class TestMenu(unittest.TestCase):
    def test_add_menu_item(self):
        menu = Menu()
        menu.add_menu_item("Burger", 59.99)
        self.assertEqual(menu.get_menu(), {"Burger": 59.99})

    def test_add_duplicate_item(self):
        menu = Menu()
        menu.add_menu_item("Burger", 59.99)
        with self.assertRaises(ValueError):
            menu.add_menu_item("Burger", 69.99)