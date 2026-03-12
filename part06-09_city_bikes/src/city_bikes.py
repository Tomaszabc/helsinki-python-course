# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
    stations = {}

    with open(filename) as file:
        for line in file:
            parts = line.split(";")
            
            if parts[0] == "Longitude":
                continue

            name = parts[3]
            longitude = float(parts[0])
            latitude = float(parts[1])

            stations[name] = (longitude, latitude)

    return stations

def distance(stations: dict, station1: str, station2: str):
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    station1 = None
    station2 = None
    max_distance = 0

    for name1 in stations:
        for name2 in stations:
            if name1 == name2:
                continue

            d = distance(stations, name1, name2)

            if d > max_distance:
                max_distance = d
                station1 = name1
                station2 = name2

    return (station1, station2, max_distance)


# def main():
#     filename = "stations1.csv"
#     get_station_data(filename)

# main()