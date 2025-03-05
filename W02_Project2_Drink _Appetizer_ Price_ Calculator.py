""" 
Author: Tiago Borges

W02 Project: Drink & Appetizer Price Calculator

"""

# That's a Drink and Appetizer Price Calculator with Tip Feature
# This program calculates the total cost of a meal including drinks, appetizers, tax, and change after payment.
# Added Feature: Prompt the user to optionally include a tip percentage in the final total.

def main():
    # Ask for prices of drinks and appetizers
    drink_price = float(input("What is the price of a drink? "))
    appetizer_price = float(input("What is the price of an appetizer? "))

    # Ask for the quantity of drinks and appetizers
    num_drinks = int(input("How many drinks are there? "))
    num_appetizers = int(input("How many appetizers are there? "))

    # Compute and display the subtotal
    subtotal = (drink_price * num_drinks) + (appetizer_price * num_appetizers)
    print(f"\nSubtotal: ${subtotal:.2f}")

    # Ask for the sales tax rate
    tax_rate = float(input("\nWhat is the sales tax rate? "))
    
    # Compute and display the sales tax
    sales_tax = (subtotal * tax_rate) / 100
    print(f"Sales Tax: ${sales_tax:.2f}")

    # Compute and display the total price
    total = subtotal + sales_tax
    print(f"Total: ${total:.2f}")

    # Added Feature: Ask for optional tip percentage
    tip_percentage = float(input("\nWould you like to add a tip? Enter the percentage (10 for 10%, or 0 to skip): "))
    tip_amount = (subtotal * tip_percentage) / 100
    print(f"Tip: ${tip_amount:.2f}")

    # Final total including tip
    final_total = total + tip_amount
    print(f"Final Total (including tip): ${final_total:.2f}")

    # Ask for payment amount
    payment_amount = float(input("\nWhat is the payment amount? "))
    
    # Compute and display the change
    change = payment_amount - final_total
    print(f"Change: ${change:.2f}")

# Run the program
if __name__ == "__main__":
    main()