"""
Password Generator

Generates secure customizable passwords
based on user-selected criteria.
"""

import random
import string


# Collect and validate user password preferences
def get_user_preferences():
    
    # Keep asking until valid password length is entered
    while True:
    
        try:
    
            length = int(input("Enter the desired password length (8-128): "))
    
            if length < 8 or length > 128:
    
                print("Please enter a number between 8 and 128.")
    
                continue
    
            break
    
        except ValueError:
    
            print("Invalid input. Please enter a number.")
    

    # Convert y/n input into Boolean values
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    
    include_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    return length, include_uppercase, include_lowercase, include_digits, include_special


# Generate password based on selected character types
def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):

    characters = ""

    # Store password characters before shuffling
    password = []
    
    # Guarantee at least one selected character type is included in the password
    if include_uppercase:
    
        characters += string.ascii_uppercase
    
        password.append(random.choice(string.ascii_uppercase))

    if include_lowercase:
    
        characters += string.ascii_lowercase

        password.append(random.choice(string.ascii_lowercase))
    
    if include_digits:
    
        characters += string.digits

        password.append(random.choice(string.digits))
    
    if include_special:
    
        characters += string.punctuation

        password.append(random.choice(string.punctuation))
    
    # Prevent empty character pool
    if not characters:
    
        raise ValueError("At least one character type must be selected.")
    
    # Fill remaining password length with random characters
    while len(password) < length:
    
        password.append(random.choice(characters))
    
    # Randomize character order
    random.shuffle(password)
 
    return ''.join(password)

# Main program loop
def main():

    print("Welcome to the Password Generator!")

    while True:
    
        length, include_uppercase, include_lowercase, include_digits, include_special = get_user_preferences()
    
        try:
    
            password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
    
            print(f"Generated Password: {password}")
            
            # Allow user to generate multiple passwords in one session
            again = input("Generate another password? (y/n): ").lower()

            if again != 'y':
    
                print("Thank you for using the Password Generator. Goodbye!")
    
                break
    
        except ValueError as e:
    
            print(e)

# Run program directly
if __name__ == "__main__":
    main()


