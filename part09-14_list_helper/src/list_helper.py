# WRITE YOUR SOLUTION HERE:
class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        if not my_list:
            return None
            
        counts = {}
        for item in my_list:
            if item in counts:
                counts[item] = counts[item] + 1
            else:
                counts[item] = 1

        most_common = None
        max_count = 0
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
                counts[item] = counts[item] + 1
            else:
                counts[item] = 1

        double_count = 0
        for count in counts.values():
            if count >= 2:
                double_count += 1

        return double_count

    
if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))