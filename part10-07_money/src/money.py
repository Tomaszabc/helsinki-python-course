# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents

    def __str__(self):
        return f"{self.euros}.{self.cents:02d} eur"

    def __eq__(self, another):
        return (self.euros + (self.cents/100)) == (another.euros + (another.cents/100))

    def __ne__(self, another):
        return (self.euros + (self.cents/100)) != (another.euros + (another.cents/100))

    def __lt__(self, another):
        return (self.euros + (self.cents/100)) < (another.euros + (another.cents/100))
    def __gt__(self, another):
        return (self.euros + (self.cents/100)) > (another.euros + (another.cents/100))

if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)
    e3 = Money(4, 10)

    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)

    e1 = Money(4, 10)
    e2 = Money(2, 5)

    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)
    