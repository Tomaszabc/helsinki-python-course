from datetime import datetime, timedelta

week = timedelta(days=7)

def format(time):
    return time.strftime("%d.%m.%Y")

file = input("Filename: ")
start = input("Starting date: ").split('.')
days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile): ")

screen_times = []
total = 0
start = datetime(int(start[2]), int(start[1]), int(start[0]))

for i in range(days):
    day = start + timedelta(days=i)
    times = input(f"Screen time {format(day)}: ").split(' ')
    tv = int(times[0])
    pc = int(times[1])
    mobile = int(times[2])
    total += tv + pc + mobile
    screen_times.append((day, tv, pc, mobile) )

with open(file, "w") as tdsto:
    tdsto.write(f"Time period: {format(start)}-{format(start + timedelta(days=(days-1)))}\n")
    tdsto.write(f"Total minutes: {total}\n")
    tdsto.write(f"Average minutes: {total/days:.1f}\n")
    for pv, tv, pc, mob in screen_times:
        tdsto.write(f"{format(pv)}: {tv}/{pc}/{mob}\n")

print(f"Data stored in file {file}")




# from datetime import datetime, timedelta

# filename = input("Filename: ")
# start_date = input("Starting date: ")
# days = int(input("How many days: "))

# start = datetime.strptime(start_date, "%d.%m.%Y")
# start_date_formatted = start.strftime("%d.%m.%Y")

# end = start + timedelta(days=days - 1)
# end_date_formatted = end.strftime("%d.%m.%Y")

# print("Please type in screen time in minutes on each day (TV computer mobile):")

# screen_data = []
# total = 0

# for i in range(days):
#     current_date = start + timedelta(days=i)
#     date_str = current_date.strftime("%d.%m.%Y")

#     entry = input(f"Screen time {date_str}: ")
#     tv, computer, mobile = map(int, entry.split())

#     screen_data.append((date_str, tv, computer, mobile))
#     total += tv + computer + mobile

#     average = total / days

# with open(filename, "w") as file:
#     file.write(f"Time period: {start_date_formatted}-{end_date_formatted}\n")
#     file.write(f"Total minutes: {total}\n")
#     file.write(f"Average minutes: {average}\n")

#     for date_str, tv, computer, mobile in screen_data:
#         file.write(f"{date_str}: {tv}/{computer}/{mobile}\n")

# print(f"Data stored in file {filename}")