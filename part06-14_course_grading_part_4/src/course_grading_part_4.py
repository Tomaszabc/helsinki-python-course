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
  
def get_grade(points):
    a = 0
    limits = [15, 18, 21, 24, 28]
    while a < 5 and points >= limits[a]:
        a += 1
    return a
 
def as_score(number):
    return number // 4
 
students = {}
with open(student_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"
 
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

with open(course_data) as file:
    rows = []
    for row in file:
        rows.append(row)

    course_name = rows[0][5:].strip()
    credits = int(rows[1][14:])

with open("results.txt", "w") as file:
    header = f"{course_name}, {credits} credits\n"
    file.write(header)
    separator = "="*(len(header)-1)
    file.write(f"{separator}\n")
    file.write("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")
    for student_id, name in students.items():
        exer = exercises[student_id]
        exer_score = as_score(exer)
        exam_pts = exams[student_id]
        tot_score = exer_score + exam_pts
        file.write(f"{name:30}{exer:<10}{exer_score:<10}{exam_pts:<10}{tot_score:<10}{get_grade(tot_score):<10}\n")

with open("results.csv", "w") as file:
    for student_id, name in students.items():
        exer = exercises[student_id]
        exer_score = as_score(exer)
        exam_pts = exams[student_id]
        tot_score = exer_score + exam_pts
        row = ";".join([student_id, name, str(get_grade(tot_score))])
        file.write(f"{row}\n")