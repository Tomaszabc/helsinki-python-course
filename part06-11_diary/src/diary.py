with open("diary.txt") as file:
    content = []
    for row in file:
        content.append(row.replace("\n",""))

with open("diary.txt", "a") as file:
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        function = input("Function: ")
        if function == "1":
            entry = input("Diary entry: ")
            file.write(entry + "\n")
            content.append(entry)
            print("Diary saved")
        elif function == "2":
            print("Entries:")
            for entry in content:
                print(entry)
        elif function == "0":
            print("Bye now!")
            break


# # Write your solution here
# while True:
#     print("1 - add an entry, 2 - read entries, 0 - quit")
#     user_choose = input("Function: ")
#     if user_choose == "1":
#         diary_text = input("Diary entry: ")
#         with open("diary.txt", "a") as my_file:
#             my_file.write(diary_text + "\n")
#             print("Diary saved")


#     elif user_choose == "2":
#         print("Entries:")
#         with open("diary.txt") as my_file:
#             for line in my_file:
#                 print(line.strip())
#     elif user_choose == "0":
#         print("Bye now!")
#         break
