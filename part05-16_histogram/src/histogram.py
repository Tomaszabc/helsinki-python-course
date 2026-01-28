# Write your solution here
def histogram(string):
    number_letters = {}
    for letter in string:
        if letter not in number_letters:
            number_letters[letter] = 0
        number_letters[letter] += 1
    for key, value in number_letters.items():
        print(f"{key} {value*"*"}")


if __name__ == "__main__":
    string = "abba"
    print(histogram(string))