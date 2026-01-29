letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']

layers = int(input("Layers: "))

square = [["A"]]

for layer in range(2, layers + 1):
    current_letter = letters[layer-1]

    old_size = len(square)
    new_size = old_size + 2

    new_square = []
    new_square.append([current_letter]* new_size)

    for row in square:
        new_row = [current_letter] + row + [current_letter]
        new_square.append(new_row)
    
    new_square.append([current_letter]* new_size)

    square = new_square
    
for row in square:
    print("".join(row))

# if __name__ == "__main__":
#     letter_square(5)

# This final exercise in this part is a relatively 
# demanding problem solving task. It can be
#  solved in many different ways. Even though 
#  this current section in the material covers tuples, 
#  tuples are not necessarily the best way to go about solving this.

# Please write a program which prints out a square 
# of letters as specified in the examples below. You may assume there will be at most 26 layers.

# Sample output
# Layers: 3

# CCCCC
# CBBBC
# CBABC
# CBBBC
# CCCCC
# Sample output
# Layers: 4

# DDDDDDD
# DCCCCCD
# DCBBBCD
# DCBABCD
# DCBBBCD
# DCCCCCD
# DDDDDDD
# NB: this exercise 
# doesn't ask you to write any functions, 
# so you should not place any code within an if __name__ == "__main__" block.