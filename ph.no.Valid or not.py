import re

def is_valid_indian_phone_number(phone_number):
    # Define a regular expression pattern for an Indian phone number
    pattern = r'^[6-9]\d{9}$'
    
    # Use the re.match() function to check if the input matches the pattern
    if re.match(pattern, phone_number):
        return True
    else:
        return False

# Input a phone number for validation
phone_number = input("Enter an Indian phone number (10 digits starting with 6 or 9): ")

# Check if the phone number is valid
if is_valid_indian_phone_number(phone_number):
    print("Valid Indian phone number")
else:
    print("Invalid Indian phone number")
