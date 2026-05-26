# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
        self.sum = 0

    def add_number(self, number:int):
        self.count += 1
        self.sum += number

    def count_numbers(self):
        return self.count

stats = NumberStats()
stats.add_number(3)
stats.add_number(5)
stats.add_number(1)
stats.add_number(2)
print("Numbers added:", stats.count_numbers())