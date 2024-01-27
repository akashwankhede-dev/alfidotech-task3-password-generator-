import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not any([uppercase, lowercase, digits, special_chars]):
        return "Error: At least one character type must be selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


length = int(input("Enter the desired password length: "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'


password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special_chars)


print(f"Generated Password: {password}")
