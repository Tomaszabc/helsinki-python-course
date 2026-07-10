# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents

    def __str__(self):
        return f"{self.euros}.{self.cents:02d} eur"

    def __value(self):
        return self.euros * 100 + self.cents

    def __eq__(self, another):
        return self.__value() == another.__value()

    def __ne__(self, another):
        return self.__value() != another.__value()

    def __lt__(self, another):
        return self.__value() < another.__value()

    def __gt__(self, another):
        return self.__value() > another.__value()

    def __add__(self, another):
        return self.__value() + another.__value()

    def __sub__(self, another):
        return self.__value() - another.__value()


if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1
    