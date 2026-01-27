# Write your solution here
def add_student(database: dict, name: str):
    database[name] = []
    
def print_student(database: dict, name: str):
    if name in database:
        if database[name] == []:
            print(f"{name}:")
            print(" no completed courses")
        else:
            print(f"{name}: ")
            if len(database[name]) != 0:
                print(f" {len(database[name])} completed courses:")

            grade_sum = 0
            for i in range(len(database[name])):
                print(f"  {database[name][i]}")
                grade_sum += database[name][i][1]

    else: 
        print(f"{name}: no such person in the database")

def add_course(database: dict, name: str, course: tuple):
    if name in database:
        if database[name] == []:
            database[name] = [course]
        else:
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
    best_avg_grade = 0
    best_avg_grade_name = ""
    for people in database:
        temp_avg_grade = 0
        count = 0
        for grade in database[people]:
            count += 1
            temp_avg_grade += grade[1]/count
            if temp_avg_grade > best_avg_grade:
                best_avg_grade = temp_avg_grade
                best_avg_grade_name = people
 
    
    print(f"students {len(database)}")
    print(f"most courses completed {most_courses} {name_most_courses}")
    print(f"best average grade {best_avg_grade:.1f} {best_avg_grade_name}")
    

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")

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
    # add_course(students, "Peter", ("Data Structures and Algorithms", 5))
    # add_course(students, "Peter", ("Introduction to Programming", 5))
    # add_course(students, "Peter", ("Advanced Course in Programming", 5))
    # add_course(students, "Eliza", ("Introduction to Programming", 5))
    # add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    # summary(students)