from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
# def sum_of_all_credits_helper(credit_sum, attempt):
#     return credit_sum + attempt.credits

# def sum_of_all_credits(attempts: list):
#     return reduce(sum_of_all_credits_helper, attempts, 0)

def credit_summer(cr_sum, attempt):
    return cr_sum + attempt.credits

def sum_of_all_credits(attempts: list):
    return reduce(credit_summer, attempts, 0)

def sum_of_passed_credits(attempts: list):
    passed = filter(lambda x: x.grade > 0, attempts)
    return reduce(credit_summer, passed, 0)


def average(attempts: list):
    def grade_summer(cr_sum, attempt):
        return cr_sum + attempt.grade

    accepted = list(filter(lambda s: s.grade > 0, attempts))
    sum_of_grades = reduce(grade_summer, accepted, 0)

    return sum_of_grades / len(accepted)



if __name__ == "__main__":

    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)