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

    def __str__(self):
        return (f"{self.__name} ({self.__credits} cr), grade {self.__grade}")

class CoursesList:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        course = Course(name, grade, credits)

        self.__courses[name] = course

class Application:


