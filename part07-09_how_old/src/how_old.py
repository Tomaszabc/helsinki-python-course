from datetime import date

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

millenium_eve = date(1999, 12, 31)
birth_date = date(year, month, day)

if birth_date < millenium_eve:
    age = millenium_eve - birth_date
    print(f"You were {age.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
