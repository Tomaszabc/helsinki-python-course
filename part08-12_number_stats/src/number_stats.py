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
