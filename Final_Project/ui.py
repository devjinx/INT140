from menu import Menu
from calculator import Calculator

class RestaurantUI:
    def __init__(self):
        self.menu = Menu()

    def display_menu(self):
        items = self.menu.get_menu()
        if not items:
            print("No items in the menu.")
            return
        print("\n--- Menu ---")
        for index, (name, price) in enumerate(items.items(), start=1):
            print(f"{index}. {name}: {price:.2f} BATH")

    def add_menu_item(self):
        name = input("Enter the name of the menu item: ")
        try:
            price = float(input(f"Enter the price of {name}: "))
            self.menu.add_menu_item(name, price)
            print(f"{name} added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def calculate_order(self):
        self.display_menu()

        print("\nEnter the quantities for the items by their numbers:")
        items = list(self.menu.get_menu().items())
        order = {}

        for index, (item_name, price) in enumerate(items, start=1):
            try:
                quantity = int(input(f"Quantity for {index}. {item_name}: "))
                if quantity > 0:
                    order[item_name] = quantity
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        try:
            total = Calculator.calculate_total_with_quantity(order, self.menu.get_menu())
            print(f"Total cost: {total:.2f} BATH")
        except ValueError as e:
            print(f"Error: {e}")