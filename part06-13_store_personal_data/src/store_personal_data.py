# Write your solution here
def store_personal_data(person: tuple):
    name = person[0]
    age = person[1]
    height = person[2]

    with open("people.csv", "a") as file:
        file.write(f"{name};{age};{height}")