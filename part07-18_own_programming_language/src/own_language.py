def run(program):
    # Inicjalizacja zmiennych A-Z
    variables = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
    
    # Słownik do przechowywania lokalizacji (etykiet)
    labels = {}
    
    # Znajdź wszystkie etykiety w programie
    for i, line in enumerate(program):
        line = line.strip()
        # Szukaj etykiety: może być "label:" lub "label::"
        if ":" in line and not line.startswith("IF"):  # unikaj mylenia z IF
            # Sprawdź czy to etykieta (nie część komendy)
            if " " not in line.split(":")[0]:  # etykieta nie ma spacji
                label = line.split(":")[0].strip()
                labels[label] = i
    
    # Lista na wyniki PRINT
    results = []
    
    # Licznik bieżącej linii
    line_number = 0
    
    while line_number < len(program):
        line = program[line_number].strip()
        
        # Pomiń puste linie
        if not line:
            line_number += 1
            continue
        
        # Jeśli to etykieta (linia zawiera : i nie jest komendą)
        if ":" in line and not line.startswith(("IF", "PRINT", "MOV", "ADD", "SUB", "MUL", "JUMP", "END")):
            line_number += 1
            continue
        
        # Podziel linię na części
        parts = line.split()
        command = parts[0]
        
        # ---------- PRINT ----------
        if command == "PRINT":
            value = get_value(parts[1], variables)
            results.append(value)
            line_number += 1
        
        # ---------- MOV ----------
        elif command == "MOV":
            var = parts[1]
            value = get_value(parts[2], variables)
            variables[var] = value
            line_number += 1
        
        # ---------- ADD ----------
        elif command == "ADD":
            var = parts[1]
            value = get_value(parts[2], variables)
            variables[var] += value
            line_number += 1
        
        # ---------- SUB ----------
        elif command == "SUB":
            var = parts[1]
            value = get_value(parts[2], variables)
            variables[var] -= value
            line_number += 1
        
        # ---------- MUL ----------
        elif command == "MUL":
            var = parts[1]
            value = get_value(parts[2], variables)
            variables[var] *= value
            line_number += 1
        
        # ---------- JUMP ----------
        elif command == "JUMP":
            label = parts[1]
            if label in labels:
                line_number = labels[label]
            else:
                line_number += 1
        
        # ---------- IF ----------
        elif command == "IF":
            # Format: IF A > 0 JUMP start
            # parts[1] = A, parts[2] = >, parts[3] = 0, parts[4] = JUMP, parts[5] = start
            left = get_value(parts[1], variables)
            operator = parts[2]
            right = get_value(parts[3], variables)
            label = parts[5]
            
            condition = False
            if operator == "==":
                condition = (left == right)
            elif operator == "!=":
                condition = (left != right)
            elif operator == "<":
                condition = (left < right)
            elif operator == "<=":
                condition = (left <= right)
            elif operator == ">":
                condition = (left > right)
            elif operator == ">=":
                condition = (left >= right)
            
            if condition and label in labels:
                line_number = labels[label]
            else:
                line_number += 1
        
        # ---------- END ----------
        elif command == "END":
            break
        
        else:
            line_number += 1
    
    return results


def get_value(operand, variables):
    """
    Zwraca wartość operandu (liczba lub zmienna).
    """
    # Sprawdź czy to liczba (może być ujemna)
    if operand.isdigit() or (operand[0] == '-' and operand[1:].isdigit()):
        return int(operand)
    else:
        return variables.get(operand, 0)

if __name__ == "__main__":
    program = []
    print("Wpisz komendy (wpisz 'END' aby zakończyć):")
    
    while True:
        line = input("> ")
        program.append(line)
        if line == "END":
            break
    
    result = run(program)
    print("Wynik:", result)