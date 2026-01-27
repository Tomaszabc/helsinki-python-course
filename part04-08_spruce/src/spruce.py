# Write your solution here
# You can test your function by calling it within the following block

def spruce(size):
    print("a spruce!")
    i = 1
    position = size
    size = int(size)

    while i <= size*2-1:
        print(" " * ((size*2-1 - i)//2) + "*" * i)
        i += 2
       
    
    
    print(" " * ((size*2-1 - 1)//2) + "*" )
        

if __name__ == "__main__":
    spruce(5)