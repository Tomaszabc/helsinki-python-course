# Write your solution here
times_eat = int(input("How many times a week do you eat at the student cafeteria?"))
typical_price = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week?"))
weekly = (times_eat * typical_price) + groceries

print("Average food expenditure:")
print(f"Daily: {weekly/7} euros")
print(f"Weekly: {weekly} euros")