# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    return [Fraction(1, amount) for _ in range(amount)]




# from fractions import Fraction

# def fractionate(amount: int):
#     fractions_list = []

#     for i in range(amount):
#         fractions_list.append(Fraction(1, amount))

#     return fractions_list
