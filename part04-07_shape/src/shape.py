# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(length, character):
    if character == "":
        character = "*"

    print(length * character[0])


def shape(length1, character1, length2, character2):
    i = 1
    while length1 >= i:
        line(i, character1)
        i += 1
    i = 1
    while length2 >= i:
        line(length1, character2)
        i += 1
if __name__ == "__main__":
    shape(5, "x", 2, "o")