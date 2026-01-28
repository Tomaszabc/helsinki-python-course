# Write your solution here

def line(length, character):
    if character == "":
        character = "*"

    print(length * character[0])

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")
