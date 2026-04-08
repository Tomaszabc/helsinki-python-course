# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()
        students = json.loads(data)

        for student in students:
            name = student["name"]
            age = student["age"]
            hobbies = student["hobbies"]

            hobbies_str = ", ".join(hobbies)
            print(f"{name} {age} years ({hobbies_str})")
