# Write your solution here
name_input = input("Whom should I sign this to: ")
filename_input = input("Where shall I save it: ")

with open(filename_input, "w") as my_file:
    my_file.write(f"Hi {name_input}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

