# write your solution here
def largest():
    with open("numbers.txt") as text_file:
        largest = 0
        for i in text_file:
            if int(i) > largest:
                largest = int(i)
    return largest

if __name__ == "__main__":  
    largest()