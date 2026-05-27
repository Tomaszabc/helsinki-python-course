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

    def get_sum(self):
        return self.sum
    
    def average(self):
        if self.count != 0:
            return self.sum/self.count
        else:
            return 0

#mai
print("Please type in integer numbers:")
all_stats = NumberStats()
even_stats = NumberStats()
odd_stats = NumberStats()

while True:
    number = int(input())
    if number == -1:
        break
    all_stats.add_number(number)

    if number % 2 == 0:
        even_stats.add_number(number)
    else:
        odd_stats.add_number(number)

print("Sum of numbers:", all_stats.get_sum())
print("Mean of numbers:", all_stats.average())
print("Sum of even numbers:", even_stats.get_sum())
print("Sum of odd numbers:", odd_stats.get_sum())

