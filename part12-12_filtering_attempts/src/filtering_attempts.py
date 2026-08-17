class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# 1. Accepted attempts (grade >= 1)
def accepted(attempts: list):
    return list(filter(lambda x: x.grade >= 1, attempts))

# 2. Attempts with grade (grade == given grade)
def attempts_with_grade(attempts: list, grade: int):
    return list(filter(lambda x: x.grade == grade, attempts))

# 3. Students who passed the course (grade > 0, sorted alphabetically)
def passed_students(attempts: list, course: str):
    return sorted(map(lambda x: x.student_name, 
                      filter(lambda x: x.course_name == course and x.grade > 0, attempts)))


# Testy
if __name__ == "__main__":
    # Test accepted
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 0)

    print("Accepted attempts:")
    for attempt in accepted([s1, s2, s3]):
        print(attempt)

    print()

    # Test attempts_with_grade
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 3)
    s4 = CourseAttempt("Olivia C. Objective", "Data Structures and Algorithms", 3)

    print("Attempts with grade 3:")
    for attempt in attempts_with_grade([s1, s2, s3, s4], 3):
        print(attempt)

    print()

    # Test passed_students
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
    s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

    print("Students who passed Introduction to AI:")
    for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
        print(attempt)