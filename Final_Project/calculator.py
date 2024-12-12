from typing import Dict

class Calculator:
    @staticmethod
    def calculate_total_with_quantity(order: Dict[str, int], menu: Dict[str, float]) -> float:
        """
        Calculate the total cost of an order based on the quantity of each item and their prices.

        Args:
            order (Dict[str, int]): A dictionary where the key is the item name and the value is the quantity ordered.
            menu (Dict[str, float]): A dictionary where the key is the item name and the value is its price.

        Returns:
            float: The total cost of the order.

        Raises:
            ValueError: If an item in the order is not found in the menu.
        """
        total = 0.0
        # Loop through the items in the order
        for item, quantity in order.items():
            # Check if the item exists in the menu
            if item not in menu:
                raise ValueError(f"{item} is not on the menu.")
            # Add the item's total cost (price * quantity) to the total
            total += menu[item] * quantity
        return total
