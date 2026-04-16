import csv
from datetime import datetime, timedelta

def cheaters():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        # First read students and start times to memory    
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time
        # Then read submissions
        # From each student, last (i.e. greatest) is saved
        submission_times = {}
        for row in csv.reader(submission, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[3], "%H:%M")
        # If name does not exists in dictionary, add time directly to the dictionary
            if name not in submission_times:
                submission_times[name] = time
        # If there alredy exists time for key, compare if current time is greater
            elif time > submission_times[name]:
                submission_times[name] = time

        cheaters = []
        # Iterate through students one by one
        for name in start_times:
            if submission_times[name] - start_times[name] > timedelta(hours = 3):
                cheaters.append(name)
        return cheaters




# # Write your solution here
# from datetime import datetime

# def cheaters():
#     start_times = {}
#     with open("start_times.csv") as file:
#         for line in file:
#             line = line.strip()
#             if line:
#                 name, time_str = line.split(";")
#                 start_times[name] = datetime.strptime(time_str, "%H:%M")
        
#     cheaters_list = []
#     cheaters_set = set()

#     with open("submissions.csv") as file:
#         for line in file:
#             line = line.strip()
#             if line:
#                 parts = line.split(";")
#                 name = parts[0]
#                 task = parts[1]
#                 points = parts[2]
#                 time_str = parts[3]

#             if name not in start_times:
#                 continue

#             submission_time = datetime.strptime(time_str, "%H:%M")
#             start_time = start_times[name]

#             time_diff = (submission_time - start_time).total_seconds() / 3600
            
#             if time_diff > 3:
#                 cheaters_set.add(name)

#     cheaters_list = list(cheaters_set)
#     cheaters_list.sort()

#     return cheaters_list