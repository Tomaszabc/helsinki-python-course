# Write your solution here
def change_case(orig_string: str):
    result = ""
    for char in orig_string:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
    return result

def split_in_half(orig_string: str):
    length = len(orig_string)
    half = length // 2
    return (orig_string[:half], orig_string[half:])

def remove_special_characters(orig_string: str):
    result = ""
    for char in orig_string:
        if char.isalnum() or char.isspace():
            result += char
    return result