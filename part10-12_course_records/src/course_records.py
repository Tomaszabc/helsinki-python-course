# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self):
        return self.__name

    def grade(self):
        return self.__grade

    def credits(self):
        return self.__credits

    def set_grade(self, grade: int):
        if grade > self.__grade:
            self.__grade = grade

class StudyTracker:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.__courses:
            self.__courses[name] = Course(name, grade, credits)
        else:
            current = self.__courses[name]
            if grade > current.grade():
                current.set_grade(grade)
    
    def get_course(self, name: str):
        return self.__courses.get(name)

    def get_all_courses(self):
        return list(self.__courses.values())

class StudyTrackerApplication:
    def __init__(self):
        self.__tracker = StudyTracker()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__tracker.add_course(name, grade, credits)

    def get_course(self):
        name = input("course: ")
        course = self.__tracker.get_course(name)
        if course is None:
            print("no entry for this course")
        else:
            print(f"{course.name()} ({course.credits()} cr) grade {course.grade()}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course()
            elif command == "3":
                self.statistics()
            else:
                self.help()

    def statistics(self):
        courses = self.__tracker.get_all_courses()
        count = len(courses)
        total_credits = sum(c.credits() for c in courses)
        total_grades = sum(c.grade() for c in courses)
        mean = total_grades / count if count > 0 else 0

        print(f"{count} completed courses, a total of {total_credits} credits")
        print(f"mean {mean:.1f}")

        grade_distribution = {1:0, 2:0, 3:0, 4:0, 5:0}
        for course in courses:
            grade_distribution[course.grade()] += 1

        print("grade distribution")
        for grade in range(5, 0, -1):
            print(f"{grade}: {'x' * grade_distribution[grade]}")


application = StudyTrackerApplication()
application.execute()