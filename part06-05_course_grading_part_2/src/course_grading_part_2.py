# wwite your solution here
def user_input():
    if False:
        student_info = input("Student information: ")
        exercises_comp = input("Exercises completed: ")
        exam_points = input("Exam points: ")
    else:
        student_info = "students1.csv"
        exercises_comp = "exercises1.csv"
        exam_points = "exam_points1.csv"


    names = {}

    with open(student_info) as student_file:
        for line in student_file:
            parts = line.split(";")
            if parts [0] == "id":
                continue
            names[parts[0]] = parts[1].strip() + " " + parts[2].strip()
    

    exercises_sum = {}

    with open(exercises_comp) as exercises_file:
        for line in exercises_file:
            parts = line.split(";")
            if parts[0] == "id":
                continue
            exercises_sum[parts[0]] = [int(num.strip()) for num in parts[1:]]

    exam_grades = {}
    with open(exam_points) as exam_file:
        for line in exam_file:
            parts = line.split(";")
            if parts[0] == "id":
                continue
            exam_grades[parts[0]] = [int(num.strip()) for num in parts[1:]]

    return names, exercises_sum, exam_grades



def print_data():
    names, exercises_sum, exam_grades = user_input()

    grades = [0,1,2,3,4,5,6]
    for ids, name in names.items():
        if ids in exercises_sum:
            result = exercises_sum[ids]
            exam_result = exam_grades[ids]
            total = sum(result)
            exam_total = sum(exam_result)
            final_grade = []
            points_from_exercises = int((total/40)*10)
            final_points = points_from_exercises + exam_total
            if final_points < 15:
                final_grade = grades[0]
            elif final_points < 18:
                final_grade = grades[1]
            elif final_points < 21:
                final_grade = grades[2]
            elif final_points < 24:
                final_grade = grades[3]
            elif final_points < 28:
                final_grade = grades[4]
            elif final_points >= 28:
                final_grade = grades[5]
            print(f"{name} {final_grade}")


print_data()