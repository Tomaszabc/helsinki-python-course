# WRITE YOUR SOLUTION HERE:
class ListHelper:   
    # def __init__(self, my_list: list):
    #     self.my_list = my_list
    @classmethod
    def greatest_frequency(cls, my_list: list):
        counts = {}
        for item in my_list:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1

        max_count = 0
        most_common = None
        for item, count in counts.items():
            if count > max_count:
                max_count = count
                most_common = item

        return most_common

    @classmethod
    def doubles(cls, my_list: list):
        counts = {}
        for item in my_list:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1

        double_count = 0


numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))