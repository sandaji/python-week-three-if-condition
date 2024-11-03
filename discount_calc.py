def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Prompt the user to enter the original price of an item
price = float(input("Enter the original price of the item: "))

# Prompt the user to enter the discount percentage
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(price, discount_percent)

# Print the final price after applying the discount, or the original price if no discount was applied
if discount_percent >= 20:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {price}")
