# Write your solution here

# Write your solution here
def add_student(database: dict, name: str):
    database[name] = []
    
def print_student(database: dict, name: str):
    if name in database:
        if database[name] == {}:
            print(f"{name}: no completed courses")
        else:
            print(f"{name}: ")
            print(f" {len(database[name])} completed courses:")
            grade_sum = 0
            for i in range(len(database[name])):
                print(f"  {database[name][i]}")
                grade_sum += database[name][i][1]
            print(f" average grade {grade_sum/len(database[name])}")
    else: 
        print(f"{name}: no such person in the database")

def add_course(database: dict, name: str, course: tuple):
    if name in database:
        if database[name] == [] and course[1] != 0:
            database[name] = [course]
        elif course[1] != 0:
            database[name].append(course)
    else:
        print(f"{name}: no such person in the database")

def summary(database: dict):
    most_courses = 0
    name_most_courses = ""
    for people in database:
        if len(database[people]) > most_courses:
            most_courses = len(database[people])
            name_most_courses = people
    grades = []
    highest_avg = 0
    highest_avg_ppl = ""
    if len(database[people]) == 0:
        avg = 0
    else:
        avg = grades/len(database[people])
    for people in database:
        grades = 0
        for course in database[people]:
            grades += course[1]
            if avg > highest_avg:
                highest_avg = avg
                highest_avg_ppl = people


    print(f"students {len(database)}")
    if most_courses == []:
        most_courses = 0
    print(f"most courses completed {most_courses} {name_most_courses}")
    print(f"best average grade {highest_avg} {highest_avg_ppl}")
    

if __name__ == "__main__":
#     students = {}
#     add_student(students, "Peter")
#     add_student(students, "Eliza")
#     print_student(students, "Peter")
#     print_student(students, "Eliza")
#     print_student(students, "Jack")

# # Peter:
# #  no completed courses
# # Eliza:
# #  no completed courses
# # Jack: no such person in the database

    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # print_student(students, "Peter")

    # students = {}
    # add_student(students, "Peter")
    # add_student(students, "Eliza")
    # add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    # add_course(students, "Peter", ("Introduction to Programming", 1))
    # add_course(students, "Peter", ("Advanced Course in Programming", 1))
    # add_course(students, "Eliza", ("Introduction to Programming", 5))
    # add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    # summary(students)

    students = {}
    add_student(students, "Peter")
    add_student(students, "Emily")
    print_student(students, "Peter")
    print_student(students, "Emily")
    print_student(students, "Andy")
