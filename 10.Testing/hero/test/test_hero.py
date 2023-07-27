from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def test_hero_init(self):
        hero = Hero("Marauder", 10, 99.1, 10.1)
        self.assertEqual("Marauder", hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual(99.1, hero.health)
        self.assertEqual(10.1, hero.damage)

    def test_battle_same_name_error(self):
        hero = Hero("Marauder", 10, 99.1, 10.1)
        enemy_hero = Hero("Marauder", 10, 99.1, 10.1)

        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_no_health_error(self):
        hero = Hero("Marauder", 10, 0, 10.1)
        enemy_hero = Hero("Ben10", 8, 88.1, 5.1)

        with self.assertRaises(ValueError) as valer:
            hero.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(valer.exception))

    def test_battle_enemy_no_health_error(self):
        hero = Hero("Marauder", 10, 99.1, 10.1)
        enemy_hero = Hero("Ben10", 8, 0, 5.1)

        with self.assertRaises(ValueError) as valer:
            hero.battle(enemy_hero)

        self.assertEqual("You cannot fight Ben10. He needs to rest", str(valer.exception))

    def test_battle_draw(self):
        hero = Hero("Marauder", 10, 99, 10.1)
        enemy_hero = Hero("Ben10", 10, 101, 10.1)

        result = hero.battle(enemy_hero)

        self.assertEqual(-2.0, hero.health)
        self.assertEqual(0, enemy_hero.health)
        self.assertEqual("Draw", result)

    def test_battle_win(self):
        hero = Hero("Marauder", 10, 150, 10.1)
        enemy_hero = Hero("Ben10", 10, 50, 10.1)

        result = hero.battle(enemy_hero)

        self.assertEqual(54, hero.health)
        self.assertEqual(15.1, hero.damage)
        self.assertEqual(11, hero.level)
        self.assertEqual(-51, enemy_hero.health)
        self.assertEqual("You win", result)

    def test_battle_lost(self):
        hero = Hero("Marauder", 10, 50, 10.1)
        enemy_hero = Hero("Ben10", 10, 150, 10.1)

        result = hero.battle(enemy_hero)

        self.assertEqual(54, enemy_hero.health)
        self.assertEqual(15.1, enemy_hero.damage)
        self.assertEqual(11, enemy_hero.level)
        self.assertEqual(-51, hero.health)
        self.assertEqual("You lose", result)

    def test_str(self):
        hero = Hero("Marauder", 10, 50, 10.1)
        self.assertEqual(f"Hero Marauder: 10 lvl\n"
                         f"Health: 50\n"
                         f"Damage: 10.1\n", hero.__str__())


if __name__ == "__main__":
    main()
