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
            for course in database[name]:
                course_name, grade = course
                print(f"  {course_name} {grade}")
                grade_sum += grade
            if len(database[name]) != 0:    
                print(f" average grade {grade_sum/len(database[name])}")
            else:
                print(f" average grade 0")

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
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")