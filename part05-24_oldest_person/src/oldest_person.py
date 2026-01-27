# Write your solution here
def oldest_person(people: list):
    oldest = people[0]
    for person in people:
        if person[1] < oldest[1]:
            oldest = person
    return oldest[0]


# def oldest_person(people: list):
#     oldest = 0
#     oldest_pos = 0
#     name = ""
#     for person in range(len(people)):
#         if oldest == 0 or people[person][1] < oldest:
#             oldest = people[person][1]
#             oldest_pos = person
#     return people[oldest_pos][0]

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))