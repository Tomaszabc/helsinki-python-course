class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def grade(self):
        return self.__grade

    def credits(self):
        return self.__credits

    def __str__(self):
            return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"

class StudyRecords:
    def __init__(self):
        self.courses = {}

    def add_completion(self, course_name, grade, op):
        if course_name in self.courses and self.courses[course_name].grade() > grade:
            return

        self.courses[course_name] = Course(course_name, grade, op)

    def get_completion(self, course_name):
        if not course_name in self.courses:
            return None

        return self.courses[course_name]

    def get_statistics(self):
        number_of_courses = len(self.courses)
        credits = 0
        sum_of_grades = 0
        grades = [0, 0 ,0 ,0 ,0 ,0 ,0]

        for courses in self.courses.values():
            credits += courses.credits()
            sum_of_grades += courses.grade()
            grades[courses.grade()] += 1

        return {
            "number_of_courses": number_of_courses,
            "credits": credits,
            "average": sum_of_grades / number_of_courses,
            "grades": grades
        }
        

class Application:
    def __init__(self):
        self.register = StudyRecords()

    def ohje(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def new_completion(self):
        course_name = input("course: ")
        grade = int(input("grade: "))
        op = int(input("credits: "))
        self.register.add_completion(course_name, grade, op)

    def get_completion(self):
        course_name = input("course: ")
        courses = self.register.get_completion(course_name)
        if courses is None:
            print("no entry for this course")
        else:
            print(courses)

    def statistics(self):
        t = self.register.get_statistics()
        print(f"{t['number_of_courses']} completed courses, a total of {t['credits']} credits")
        print(f"mean {t['average']:.1f}")        
        print("grade distribution")
        for i in range(5, 0, -1):
            grade_hits = t['grades'][i]
            row = "x"*grade_hits
            print(f"{i}: {row}")

    def execute(self):
        self.ohje()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command=="1":
                self.new_completion()
            elif command=="2":
                self.get_completion()
            elif command=="3":
                self.statistics()

Application().execute()

# class Course:
#     def __init__(self, name: str, grade: int, credits: int):
#         self.__name = name
#         self.__grade = grade
#         self.__credits = credits

#     def name(self):
#         return self.__name
    
#     def grade(self):
#         return self.__grade

#     def credits(self):
#         return self.__credits

#     def set_grade(self, grade: int):
#         if grade > self.__grade:
#             self.__grade = grade

#     def __str__(self):
#         return (f"{self.__name} ({self.__credits} cr) grade {self.__grade}")

# class CoursesList:
#     def __init__(self):
#         self.__courses = {}

#     def add_course(self, name: str, grade: int, credits: int):
#         if name not in self.__courses:
#             self.__courses[name] = Course(name, grade, credits)
#         else:
#             existing_course = self.__courses[name]
#             if grade > existing_course.grade():
#                 existing_course.set_grade(grade)

#     def get_course_data(self, name: str):
#         return self.__courses.get(name)

#     def get_statistics(self):
#         number_of_courses = len(self.__courses)
#         total_credits = 0
#         total_grades = 0
#         grades_list = [0, 0, 0, 0, 0, 0]
#         for course in self.__courses.values():
#             grades_list[course.grade()] += 1
#             total_credits += course.credits()
#             total_grades += course.grade()
#         print(f"{number_of_courses} completed courses, a total of {total_credits} credits")

#         if number_of_courses > 0:
#             mean = total_grades / number_of_courses
#             print(f"mean {mean:.1f}")
#         else:
#             print("no grades")

#         print("grade distribution")
#         print(f"5: {grades_list[5] * 'x'}")
#         print(f"4: {grades_list[4] * 'x'}")
#         print(f"3: {grades_list[3] * 'x'}")
#         print(f"2: {grades_list[2] * 'x'}")
#         print(f"1: {grades_list[1] * 'x'}")


# class Application:
#     def __init__(self):
#         self.__courses_list = CoursesList()

#     def help(self):
#         print("1 add course")
#         print("2 get course data")
#         print("3 statistics")
#         print("0 exit")

#     def add_course(self):
#         name = input("course: ")
#         grade = int(input("grade: "))
#         credits = int(input("credits: "))
#         self.__courses_list.add_course(name, grade, credits)

#     def get_course_data(self):
#         course_name = input("Course name: ")
#         course = self.__courses_list.get_course_data(course_name)
#         if course is None:
#             print("no entry for this course")
#         else:
#             print(course)

#     def statistics(self):
#         self.__courses_list.get_statistics()

#     def execute(self):
#         self.help()
#         while True:
#             print("")
#             command = input("command: ")
#             if command == "0":
#                 break
#             elif command == "1":
#                 self.add_course()
#             elif command == "2":
#                 self.get_course_data()
#             elif command == "3":
#                 self.statistics()
#             else:
#                 self.help()


# application = Application()
# application.execute()