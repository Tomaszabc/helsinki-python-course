def user_input():
    if True:
        student_info = input("Student information: ")
        exercises_comp = input("Exercises completed: ")
    else:
        student_info = "students1.csv"
        exercises_comp = "exercises1.csv"


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
            exercises_numbers = []
            exercises_sum[parts[0]] = [int(num.strip()) for num in parts[1:]]
            

    return names, exercises_sum

def print_data():
    names, exercises_sum = user_input()

    for ids, name in names.items():
        if ids in exercises_sum:
            result = exercises_sum[ids]
            total = sum(result)
            print(f"{name} {total}")


print_data()