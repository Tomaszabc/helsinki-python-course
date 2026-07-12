# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if self.year != other.year:
            return self.year < other.year
        if self.month != other.month:
            return self.month < other.month
        if self.day != other.day:
            return self.day < other.day

    def __gt__(self, other):
        # Porównaj lata
        if self.year != other.year:
            return self.year > other.year
        # Lata są równe – porównaj miesiące
        if self.month != other.month:
            return self.month > other.month
        # Lata i miesiące są równe – porównaj dni
        return self.day > other.day 

    def __add__(self, days_to_add: int):
        new_day = self.day
        new_month = self.month
        new_year = self.year

        new_day += days_to_add

        while new_day > 30:
            new_day -= 30
            new_month += 1
            if new_month > 12:
                new_month = 1
                new_year += 1

        return SimpleDate(new_day, new_month, new_year)

    def __sub__(self, other: "SimpleDate"):
        days_in_self = self.day + (self.month * 30) + (self.year * 360)
        days_in_other = other.day + (other.month * 30) + (other.year * 360)
        return abs(days_in_self - days_in_other)

        




if __name__ == "__main__":
    # d1 = SimpleDate(4, 10, 2020)
    # d2 = SimpleDate(28, 12, 1985)
    # d3 = SimpleDate(28, 12, 1985)

    # print(d1)
    # print(d2)
    # print(d1 == d2)
    # print(d1 != d2)
    # print(d1 == d3)
    # print(d1 < d2)
    # print(d1 > d2)

    # d1 = SimpleDate(4, 10, 2020)
    # d2 = SimpleDate(28, 12, 1985)

    # d3 = d1 + 3
    # d4 = d2 + 400

    # print(d1)
    # print(d2)
    # print(d3)
    # print(d4)

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)