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

        items = list(self.menu.get_menu().items())
        order = {}

        if items == []:
            return
        print("\nChoose your menu")


        while True:

            try:
                choice = int(input(f"Enter number of item (0 = finish):"))   


                if choice == 0:
                    break
                elif 1<= choice <= len(self.menu.get_menu()):
                    item_name = items[choice-1][0]
                    quantity = int(input(f"Quantity for {item_name} :"))

                    if quantity > 0:
                        if item_name in order:
                            order[item_name] += quantity
                        else:
                            order[item_name] = quantity
                        print(f'---add {quantity} {item_name} to order--- ')
                    else:
                        print("quantity must be positive number")

                else:
                    print("Invalid item number. Please try again.")

                    
            except ValueError:
                print("Invalid input. Please enter a number.")




        try:
            total = Calculator.calculate_total_with_quantity(order, self.menu.get_menu())
            print(f"Total cost: {total:.2f} BATH")
        except ValueError as e:
            print(f"Error: {e}")