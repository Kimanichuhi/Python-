# prompt the user for the price of the meal and the tip percentage
meal_price = float(input("Enter the price of the meal: Ksh"))
tip_percentage = float(input("Enter the tip percentage you want to leave: "))

# Calculate the tip amount and total bill with tip
tip_amount = meal_price * (tip_percentage / 100)
total_bill = meal_price + tip_amount

# Print the tip amount and total bill with tip included
print("Tip Amount: Ksh", tip_amount)
print("Total Bill with Tip: Ksh", total_bill)
