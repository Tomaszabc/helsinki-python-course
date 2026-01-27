# Write your solution here
wage = float(input("wage"))
hours = int(input("hours"))
day = input("day")
if day == "Sunday":
    wage *= 2
total_wage = wage * hours
print(f"Daily wages: {total_wage} euros")

