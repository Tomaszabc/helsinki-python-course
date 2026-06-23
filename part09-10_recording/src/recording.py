# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, length: int):
        self.length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_length):
        if new_length > 0:
            self.__length = new_length
        else:
            raise ValueError("Must be > 0")


if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)