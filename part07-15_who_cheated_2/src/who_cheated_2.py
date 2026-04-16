# Write your solution here
from datetime import datetime

def final_points():
    start_times = {}
    with open("start_times.csv") as file:
        for line in file:
            line = line.strip()
            if line:
                name, time_str = line.split(";")
                start_times[name] = datetime.strptime(time_str, "%H:%M")
    
    student_tasks = {}

    with open("submissions.csv") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(";")
            name = parts[0]
            task = int(parts[1])
            points = int(parts[2])
            time_str = parts[3]

            if name not in start_times:
                continue

            submission_time = datetime.strptime(time_str, "%H:%M")
            start_time = start_times[name]

            time_diff = (submission_time - start_time).total_seconds() / 3600
        
            if time_diff > 3:
                continue

            if name not in student_tasks:
                student_tasks[name] = {}

            if task not in student_tasks[name] or points > student_tasks[name][task]:
                student_tasks[name][task] = points

    final_results = {}
    for name, tasks in student_tasks.items():
        total_points = sum(tasks.values())
        final_results[name] = total_points

    return final_results