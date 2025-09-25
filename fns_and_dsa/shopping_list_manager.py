# shopping_list_manager.py

def display_menu():
    """Displays the main menu options to the user."""
    print("\nShopping List Manager")  # Required menu title
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    # Start with an empty shopping list
    shopping_list = []

    while True:
        # Call the display_menu function
        display_menu()

        # Get user choice and ensure it's a number
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            # Add an item to the shopping list
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")

        elif choice == '2':
            # Remove an item from the shopping list
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in your shopping list.")

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nYour Shopping List:")
                for idx, list_item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {list_item}")
            else:
                print("Your shopping list is currently empty.")

        elif choice == '4':
            # Exit the program
            print("Goodbye! Thanks for using the Shopping List Manager.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Run the main function only when the script is executed directly
if __name__ == "__main__":
    main()
