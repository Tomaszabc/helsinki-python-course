# Write your solution here
from datetime import datetime

def cheaters():
    start_times = {}
    with open("start_times.csv") as file:
        for line in file:
            line = line.strip()
            if line:
                name, time_str = line.split(";")
                start_times[name] = datetime.strptime(time_str, "%H:%M")
        
    cheaters_list = []
    cheaters_set = set()

    with open("submissions.csv") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(";")
                name = parts[0]
                task = parts[1]
                points = parts[2]
                time_str = parts[3]

            if name not in start_times:
                continue

            submission_time = datetime.strptime(time_str, "%H:%M")
            start_time = start_times[name]

            time_diff = (submission_time - start_time).total_seconds() / 3600
            
            if time_diff > 3:
                cheaters_set.add(name)

    cheaters_list = list(cheaters_set)
    cheaters_list.sort()

    return cheaters_list