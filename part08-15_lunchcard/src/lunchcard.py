# Write your solution here:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def eat_lunch(self):
        self.balance -= 2.60

    def eat_special(self):
        self.balance -= 4.60

    def deposit_money(self, deposit: float):
        if deposit < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += deposit


    
peters_card = LunchCard(20)
graces_card = LunchCard(30)

# Peter eats a special
peters_card.eat_special()
# Grace eats a regular lunch
graces_card.eat_lunch()

print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

# Peter deposits 20 euros
peters_card.deposit_money(20)
# Grace eats the special
graces_card.eat_special()

# Print out the balance on each card
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

# Peter eats a regular lunch
peters_card.eat_lunch()
# Peter eats a regular lunch (second time)
peters_card.eat_lunch()
# Grace deposits 50 euros
graces_card.deposit_money(50)

# Print out the balance on each card
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

