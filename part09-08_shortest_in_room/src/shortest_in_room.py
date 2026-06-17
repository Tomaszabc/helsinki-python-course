# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)
    
    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        if not self.is_empty():
            combined_height = 0
            for person in self.persons:
                combined_height += person.height
            print(f"There are {len(self.persons)} persons in the room, and their combined height is {combined_height} cm")
            for person in self.persons:
                print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if self.is_empty():
            return None

        shortest = self.persons[0]
        for person in self.persons:
            if person.height < shortest.height:
                shortest = person
        return shortest
    
    def remove_shortest(self):
        if self.is_empty():
            return None
        
        shortest = self.persons[0]
        for person in self.persons:
            if person.height < shortest.height:
                shortest = person
        
        self.persons.remove(shortest)

        return shortest
        







if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()