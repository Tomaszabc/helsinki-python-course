# Write your solution here


def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        if i % 3 == 0 and 1 != 0:
            print()
        for j in range(len(sudoku[i])):
            if j % 3 == 0 and j != 0:
                print(" ", end="")

            if sudoku[i][j] == 0:
                print("_ ", end="")
            else:
                print(f"{sudoku[i][j]} ", end="")
        print()



if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)