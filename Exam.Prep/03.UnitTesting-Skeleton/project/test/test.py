from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def test_object_init(self):
        movie = Movie("Mario", 1988, 10)

        self.assertEqual("Mario", movie.name)
        self.assertEqual(1988, movie.year)
        self.assertEqual(10, movie.rating)
        self.assertEqual([], movie.actors)

    def test_name_error(self):
        with self.assertRaises(ValueError) as valer:
            movie = Movie("", 1988, 10)

        self.assertEqual("Name cannot be an empty string!", str(valer.exception))

    def test_year_error(self):
        with self.assertRaises(ValueError) as valer:
            movie = Movie("Mario", 1886, 10)

        self.assertEqual("Year is not valid!", str(valer.exception))

    def test_adding_actor_not_in_list(self):
        movie = Movie("Mario", 1988, 10)
        movie.add_actor("Simo")
        movie.add_actor("Eti")

        self.assertEqual(["Simo", "Eti"], movie.actors)

    def test_adding_actor_not_not_in_list(self):
        movie = Movie("Mario", 1988, 10)
        movie.add_actor("Simo")

        self.assertEqual(["Simo"], movie.actors)
        self.assertEqual("Simo is already added in the list of actors!", movie.add_actor("Simo"))
        self.assertEqual(["Simo"], movie.actors)

    def test_self_movie_is_better(self):
        movie = Movie("Mario", 1988, 10)
        other_movie = Movie("Ben10", 1989, 9)

        self.assertEqual('"Mario" is better than "Ben10"', movie.__gt__(other_movie))

    def test_self_movie_is_worse(self):
        movie = Movie("Mario", 1988, 9)
        other_movie = Movie("Ben10", 1989, 10)

        self.assertEqual('"Ben10" is better than "Mario"', movie.__gt__(other_movie))

    def test_representation(self):
        movie = Movie("Mario", 1988, 9.987)
        movie.add_actor("Simo")
        movie.add_actor("Eti")

        self.assertEqual(f"Name: Mario\n"
                         f"Year of Release: 1988\n"
                         f"Rating: 9.99\n"
                         f"Cast: Simo, Eti", movie.__repr__())


if __name__ == "__main__":
    main()
