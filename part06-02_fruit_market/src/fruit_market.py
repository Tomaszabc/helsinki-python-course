# write your solution here
def read_fruits():
    with open("fruits.csv") as fruits_file:
        dictionary = {}
        for line in fruits_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruit = parts[0]
            price = float(parts[1])
            dictionary[fruit] = price
    return dictionary


if __name__ == "__main__":
    read_fruits()
# banana;6.50
# apple;4.95
# orange;8.0