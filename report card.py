def apply_discount(price, discount):
    # 3. Check if price is a number
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    
    # 4. Check if discount is a number
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    
    # 5. Check if price is greater than 0
    if price <= 0:
        return "The price should be greater than 0"
    
    # 6. Check if discount is between 0 and 100
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    # Calculation: price - (price * discount / 100)
    result = price * (1 - discount / 100)
    
    # Return result (Rules 7-11)
    return result

# --- Section to ask for User Input ---

try:
    # We use input() to get values from the user
    user_price = input("Enter the price: ")
    user_discount = input("Enter the discount percentage: ")

    # Try to convert inputs to floats for the function to process
    # If the user enters text, the function's logic will handle it 
    # but we'll try to convert valid numbers first.
    try:
        a = float(user_price)
    except ValueError:
        a = user_price # Keep as string to trigger the function's error message

    try:
        d = float(user_discount)
    except ValueError:
        d = user_discount

    # Call the function and print the result
    print(apply_discount(a, d))

except Exception as e:
    print(f"An unexpected error occurred: {e}")
