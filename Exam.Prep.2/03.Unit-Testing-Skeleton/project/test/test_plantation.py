from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def test_object_init(self):
        plantation = Plantation(10)
        self.assertEqual(10, plantation.size)
        self.assertEqual({}, plantation.plants)
        self.assertEqual([], plantation.workers)

    def test_object_name_setter(self):
        with self.assertRaises(ValueError) as valer:
            plantation = Plantation(-1)

        self.assertEqual("Size must be positive number!", str(valer.exception))

    def test_hire_worker_not_in_list(self):
        plantation = Plantation(10)
        self.assertEqual([], plantation.workers)

        self.assertEqual("Ben successfully hired.", plantation.hire_worker("Ben"))
        self.assertEqual(["Ben"], plantation.workers)

    def test_hire_worker_in_list(self):
        plantation = Plantation(10)
        plantation.hire_worker("Ben")
        self.assertEqual(["Ben"], plantation.workers)

        with self.assertRaises(ValueError) as valer:
            plantation.hire_worker("Ben")

        self.assertEqual("Worker already hired!", str(valer.exception))
        self.assertEqual(["Ben"], plantation.workers)

    def test_count_of_plants(self):
        plantation = Plantation(10)
        self.assertEqual(0, plantation.__len__())

        plantation.hire_worker("Ben")
        plantation.hire_worker("Sim")
        plantation.planting("Ben", "tree")
        plantation.planting("Ben", "flower")
        plantation.planting("Sim", "grass")

        self.assertEqual(3, plantation.__len__())

    def test_planting_worker_error(self):
        plantation = Plantation(10)

        with self.assertRaises(ValueError) as valer:
            plantation.planting("Ben", "tree")

        self.assertEqual("Worker with name Ben is not hired!", str(valer.exception))

    def test_planting_size_error(self):
        plantation = Plantation(2)
        self.assertEqual(0, plantation.__len__())

        plantation.hire_worker("Ben")
        plantation.hire_worker("Sim")
        plantation.planting("Ben", "tree")
        plantation.planting("Ben", "grass")

        with self.assertRaises(ValueError) as valer:
            plantation.planting("Sim", "flower")

        self.assertEqual("The plantation is full!", str(valer.exception))

    def test_planting_worker_in_list_plant_not_first(self):
        plantation = Plantation(2)
        plantation.hire_worker("Ben")
        plantation.planting("Ben", "tree")
        self.assertEqual("Ben planted grass.", plantation.planting("Ben", "grass"))

    def test_planting_worker_in_list_plant_first(self):
        plantation = Plantation(2)
        plantation.hire_worker("Ben")
        self.assertEqual("Ben planted it's first grass.", plantation.planting("Ben", "grass"))

    def test_str_method(self):
        plantation = Plantation(10)
        plantation.hire_worker("Ben")
        plantation.hire_worker("Sim")
        plantation.planting("Ben", "tree")
        plantation.planting("Ben", "flower")
        plantation.planting("Sim", "grass")

        self.assertEqual(f"Plantation size: 10\n"
                         f"Ben, Sim\n"
                         f"Ben planted: tree, flower\n"
                         f"Sim planted: grass", plantation.__str__())

    def test_repr_method(self):
        plantation = Plantation(10)
        plantation.hire_worker("Ben")
        plantation.hire_worker("Sim")

        self.assertEqual(f"Size: 10\n"
                         f"Workers: Ben, Sim", plantation.__repr__())


if __name__ == "__main__":
    main()
