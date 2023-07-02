from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def drive(self, kilometers):
        self.kilometers = kilometers
        fuel_needed = self.kilometers * self.fuel_consumption
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed