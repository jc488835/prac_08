from car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """creat a new number and compare with reliability"""
        random_number = random.randint(0, 100)
        print(random_number)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            print("Your car is unreliable")
