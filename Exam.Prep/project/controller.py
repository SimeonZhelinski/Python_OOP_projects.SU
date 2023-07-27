from supply.food import Food
from supply.drink import Drink
from player import Player
from supply.supply import Supply
from typing import List


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies = List[Supply] = []

    def add_player(self, player: Player):
        if player not in self.players:
            self.players.append(player)

