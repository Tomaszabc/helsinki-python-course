# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date


def list_years(dates: list):

    return sorted([d.year for d in dates])


# def list_years(dates: list):
#     chronological = []

#     for i in dates:
#         year = i.year
#         chronological.append(year)

#     chronological.sort()
#     return chronological