from ui import RestaurantUI

def main():
    """
    Main function to run the Restaurant Cash Register application.
    """
    ui = RestaurantUI()
    while True:
        # Display the main menu
        print("\n--- Restaurant Cash Register ---")
        print("1. Add Menu Item")
        print("2. Show Menu")
        print("3. Calculate Order")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            ui.add_menu_item()  # Add a new item to the menu
        elif choice == "2":
            ui.display_menu()  # Display the current menu
        elif choice == "3":
            ui.calculate_order()  # Place an order and calculate the total
        elif choice == "4":
            print("Exiting. Thank you!")  # Exit the application
            break
        else:
            print("Invalid choice. Try again.")  # Handle invalid menu choices

if __name__ == "__main__":
    main()