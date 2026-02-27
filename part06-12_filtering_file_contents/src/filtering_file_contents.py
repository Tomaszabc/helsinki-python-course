def filter_solutions():
    with open("solutions.csv") as source, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
        for row in source:
            pieces = row.split(";")

            calculation = pieces[1]
            result = pieces[2]

            if "+" in calculation:
                operands = calculation.split("+")
                correct = int(operands[0]) + int(operands[1]) == int(result)
            else:
                operands = calculation.split("-")
                correct = int(operands[0]) - int(operands[1]) == int(result)

            if correct:
                correct_file.write(row)
            else:
                incorrect_file.write(row)
# # Write your solution here
# def filter_solutions():
#     correct = []
#     incorrect = []

#     with open("solutions.csv") as file:
#         for line in file:
#             line = line.strip()
#             parts = line.split(";")

#             name = parts[0]
#             problem = parts[1]
#             given_answer = int(parts[2])

#             if "+" in problem:
#                 operands = problem.split("+")
#                 correct_answer = int(operands[0]) + int(operands[1])
#             else:
#                 operands = problem.split("-")
#                 correct_answer = int(operands[0]) - int(operands[1])
            
#             if given_answer == correct_answer:
#                 correct.append(line)
#             else:
#                 incorrect.append(line)

#     with open("correct.csv", "w") as correct_file:
#         for line in correct:
#             correct_file.write(line + "\n")
#     with open("incorrect.csv", "w") as incorrect_file:
#         for line in incorrect:
#             incorrect_file.write(line + "\n")        