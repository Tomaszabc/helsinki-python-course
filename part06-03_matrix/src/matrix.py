def read_matrix():
    matrix = []
    with open("matrix.txt") as file:  # ZMIANA TUTAJ
        for line in file:
            line = line.strip()  # użyj strip zamiast replace!
            numbers = line.split(",")
            
            row = []
            for number in numbers:
                row.append(int(number))
            
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
    maximum = matrix[0][0]
    for row in matrix:
        for number in row:
            if number > maximum:
                maximum = number
    return maximum

def row_sums():
    matrix = read_matrix()
    sums_list = []
    for row in matrix:
        sums_list.append(sum(row))
    return sums_list

read_matrix()