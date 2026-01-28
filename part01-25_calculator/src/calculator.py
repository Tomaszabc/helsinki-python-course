# Write your solution here
number1 = int(input("Number1"))
number2 = int(input("Number2"))
operation = input("operation")

if operation == "add":
    print(str(number1) + " + " + str(number2) + " = " + str(number1 + number2))
if operation == "multiply":
    print(str(number1) + " * " + str(number2) + " = " + str(number1 * number2))
if operation == "subtract":
    print(str(number1) + " - " + str(number2) + " = " + str(number1 - number2))