import unittest
from Final_Project.test.test_menu import Menu

class TestMenu(unittest.TestCase):
    def test_add_menu_item(self):
        menu = Menu()
        menu.add_menu_item("Burger", 5.99)
        self.assertEqual(menu.get_menu(), {"Burger": 5.99})

    def test_add_duplicate_item(self):
        menu = Menu()
        menu.add_menu_item("Burger", 5.99)
        with self.assertRaises(ValueError):
            menu.add_menu_item("Burger", 6.99)