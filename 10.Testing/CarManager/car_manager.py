class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


from unittest import TestCase, main


class TestCar(TestCase):

    def test_object_constructor(self):
        car = Car("Skoda", "Kodiaq", 5, 60)
        self.assertEqual("Skoda", car.make)
        self.assertEqual("Kodiaq", car.model)
        self.assertEqual(5, car.fuel_consumption)
        self.assertEqual(60, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_make_setter(self):
        car = Car("Skoda", "Kodiaq", 5, 60)
        car.make = "VW"
        self.assertEqual("VW", car.make)

    def test_make_setter_error(self):
        car = Car("Skoda", "Kodiaq", 5, 60)

        with self.assertRaises(Exception) as ex:
            car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.make = None

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter(self):
        car = Car("Skoda", "Kodiaq", 5, 60)
        car.model = "Golf"
        self.assertEqual("Golf", car.model)

    def test_model_setter_error(self):
        car = Car("Skoda", "Kodiaq", 5, 60)

        with self.assertRaises(Exception) as ex:
            car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.model = None

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter(self):
        car = Car("Skoda", "Kodiaq", 5, 60)
        car.fuel_consumption = 7
        self.assertEqual(7, car.fuel_consumption)

    def test_fuel_consumption_setter_error(self):
        car = Car("Skoda", "Kodiaq", 5, 60)

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter(self):
        car = Car("Skoda", "Kodiaq", 5, 60)
        car.fuel_capacity = 70
        self.assertEqual(70, car.fuel_capacity)

    def test_fuel_capacity_setter_error(self):
        car = Car("Skoda", "Kodiaq", 5, 60)

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = -10

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_setter(self):
        car = Car("Skoda", "Kodiaq", 5, 60)
        self.assertEqual(0, car.fuel_amount)
        car.fuel_amount = 30
        self.assertEqual(30, car.fuel_amount)

    def test_fuel_setter_error(self):
        car = Car("Skoda", "Kodiaq", 5, 60)
        self.assertEqual(0, car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -10

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_error(self):
        car = Car("Skoda", "Kodiaq", 5, 60)

        with self.assertRaises(Exception) as ex:
            car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_not_by_limit_capacity(self):
        car = Car("Skoda", "Kodiaq", 5, 60)
        car.fuel_amount = 30
        car.refuel(10)
        self.assertEqual(40, car.fuel_amount)

        car.fuel_amount = 60
        car.refuel(1)
        self.assertEqual(60, car.fuel_amount)

    def test_distance_error(self):
        car = Car("Skoda", "Kodiaq", 5, 60)

        with self.assertRaises(Exception) as ex:
            car.fuel_amount = 49
            car.drive(1000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_distance_drive(self):
        car = Car("Skoda", "Kodiaq", 5, 60)
        car.fuel_amount = 50
        car.drive(1000)
        self.assertEqual(0, car.fuel_amount)


if __name__ == "__main__":
    main()
