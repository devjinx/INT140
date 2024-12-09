from ui import RestaurantUI

def main():
    ui = RestaurantUI()
    while True:
        print("\n--- Restaurant Cash Register ---")
        print("1. Add Menu Item")
        print("2. Show Menu")
        print("3. Calculate Order")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            ui.add_menu_item()
        elif choice == "2":
            ui.display_menu()
        elif choice == "3":
            ui.calculate_order()
        elif choice == "4":
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
