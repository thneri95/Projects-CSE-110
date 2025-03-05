"""
PC103_CSE110 
W05 Project: Shopping Cart - Final  
Author: Tiago Borges 

"""

# Shopping Cart Program (Final Version)
# In addition to the basic functionality (add, view, quit), I have added:
# - Storing both item names and prices.
# - Displaying prices next to item names with currency formatting.
# - Showing the total price of all items.
# - Ability to remove items by selecting their position in the list.

# Let's try to do that Work!

# Start of the program

print("Welcome to the Shopping Cart Program!")

# Lists to store item names and prices
cart_items = []
cart_prices = []

# Function to display the cart
def display_cart():
    if not cart_items:
        print("\nThe cart is empty.")
    else:
        print("\nThe contents of the shopping cart are:")
        for i in range(len(cart_items)):
            print(f"{i + 1}. {cart_items[i]} - ${cart_prices[i]:.2f}")

# Loop to keep the menu running
while True:
    print("\nPlease select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    choice = input("Please enter an action: ")

    if choice == "1":  # Add item
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? $"))
        cart_items.append(item)
        cart_prices.append(price)
        print(f"'{item}' has been added to the cart.")

    elif choice == "2":  # View cart
        display_cart()

    elif choice == "3":  # Remove item
        display_cart()
        if cart_items:
            try:
                item_number = int(input("Which item would you like to remove? "))
                # Convert to 0-based index
                if 1 <= item_number <= len(cart_items):
                    removed_item = cart_items.pop(item_number - 1)
                    removed_price = cart_prices.pop(item_number - 1)
                    print(f"'{removed_item}' has been removed from the cart.")
                else:
                    print("Sorry, that is not a valid item number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("There are no items to remove.")

    elif choice == "4":  # Compute total
        total = sum(cart_prices)
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

    elif choice == "5":  # Quit
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid choice. Please select a valid option.")

# This project has been a great opportunity to improve my Python skills. 
# I've learned how to manage lists, handle user input, and work with data to create a 
# functional shopping cart application. It’s been a valuable learning experience
# and I appreciate the chance to apply these concepts in a real-world project.

# Thank you to the evaluators for your time and feedback. 
# Your support has been invaluable in helping me grow my skills! 
# May Heavenly Father bless you!
 
