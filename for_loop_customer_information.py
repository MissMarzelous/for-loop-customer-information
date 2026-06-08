# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Customer Information — FOR Loop
# DATE WRITTEN: October 6, 2020
# UPDATED:      2026 — fixed PURPOSE comment (was "WHILE LOOP"), added input
#                      validation, renamed howMany → how_many, updated to f-strings
#
# PURPOSE: Demonstrate the FOR loop concept by processing customer names
#          and purchase amounts for a user-defined number of customers.
#
# KEY CONCEPT — FOR LOOP:
#   range(1, how_many + 1, 1) generates: 1, 2, 3, ... how_many
#   The loop runs exactly how_many times — no more, no less.
#
# Compare this to while_loop_customer_information.py which uses a
# WHILE loop (y/Y to continue) to process an unknown number of customers.

# ============================================================
# Declare / define variables and data types
# INPUT OPERATIONS — ask how many customers to process

# Loop until a valid positive integer is entered
while True:
    try:
        print("How many customers do you wish to process?")
        how_many = int(input())
        if how_many <= 0:
            print("Please enter a number greater than zero.")
        else:
            break  # Valid input received, exit loop
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# ============================================================
# FOR LOOP — process each customer one at a time
# range(start, stop, step): starts at 1, goes up to how_many (inclusive), step of 1

for count in range(1, how_many + 1, 1):
    # Input customer name
    print(f"Enter Customer #{count}'s name:")
    customer_name = input()

    # Input purchase amount with validation
    while True:
        try:
            print(f"How much did {customer_name} spend on this item?")
            purchase_amount = float(input())
            break  # Exit loop once valid number is entered
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Output customer purchase summary
    print("====================================================================================================")
    print(f"{customer_name} spent ${format(purchase_amount, ',.2f')} on the item.")
    print("====================================================================================================")

# Display completion message when all customers have been processed
print("THIS PROGRAM IS COMPLETE — Fabrick, Marlena")

# END PROGRAM
