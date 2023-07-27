from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def test_object_init(self):
        mammal = Mammal("Ben", "Lion", "arrr")
        self.assertEqual("Ben", mammal.name)
        self.assertEqual("Lion", mammal.type)
        self.assertEqual("arrr", mammal.sound)

    def test_make_sound(self):
        mammal = Mammal("Ben", "Lion", "arrr")
        self.assertEqual("Ben makes arrr", mammal.make_sound())

    def test_get_kingdom(self):
        mammal = Mammal("Ben", "Lion", "arrr")
        self.assertEqual("animals", mammal.get_kingdom())

    def test_info(self):
        mammal = Mammal("Ben", "Lion", "arrr")
        self.assertEqual("Ben is of type Lion", mammal.info())


if __name__ == "__main__":
    main()
