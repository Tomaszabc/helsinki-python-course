# Write your solution here
def filter_incorrect():
    correct_lines = []

    with open("lottery_numbers.csv") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(";")

            if len(parts) != 2:
                continue

            week_part = parts[0]
            numbers_part = parts[1]

            if not week_part.startswith("week "):
                continue

            try:
                week_number = int(week_part[5:])

            except ValueError:
                continue

            numbers = numbers_part.split(",")

            if len(numbers) != 7:
                continue

            valid = True
            number_set = set()

            for num_str in numbers:
                try:
                    num = int(num_str)
                    
                    if num < 1 or num > 39:
                        valid = False
                        break
                    if num in number_set:
                        valid = False
                        break
                    
                    number_set.add(num)
                except ValueError:
                    valid = False
                    break
            if not valid:
                continue

            correct_lines.append(line)

    with open("correct_numbers.csv", "w") as file:
        for line in correct_lines:
            file.write(line + "\n")