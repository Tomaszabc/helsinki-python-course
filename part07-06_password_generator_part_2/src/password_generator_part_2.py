from random import choice, randint
from string import ascii_lowercase, digits
 
def generate_strong_password(length: int, numbers: bool, special_characters: bool):
    special_chars = "!?=+-()#"
    # One letter at beginning of the password
    passwd = choice(ascii_lowercase)
    choice_set = ascii_lowercase
 
    # If numbers is wanted, add at least one number
    if numbers:
        passwd = add_character(passwd, digits)
        choice_set += digits
 
    # same for special characters
    if special_characters:
        passwd = add_character(passwd, special_chars)
        choice_set += special_chars
 
    # build the rest of the password from the whole set
    while (len(passwd) < length):
        passwd = add_character(passwd, choice_set)
 
    return passwd
 
# Add a random character from the given set either
# at the beginning or end of the string
def add_character(passwd: str, characters):
    character = choice(characters)
    if randint(1,2) == 1:
        return character + passwd
    else:
        return passwd + character
 
# Write your solution here
for i in range(10):
    print(generate_strong_password(8, True, True))




# # Write your solution here
# from random import choice, randint, shuffle
# from string import ascii_lowercase, digits

# def generate_strong_password(length: int, include_numbers: bool, include_special: bool):
#     lowercase = ascii_lowercase
#     numbers = digits
#     special = "!?=+-()#"   

#     characters = lowercase
#     if include_numbers:
#         characters += numbers
#     if include_special:
#         characters += special

#     password = []

#     password.append(choice(lowercase))

#     if include_numbers:
#         password.append(choice(numbers))
#     if include_special:
#         password.append(choice(special))

#     while len(password) < length:
#         password.append(choice(characters))

#         shuffle(password)
    
#     return "".join(password)