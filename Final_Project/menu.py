from typing import Dict

class Menu:
    def __init__(self):
        self.items: Dict[str, float] = {}

    def add_menu_item(self, name: str, price: float) -> None:
        if name in self.items:
            raise ValueError("Item already exists!")
        self.items[name] = price

    def get_menu(self) -> Dict[str, float]:
        return self.items