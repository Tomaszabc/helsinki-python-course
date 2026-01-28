# Write your solution here
def transpose(matrix: list):
    n = len(matrix)

    for x in range(n):
        for y in range(x, n):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][x]
            matrix[y][x] = temp



if __name__ == "__main__":

    matrix = [[1, 2], [1, 2]]
    transpose(matrix)
    print(matrix)