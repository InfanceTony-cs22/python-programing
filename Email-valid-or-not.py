import re

def is_valid_email(email):
    # Define a regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

# Input an email address for validation
email = input("Enter an email address: ")

if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
