# Write your solution here
from random import choice
from string import ascii_lowercase

def generate_password(length: int):
    passwd = ""
    for i in range(length):
        passwd += choice(ascii_lowercase)
    
    return passwd

# from random import randint
# import string

# def generate_password(length: int):
#     password = []
#     while len(password) < length:
#         random_index = randint(0,len(string.ascii_lowercase) - 1)
#         password.append(string.ascii_lowercase[random_index])
#     return "".join(password)

# for i in range(10):
#     print(generate_password(8))