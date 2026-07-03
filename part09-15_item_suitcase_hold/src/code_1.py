# Write your solution here:
class Item:
    def __init__(self, name: str, weight: float):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f"{self.__name}({self.__weight} kg)"
    
    def name(self):
        return self.__name

    def weight(self):
        return self.__weight


class Suitcase():
    def __init__(self, maximum_weight: float):
        self.__maximum_weight = maximum_weight
        self.__items = []

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.__maximum_weight:
            self.__items.append(item)
   
    def print_items(self):
        for item in self.__items:
            print(item.__str__())

    def weight(self):
        total = 0
        for item in self.__items:
            total += item.weight()
        return total

    def __str__(self):
        if self.__items_number != 1:
            return f"{self.__items_number} items ({self.__weight} kg)"
        else:
            return f"{self.__items_number} item ({self.__weight} kg)"

book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

suitcase = Suitcase(10)
suitcase.add_item(book)
suitcase.add_item(phone)
suitcase.add_item(brick)

print("The suitcase contains the following items:")
suitcase.print_items()
combined_weight = suitcase.weight()
print(f"Combined weight: {combined_weight} kg")