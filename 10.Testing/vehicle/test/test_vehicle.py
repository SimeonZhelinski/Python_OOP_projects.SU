from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def test_object_init(self):
        vehicle = Vehicle(55.6, 150.6)
        self.assertEqual(55.6, vehicle.fuel)
        self.assertEqual(150.6, vehicle.horse_power)
        self.assertEqual(55.6, vehicle.capacity)
        self.assertEqual(1.25, vehicle.fuel_consumption)

    def test_drive_ok(self):
        vehicle = Vehicle(55.6, 150.6)
        vehicle.drive(20)
        self.assertEqual(30.6, vehicle.fuel)

    def test_drive_error(self):
        vehicle = Vehicle(55.6, 150.6)

        with self.assertRaises(Exception) as ex:
            vehicle.drive(50)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_ok(self):
        vehicle = Vehicle(55.6, 150.6)
        vehicle.drive(20)
        vehicle.refuel(10)
        self.assertEqual(40.6, vehicle.fuel)

    def test_refuel_error(self):
        vehicle = Vehicle(55.6, 150.6)
        vehicle.drive(20)

        with self.assertRaises(Exception) as ex:
            vehicle.refuel(30)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_method(self):
        vehicle = Vehicle(55.6, 150.6)
        self.assertEqual("The vehicle has 150.6 horse power with 55.6 fuel left and 1.25 fuel consumption",
                         vehicle.__str__())


if __name__ == "__main__":
    main()
