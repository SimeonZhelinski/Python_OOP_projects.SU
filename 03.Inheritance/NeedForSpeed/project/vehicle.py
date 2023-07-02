class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption: float = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        self.kilometers = kilometers
        fuel_needed = self.kilometers * self.fuel_consumption
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
