class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __value(self):
        return self.__euros * 100 + self.__cents

    def __eq__(self, another):
        return self.__value() == another.__value()

    def __ne__(self, another):
        return self.__value() != another.__value()

    def __lt__(self, another):
        return self.__value() < another.__value()

    def __gt__(self, another):
        return self.__value() > another.__value()

    def __add__(self, another):
        total_cents = self.__value() + another.__value()
        euros = total_cents // 100
        cents = total_cents % 100
        return Money(euros, cents)

    def __sub__(self, another):
        total_cents = self.__value() - another.__value()
        if total_cents < 0:
            raise ValueError("a negative result is not allowed")
        euros = total_cents // 100
        cents = total_cents % 100
        return Money(euros, cents)



if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

   

    print(e1)
    e1.__euros = 2000
    print(e1)
    