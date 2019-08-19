class Location:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Trip:
    def __init__(self):
        self.stops = []

    def add_location(self, stop):
        self.stops.append(stop)

    def begin_trip(self):
        print('Began Trip')
        for i in range(len(self.stops)-1):
            print(f'Travelled from {self.stops[i]} to {self.stops[i+1]}')
        print('Ended Trip')


first_trip = Trip()
toronto = Location('Toronto')
ottowa = Location('Ottawa')
montreal = Location('Montreal')
quebec_city = Location('Quebec City')
halifax = Location('Halifax')
st_john = Location('St. John\'s')

first_trip.add_location(toronto)
first_trip.add_location(ottowa)
first_trip.add_location(montreal)
first_trip.add_location(quebec_city)
first_trip.add_location(halifax)
first_trip.add_location(st_john)

print(first_trip.stops[0])
first_trip.begin_trip()