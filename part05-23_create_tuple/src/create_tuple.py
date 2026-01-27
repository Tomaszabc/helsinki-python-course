# Write your solution here
def create_tuple(x: int, y: int, z: int):
    smallest = min([x, y, z])
    greatest = max([x, y, z])
    sum = x + y + z
    return(smallest, greatest, sum)

# # 
# Please write a function named create_tuple(x: int, y: int, z: int),
#  which takes three integers as its arguments, and creates and 
#  returns a tuple based on the following criteria:

#     The first element in the tuple is the smallest of the arguments
#     The second element in the tuple is the greatest of the arguments
#     The third element in the tuple is the sum of the arguments

# An example of its use:


if __name__ == "__main__":
    print(create_tuple(1, 2, 3))

# Sample output

# (-1, 5, 7)