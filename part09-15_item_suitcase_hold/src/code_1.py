# Write your solution here:
class Item:
    def __init__(self, name: str, weight: float):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f"{self.__name}({self.__weight})"
    
    def name(self):
        return self.__name

    def weight(self):
        return self.__weight


class Suitcase():
    def __init__(self, maximum_weight: float):
        self.__maximum_weight = maximum_weight
        self.__weight = 0
        self.__items_number = 0

    def add_item(self, item: Item):
        if self.__weight + item.weight() <= self.__maximum_weight:
            self.__weight += item.weight()
            self.__items_number += 1


    def __str__(self):
        return f"{self.__items_number} items ({self.__weight} kg)"

book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

suitcase = Suitcase(5)
print(suitcase)

suitcase.add_item(book)
print(suitcase)

suitcase.add_item(phone)
print(suitcase)

suitcase.add_item(brick)
print(suitcase)