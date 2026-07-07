# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__observ = []

        

    def add_observation(self, observation: str):
        if observation != "":
            self.__observ.append(observation)
        else:
            raise ValueError("must be a non empty string")
    def latest_observation(self):
        if len(self.__observ) > 0:
            return self.__observ[-1]
        else:
            return ""
    def number_of_observations(self):
        return len(self.__observ)

    def __str__(self):
        return f"{self.__name}, {len(self.__observ)} observations"

if __name__ == "__main__":

    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)

