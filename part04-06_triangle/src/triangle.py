# Copy here code of line function from previous exercise
def line(length, character):
    if character == "":
        character = "*"

    print(length * character[0])

def triangle(size):
    i = 0
    while i < size:
    # You should call function line here with proper parameters
        i += 1
        line(i, "#")
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
