from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    def drive(self, kilometers):
        self.kilometers = kilometers
        fuel_needed = self.kilometers * self.fuel_consumption
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
