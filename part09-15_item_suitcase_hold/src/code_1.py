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

    def heaviest_item(self):
        if not self.__items:
            return None

        heaviest = self.__items[0]
        for item in self.__items:
            if item.weight() > heaviest.weight():
                heaviest = item
        return heaviest

    def __str__(self):
        if len(self.__items) == 1:
            return f"1 item ({self.weight()} kg)"
        else:
            return f"{len(self.__items)} items ({self.weight()} kg)"

class CargoHold:
    def __init__(self, max_weight: float):
        self.__max_weight = max_weight
        self.__cargo = []

    def weight_left(self):
        total_weight = 0
        for suitcase in self.__cargo:
            total_weight += suitcase.weight()
        return self.__max_weight - total_weight

    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() <= self.weight_left():
            self.__cargo.append(suitcase)

    def __str__(self):

        return f"{len(self.__cargo)} suitcases, space for {self.weight_left()} kg"
