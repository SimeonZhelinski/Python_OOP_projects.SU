from project.player import Player
from typing import List


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        try:
            player_kick = next(filter(lambda p: p.name == player_name, self.players))

        except StopIteration:
            return f"Player {player_name} is not in the guild."

        self.players.remove(player_kick)
        player_kick.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        player_guild_info = "\n".join([p.player_info() for p in self.players])

        return f"Guild: {self.name}\n" + \
            f"{player_guild_info}"
