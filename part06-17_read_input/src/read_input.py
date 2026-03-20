# Write your solution here
def read_input(prompt, lower_bound, upper_bound):
    while True:
        try:
            number = int(input(prompt))
            if lower_bound <= number <= upper_bound:
                return number
            else:
                 print(f"You must type in an integer between {lower_bound} and {upper_bound}")
        except ValueError:
            print(f"You must type in an integer between {lower_bound} and {upper_bound}")
  

# number = read_input("Please type in a number: ", 5, 10)
# print("You typed in:", number)