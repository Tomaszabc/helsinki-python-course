# Write your solution here
students = int(input("students"))
group_size = int(input("g size"))
groups = int((students + group_size -1) // group_size)
print(f"Number of groups formed: {groups}")