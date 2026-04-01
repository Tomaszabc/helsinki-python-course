# Write your solution here
from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = []
    while len(numbers) < amount:
        number = randint(lower, upper)
        if number not in numbers:
            numbers.append(number)

    return sorted(numbers)

# def lottery_numbers(amount: int, lower: int, upper:int):
#     random_list = []
#     while True:
#         random_number = randint(lower, upper)
#         if random_number not in random_list:
#             random_list.append(random_number)

#         if  len(random_list) == amount:
#             break
#     random_list.sort()
#     return random_list

# for number in lottery_numbers(7, 1, 40):
#     print(number)