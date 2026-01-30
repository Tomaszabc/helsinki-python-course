def read_matrix():
    matrix = []
    with open("matrix.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            numbers = line.split(",")
            
            # Tworzymy wiersz (listę liczb)
            row = []
            for number in numbers:
                row.append(int(number))  # dodajemy liczbę do wiersza
            
            # Dodajemy CAŁY wiersz do macierzy
            matrix.append(row)
            
    return matrix


def matrix_sum():
    matrix = read_matrix()
    total = 0
    for row in matrix:
        for number in row:
            total += number
    print(total)
    return total


def matrix_max():
    matrix = read_matrix()
    start = True
    maximum = 0
    for row in matrix:
        for number in row:
            if start or number > maximum:
                maximum = number
    print(number)


read_matrix()
matrix_sum()
matrix_max()