# tee ratkaisu tänne
if True:
    student_data = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    course_data = input("Course information: ")
else:
    # Użyj ścieżki względnej
    student_data = "src/students1.csv"
    exercise_data = "src/exercises1.csv"
    exam_data = "src/exam_points1.csv"
    course_data = "src/course1.txt"
 
def grade(points):
    a = 0
    limits = [15, 18, 21, 24, 28]
    while a < 5 and points >= limits[a]:
        a += 1
    return a
 
def to_points(number):
    return number // 4

# Czytanie informacji o kursie
course_name = ""
course_credits = ""
with open(course_data) as file:
    for line in file:
        line = line.strip()
        if line.startswith("name:"):
            course_name = line[5:].strip()
        elif line.startswith("study credits:"):
            course_credits = line[14:].strip()

# Czytanie danych studentów
students = {}
with open(student_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"
 
# Czytanie danych ćwiczeń
exercises = {}
with open(exercise_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        esum = 0
        for i in range(1, 8):
            esum += int(parts[i])
        exercises[parts[0]] = esum
 
# Czytanie danych egzaminów
exams = {}
with open(exam_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue 
        esum = 0
        for i in range(1, 4):
            esum += int(parts[i])
        exams[parts[0]] = esum

# Zapisz do pliku results.txt
with open("results.txt", "w") as txt_file:
    # Nagłówek z informacjami o kursie
    txt_file.write(f"{course_name}, {course_credits} credits\n")
    txt_file.write("=" * 38 + "\n")
    txt_file.write(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}\n")
    
    # Dane dla każdego studenta
    for student_id, name in students.items():
        exercise_sum = exercises[student_id]
        exercise_points = to_points(exercise_sum)
        exam_points = exams[student_id]
        total_points = exam_points + exercise_points
        final_grade = grade(total_points)
        
        txt_file.write(f"{name:<30}{exercise_sum:<10}{exercise_points:<10}{exam_points:<10}{total_points:<10}{final_grade:<10}\n")

# Zapisz do pliku results.csv
with open("results.csv", "w") as csv_file:
    for student_id, name in students.items():
        exercise_sum = exercises[student_id]
        exercise_points = to_points(exercise_sum)
        exam_points = exams[student_id]
        total_points = exam_points + exercise_points
        final_grade = grade(total_points)
        
        csv_file.write(f"{student_id};{name};{final_grade}\n")

# Komunikat dla użytkownika
print("Results written to files results.txt and results.csv")