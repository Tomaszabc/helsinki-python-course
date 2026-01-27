def user_input():
    input_list = []
    while True:
        user_inpt = input("Exam points and exercises completed: ")
        if len(user_inpt) == 0:
            break
        input_list.append(user_inpt)
    return input_list

def points_average(get_input):
    points_list = []
    for i in get_input:
        sliced_input = i.split()
        exam_pts = int(sliced_input[0])
        exercise_pts = int(sliced_input[1])
        total_points = exam_pts + (exercise_pts // 10)
        points_list.append(total_points)
    points_average = sum(points_list) / len(points_list)
    return points_average

def pass_percentage(get_input):
    pass_list = [0, 0]
    for i in get_input:
        sliced_input = i.split()
        exam_pts = int(sliced_input[0])
        exercise_pts = int(sliced_input[1])
        total_points = exam_pts + (exercise_pts // 10)
        if exam_pts < 10:
            pass_list[0] += 1
        else:
            if total_points > 14:
                pass_list[1] += 1
            else:
                pass_list[0] += 1
    percentage = pass_list[1] / len(get_input) * 100
    return percentage



def grades(get_input):
    grades = [0] * 6
    for i in get_input:
        sliced_input = i.split()
        exam_pts = int(sliced_input[0])
        exercise_pts = int(sliced_input[1])
        total_points = exam_pts + (exercise_pts // 10)
        if exam_pts < 10:
            grades[0] += 1
        else:
            if total_points > 27:
                grades[5] += 1
            elif total_points > 23:
                grades[4] += 1
            elif total_points > 20:
                grades[3] += 1
            elif total_points > 17:
                grades[2] += 1
            elif total_points > 14:
                grades[1] += 1
            else:
                grades[0] += 1
    return grades
                




def statistics(points_avg, pass_pct, grd):
    print("Statistics:")
    print(f"Points average: {points_avg:.1f}")
    print(f"Pass percentage: {pass_pct:.1f}")
    print("Grade distribution:")
    print(f"5: {grd[5] * "*"}")
    print(f"4: {grd[4] * "*"}")
    print(f"3: {grd[3] * "*"}")
    print(f"2: {grd[2] * "*"}")
    print(f"1: {grd[1] * "*"}")
    print(f"0: {grd[0] * "*"}")


def main():
    get_input = user_input()
    points_avg = points_average(get_input)
    pass_pct = pass_percentage(get_input)
    grd = grades(get_input)
    statistics(points_avg, pass_pct, grd)

main()