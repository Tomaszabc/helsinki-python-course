# Copy here code of line function from previous exercise

def line(length, character):
    if character == "":
        character = "*"

    print(length * character[0])

def box_of_hashes(height):
    # You should call function line here with proper parameters
    i = 0
    while i < height:

        line(10, "#")
        height -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
