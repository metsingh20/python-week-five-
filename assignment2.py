class Vehicle:
    def move(self):
        pass  # Abstract method placeholder

class Car(Vehicle):
    def move(self):
        print("Car...Driving ")

class Plane(Vehicle):
    def move(self):
        print("Plane...Flying ")

class Boat(Vehicle):
    def move(self):
        print("Ship...Sailing ")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
