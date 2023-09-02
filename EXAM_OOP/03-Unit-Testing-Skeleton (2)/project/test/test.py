from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def test_object_init(self):
        car = SecondHandCar("Corolla", "car", 150, 1000)
        self.assertEqual("Corolla", car.model)
        self.assertEqual("car", car.car_type)
        self.assertEqual(150, car.mileage)
        self.assertEqual(1000, car.price)
        self.assertEqual([], car.repairs)

    def test_price_setter_error(self):
        with self.assertRaises(ValueError) as valer:
            car = SecondHandCar("Corolla", "car", 150, 1)

        self.assertEqual("Price should be greater than 1.0!", str(valer.exception))

    def test_mileage_setter_error(self):
        with self.assertRaises(ValueError) as valer:
            car = SecondHandCar("Corolla", "car", 100, 1000)

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(valer.exception))

    def test_set_promotional_price_error(self):
        car = SecondHandCar("Corolla", "car", 150, 1000)
        with self.assertRaises(ValueError) as valer:
            car.set_promotional_price(1000)

        self.assertEqual("You are supposed to decrease the price!", str(valer.exception))

    def test_set_promotional_price(self):
        car = SecondHandCar("Corolla", "car", 150, 1000)

        self.assertEqual("The promotional price has been successfully set.", car.set_promotional_price(999))
        self.assertEqual(999, car.price)

    def test_need_repair_repair_price_more_than_car_price(self):
        car = SecondHandCar("Corolla", "car", 150, 1000)

        self.assertEqual("Repair is impossible!", car.need_repair(501, "engine"))

    def test_need_repair_repair_success(self):
        car = SecondHandCar("Corolla", "car", 150, 1000)

        self.assertEqual(1000, car.price)
        self.assertEqual([], car.repairs)
        self.assertEqual("Price has been increased due to repair charges.", car.need_repair(500, "two doors"))
        self.assertEqual(1500, car.price)
        self.assertEqual(["two doors"], car.repairs)

    def test_other_mismatch(self):
        car = SecondHandCar("Corolla", "car", 150, 1000)
        other_car = SecondHandCar("Jumper", "van", 200, 2000)

        self.assertEqual("Cars cannot be compared. Type mismatch!", car.__gt__(other_car))

    def test_other_car_cheaper(self):
        car = SecondHandCar("Corolla", "car", 150, 1000)
        other_car = SecondHandCar("Yaris", "car", 200, 900)

        self.assertEqual(True, car.__gt__(other_car))

    def test_other_car_equal(self):
        car = SecondHandCar("Corolla", "car", 150, 1000)
        other_car = SecondHandCar("Yaris", "car", 200, 1000)

        self.assertEqual(False, car.__gt__(other_car))

    def test_other_car_more_exp(self):
        car = SecondHandCar("Corolla", "car", 150, 1000)
        other_car = SecondHandCar("Yaris", "car", 200, 1100)

        self.assertEqual(False, car.__gt__(other_car))

    def test_str_method(self):
        car = SecondHandCar("Corolla", "car", 150, 1000)

        self.assertEqual("""Model Corolla | Type car | Milage 150km
Current price: 1000.00 | Number of Repairs: 0""", car.__str__())


if __name__ == "__main__":
    main()
