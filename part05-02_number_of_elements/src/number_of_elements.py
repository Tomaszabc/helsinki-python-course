# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    how_many = 0
    for i in range(len(my_matrix)):
        for j in my_matrix[i]:
            if element == j:
                how_many += 1
    return how_many

def count_matching_elements(my_matrix: list, element: int):
    n = 0
    for row in my_matrix:
        for cell in row:
            if cell == element
            n + = 1
    return n




if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))

