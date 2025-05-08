# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self._power = power  # Encapsulated attribute
        self.origin = origin

    def show_identity(self):
        print(f"I am {self.name} from {self.origin}.")

    def use_power(self):
        print(f"{self.name} uses {self._power}!")

# Subclass (Inheritance)
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} soars through the skies at {self.flight_speed} km/h!")

# Creating objects
hero1 = Superhero("Red boy", "Fire style", "fire village")
hero2 = FlyingHero("Air boy", "Wind style", "cloud village", 800)

# Using methods
hero1.show_identity()
hero1.use_power()
print("---")
hero2.show_identity()
hero2.use_power()
