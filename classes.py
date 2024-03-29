class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(10,12)
print(p.x, p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["a","v", "d", "e"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} successfully")
    else:
        print(f"Cannot add {person}")


print(flight.passengers)
#print(flight.open_seats)
