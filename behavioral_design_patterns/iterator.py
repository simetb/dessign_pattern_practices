class RadioStation:
    def __init__(self, frequency: float) -> None:
        self.frequency = frequency

    def get_frequency(self) -> float:
        return self.frequency

class StationList:
    def __init__(self) -> None:
        self.stations = []
        self.counter = 0

    def add_station(self, station: RadioStation) -> None:
        self.stations.append(station)

    def remove_station(self, frequency: float) -> bool:
        for station in self.stations:
            if station.get_frequency() == frequency:
                self.stations.remove(station)
                return True
        return False

    def get_stations(self) -> list:
        return self.stations

    def count(self) -> int:
        return len(self.stations)

    def current(self) -> RadioStation:
        if self.valid():
            return self.stations[self.counter]
        else:
            raise IndexError("Counter is out of bounds")

    def key(self) -> int:
        return self.counter

    def next(self) -> None:
        self.counter += 1

    def rewind(self) -> None:
        self.counter = 0

    def valid(self) -> bool:
        return self.counter < len(self.stations)

if __name__ == "__main__":
    stations_list = StationList()
    stations_list.add_station(RadioStation(98))
    stations_list.add_station(RadioStation(101))
    stations_list.add_station(RadioStation(102))
    stations_list.add_station(RadioStation(103.2))

    for station in stations_list.get_stations():
        print(station.get_frequency())

    if stations_list.remove_station(98):
        print("Station removed")
    else:
        print("The station doesn't exist")

    for station in stations_list.get_stations():
        print(station.get_frequency())
