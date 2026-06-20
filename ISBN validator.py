import sys

def calculate_check_digit_10(isbn):
    """Calculates the check digit for a 10-digit ISBN."""
    total = 0
    for i in range(9):
        total += int(isbn[i]) * (10 - i)
    
    remainder = total % 11
    check_digit = (11 - remainder) % 11
    return 'X' if check_digit == 10 else str(check_digit)

def calculate_check_digit_13(isbn):
    """Calculates the check digit for a 13-digit ISBN."""
    total = 0
    for i in range(12):
        if i % 2 == 0:
            total += int(isbn[i]) * 1
        else:
            total += int(isbn[i]) * 3
    
    remainder = total % 10
    check_digit = (10 - remainder) % 10
    return str(check_digit)

def validate_isbn(isbn, length):
    """Validates the ISBN based on the specified length (10 or 13)."""
    # Rule 15: Check length validity
    if length not in [10, 13]:
        print("Length should be 10 or 13.")
        return

    # Rules 12 & 13: Check if input matches specified length
    if len(isbn) != length:
        print(f"ISBN-{length} code should be {length} digits long.")
        return

    # Rule 8 & 14: Check for invalid characters
    # ISBN-10 allows 'X' as the last character
    check_chars = isbn[:-1]
    last_char = isbn[-1]
    
    if not check_chars.isdigit() or (length == 13 and not last_char.isdigit()) or (length == 10 and not (last_char.isdigit() or last_char.upper() == 'X')):
        print("Invalid character was found.")
        return

    # Rules 9, 10, 11, 18, 19, 20: Validate check digit
    if length == 10:
        expected = calculate_check_digit_10(isbn)
        if last_char.upper() == expected:
            print("Valid ISBN Code.")
        else:
            print("Invalid ISBN Code.")
    else:
        expected = calculate_check_digit_13(isbn)
        if last_char == expected:
            print("Valid ISBN Code.")
        else:
            print("Invalid ISBN Code.")

def main():
    user_input = input("Enter ISBN and length (comma-separated): ")
    
    # Rules 6 & 17: Check for comma separation
    if ',' not in user_input:
        print("Enter comma-separated values.")
        return

    parts = user_input.split(',')
    isbn_str = parts[0].strip()
    length_str = parts[1].strip()

    # Rules 7 & 16: Check if length is a number
    try:
        length = int(length_str)
    except ValueError:
        print("Length must be a number.")
        return

    validate_isbn(isbn_str, length)

# Rule 1: Comment out the main function call for tests
# if __name__ == "__main__":

#main()



