# Write your solution here
from datetime import date

def is_it_valid(pic: str):
    if len(pic) != 11:
        return False

    try:
        day = int(pic[0:2])
        month = int(pic[2:4])
        year = int(pic[4:6])
    except ValueError:
        return False

    century_marker = pic[6]
    personal_id = pic[7:10]
    control_char = pic[10]

    if century_marker not in "+-A":
        return False
    
    if not personal_id.isdigit():
        return False

    if century_marker == "+":
        full_year = 1800 + year
    elif century_marker == "-":
        full_year = 1900 + year
    else:  
        full_year = 2000 + year

    try:
        birth_date = date(full_year, month, day)
    except ValueError:
        return False
    


    nine_digit = pic[0:6] + personal_id
    nine_digit_int = int(nine_digit)

    remainder = nine_digit_int % 31

    control_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    if control_char != control_chars[remainder]:
        return False

    return True