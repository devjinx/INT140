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
        name = input("Enter the name of the menu item: ").strip()
        try:
            price = float(input(f"Enter the price of {name}: "))
            if price <= 0:
                print("Price must be a positive number.")
                return
            self.menu.add_menu_item(name, price)
            print(f"{name} added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def calculate_order(self):
        self.display_menu()
        items = list(self.menu.get_menu().items())
        order = {}

        if not items:
            print("No items available to order.")
            return

        print("\nChoose your menu:")
        while True:
            try:
                choice = int(input("Enter the number of the item (0 = finish): "))
                if choice == 0:
                    break
                elif 1 <= choice <= len(items):
                    item_name = items[choice - 1][0]
                    quantity = int(input(f"Quantity for {item_name}: "))
                    if quantity > 0:
                        if item_name in order:
                            order[item_name] += quantity
                        else:
                            order[item_name] = quantity
                        print("\n--- Updated Order Summary ---")
                        for order_item, order_quantity in order.items():
                            print(f"{order_item}: {order_quantity} pcs")
                    else:
                        print("Quantity must be a positive number.")
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Final order summary
        if order:
            print("\n--- Final Order Summary ---")
            for item, quantity in order.items():
                print(f"{item}: {quantity} pcs")

            try:
                total = Calculator.calculate_total_with_quantity(order, self.menu.get_menu())
                print(f"Total cost: {total:.2f} BATH")
            except ValueError as e:
                print(f"Error: {e}")