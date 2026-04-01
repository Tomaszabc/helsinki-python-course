# Write your solution here
# Write your solution here
from random import choice, randint, shuffle
from string import ascii_lowercase, digits

def generate_strong_password(length: int, include_numbers: bool, include_special: bool):
    lowercase = ascii_lowercase
    numbers = digits
    special = "!?=+-()#"   

    characters = lowercase
    if include_numbers:
        characters += numbers
    if include_special:
        characters += special

    password = []

    password.append(choice(lowercase))

    if include_numbers:
        password.append(choice(numbers))
    if include_special:
        password.append(choice(special))

    while len(password) < length:
        password.append(choice(characters))

        shuffle(password)
    
    return "".join(password)