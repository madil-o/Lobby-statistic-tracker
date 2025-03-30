
import os

from type import *


class Display:
    def __init__(self, stats: list[Player_stats], space: int):
        self.stats = stats
        self.space = space

    def fkdr_pos(self, player: list[str, ...]) -> float:
        """Return stats third position"""
        return player[3]

    @property
    def fkdr_sorting(self) -> list[Player_stats, ...]:
        """Sort players by fkdr."""
        unknown = [player for player in self.stats if not isinstance(player[3], float)]
        known = [real for real in self.stats if real not in unknown]
        known.sort(reverse=True, key=self.fkdr_pos)

        return unknown + known

    def display_stats(self) -> ConsoleEffect:
        """Display players stats."""
        players = [("Name", "Stars", "Wins", "fkdr")] + self.fkdr_sorting
        for player in players:
            to_print = ""
            for stat in player:
                to_print += str(stat) + " "*(self.space - len(str(stat)))
            print(to_print)
