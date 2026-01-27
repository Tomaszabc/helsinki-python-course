# Write your solution here
# Write your solution here

def row_correct(sudoku: list, row_no: int) -> bool:
 
    # Pobierz wiersz do sprawdzenia
    row = sudoku[row_no]
    
    # Stwórz zbiór do śledzenia już napotkanych liczb
    seen = set()
    
    for num in row:
        # Pomiń zera (puste pola)
        if num == 0:
            continue
            
        # Sprawdź, czy liczba jest w zakresie 1-9
        if num < 1 or num > 9:
            return False
            
        # Sprawdź, czy liczba już wystąpiła
        if num in seen:
            return False
            
        # Dodaj liczbę do zbioru napotkanych
        seen.add(num)
    
    # Jeśli dotarliśmy tutaj, wiersz jest poprawny
    return True

def column_correct(sudoku: list, column_no: int) -> bool:

    # Stwórz zbiór do śledzenia już napotkanych liczb
    seen = set()
    
    # Iteruj przez wszystkie wiersze w danej kolumnie
    for row in sudoku:
        # Pobierz wartość z odpowiedniej kolumny
        num = row[column_no]
        
        # Pomiń zera (puste pola)
        if num == 0:
            continue
            
        # Sprawdź, czy liczba jest w zakresie 1-9
        if num < 1 or num > 9:
            return False
            
        # Sprawdź, czy liczba już wystąpiła
        if num in seen:
            return False
            
        # Dodaj liczbę do zbioru napotkanych
        seen.add(num)
    
    # Jeśli dotarliśmy tutaj, kolumna jest poprawna
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    check = []
    for row in range(row_no, row_no+3):
        for column in range(column_no, column_no+3):
            number = sudoku[row][column]
            if number == 0:
                continue
            
            if number in check:
                return False
            check.append(number)
            
    return True



def sudoku_grid_correct(sudoku: list):

    for row_no in range(0, 9):
        row = row_correct(sudoku, row_no)
        if row == False:
            return False
    for column_no in range(0, 9):
        column = column_correct(sudoku, column_no)
        if column == False:
            return False
    for row_no in range(0, 9, 3):
        for column_no in range(0, 9, 3):
            block = block_correct(sudoku, row_no, column_no)
            if not block_correct(sudoku, row_no, column_no):  # SPRAWDŹ!
                return False

    else:
        return True


if __name__ == "__main__":
    sudoku = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 6, 0, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]
    print(sudoku_grid_correct(sudoku))

    # sudoku2 = [
    # [2, 6, 7, 8, 3, 9, 5, 0, 4],
    # [9, 0, 3, 5, 1, 0, 6, 0, 0],
    # [0, 5, 1, 6, 0, 0, 8, 3, 9],
    # [5, 1, 9, 0, 4, 6, 3, 2, 8],
    # [8, 0, 2, 1, 0, 5, 7, 0, 6],
    # [6, 7, 4, 3, 2, 0, 0, 0, 5],
    # [0, 0, 0, 4, 5, 7, 2, 6, 3],
    # [3, 2, 0, 0, 8, 0, 0, 5, 7],
    # [7, 4, 5, 0, 0, 3, 9, 0, 1]
    # ]

    # print(sudoku_grid_correct(sudoku2))