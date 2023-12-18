import string
import random

def generate_password():
    length = 0
    while length < 5:
        length = int(input("Enter the desired length of the password: "))
        if length < 5:
            print("Password length should be at least 5. Please try again.")

    # Define the character sets, excluding certain characters
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = "!@#$&"  # Include any other punctuation characters you want

    all_character_sets = [lowercase, uppercase, digits, punctuation]
    password = []

    # Ensure at least one character from each category
    for character_set in all_character_sets:
        password.extend(random.sample(character_set, 1))

    # Fill the rest of the password length with random characters from all categories
    all_characters = ''.join(all_character_sets)
    for i in range(length - len(password)):
        password.append(random.choice(all_characters))

    # Shuffle the list of characters
    random.shuffle(password)

    # Convert the list of characters into a string
    password = ''.join(password)

    return password

# Test the function
while True:
    password = generate_password()
    print(password)
    print("Please save this password. It will not be shown again.")
    another = input("Do you want to generate another password? (y/n): ")
    if another.lower() != "y":
        break
