# Write your solution here
def new_person(name: str, age: int):
    if name == "" or (" " not in name) or len(name) > 40:
        raise ValueError("Invalid argument value for name: " + name)
    
    if age < 0 or age > 150:
        raise ValueError("Invalid argiment value for age:" + str(age))

    return (name, age)
    
# def new_person(name: str, age: int):
#     created_tuple = name, age

#     if len(name) == 0 or len(name) > 40:
#         raise ValueError("Name cannot be empty")
#     if len(name) > 40:
#         raise ValueError("Name should be not longer than 40")
#     if len(name.split()) < 2:
#         raise ValueError("Name must contain at least two words")
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     if age > 150:
#         raise ValueError("Age cannot be greater than 150")

#     created_tuple = (name, age)
#     return created_tuple

