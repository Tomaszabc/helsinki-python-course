# Write your solution here
import string


def separate_characters(my_string: str):
    letters = ""
    punctuation = ""
    other = ""

    for char in my_string:
        if char in string.ascii_letters:
            letters += char
        elif char in string.punctuation:
            punctuation += char
        else:
            other += char
    return (letters, punctuation, other)

