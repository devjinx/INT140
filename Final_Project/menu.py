from typing import Dict

class Menu:
    def __init__(self):
        # Dictionary to store menu items and their prices
        self.items: Dict[str, float] = {}

    def add_menu_item(self, name: str, price: float) -> None:
        """
        Add a new item to the menu.

        Args:
            name (str): The name of the menu item.
            price (float): The price of the menu item.

        Raises:
            ValueError: If the item already exists in the menu.
        """
        if name in self.items:
            raise ValueError("Item already exists!")
        self.items[name] = price  # Add the item to the menu

    def get_menu(self) -> Dict[str, float]:
        """
        Get the current menu.

        Returns:
            Dict[str, float]: A dictionary of menu items and their prices.
        """
        return self.items
