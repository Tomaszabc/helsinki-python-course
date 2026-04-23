# Write your solution here
def row_sums(my_matrix: list):
    for row in my_matrix:
        row_sum = sum(row)
        row.append(row_sum)

if __name__ == "__main__":
    # Test 1: Podstawowy
    matrix1 = [[1, 2], [3, 4]]
    row_sums(matrix1)
    print(matrix1)  # [[1, 2, 3], [3, 4, 7]]
    
    # Test 2: Macierz 3x3
    matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    row_sums(matrix2)
    print(matrix2)  # [[1, 2, 3, 6], [4, 5, 6, 15], [7, 8, 9, 24]]
    
    # Test 3: Pojedynczy element
    matrix3 = [[5]]
    row_sums(matrix3)
    print(matrix3)  # [[5, 5]]
    
    # Test 4: Pusta macierz
    matrix4 = []
    row_sums(matrix4)
    print(matrix4)  # []
    
    # Test 5: Liczby ujemne
    matrix5 = [[-1, -2], [-3, -4]]
    row_sums(matrix5)
    print(matrix5)  # [[-1, -2, -3], [-3, -4, -7]]