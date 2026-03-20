# Write your solution here
def read_input(prompt: str, lower_limit: int, upper_limit: int):
    while True:
        error = False
        try:
            number = int(input(prompt))
            if number < lower_limit or number > upper_limit:
                error = True
        except:
            error = True
        if error:
            print(f"You must type in an integer between {lower_limit} and {upper_limit}")
        else:
            return number

# def read_input(prompt, lower_bound, upper_bound):
#     while True:
#         try:
#             number = int(input(prompt))
#             if lower_bound <= number <= upper_bound:
#                 return number
#             else:
#                  print(f"You must type in an integer between {lower_bound} and {upper_bound}")
#         except ValueError:
#             print(f"You must type in an integer between {lower_bound} and {upper_bound}")
  

# number = read_input("Please type in a number: ", 5, 10)
# print("You typed in:", number)