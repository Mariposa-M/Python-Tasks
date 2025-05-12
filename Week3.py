# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price:float, discount_percent:float) -> float:
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): original price
        discount_percent (float): percent provided 

    Returns:
        float: price after discount if applicable
    """
    if discount_percent >= 20:
        return price * discount_percent / 100
    else:
        return price

# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
user_input = input("Please enter the original price: ")
discount_provided = input("Discount percent value: ")

print("Price After discount if applicable is: ")
print(calculate_discount(float(user_input), float(discount_provided)))
