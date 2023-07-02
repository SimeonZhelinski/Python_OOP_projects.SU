from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def drive(self, kilometers):
        self.kilometers = kilometers
        fuel_needed = self.kilometers * self.fuel_consumption
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed