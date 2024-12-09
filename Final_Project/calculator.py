from typing import Dict

class Calculator:
    @staticmethod
    def calculate_total_with_quantity(order: Dict[str, int], menu: Dict[str, float]) -> float:
        total = 0.0
        for item, quantity in order.items():
            if item not in menu:
                raise ValueError(f"{item} is not on the menu.")
            total += menu[item] * quantity
        return total