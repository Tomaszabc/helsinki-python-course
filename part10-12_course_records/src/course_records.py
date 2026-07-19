# tee ratkaisusi tänne
class CourseRecords:

    def help():
        print("1 add course")
        print("2 get course data")  
        print("3 statistics")
        print("0 exit")

    def exec():
        help() 
        user_number = input("Input number")
        if user_number == 1:
            pass
        elif user_number == 2:
            pass
        elif user_number == 3:
            pass
        elif user_number == 0:
            pass
        else:
            print("Wrong number")
            

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

CourseRecords.exec()