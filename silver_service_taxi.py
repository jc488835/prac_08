from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness

    def __str__(self):
        """Return a string of a Car's details and fare."""
        return "{}, fuel={}, odo={}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(
            self.name, self.fuel, self.odometer, self.current_fare_distance, self.new_fare(), self.flagfall)

    def new_fare(self):
        return self.price_per_km * self.fanciness

    def get_fare(self):
        """ fare need to multiply by faciness"""
        return self.flagfall + super().get_fare() * self.fanciness
