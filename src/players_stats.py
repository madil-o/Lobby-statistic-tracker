
import requests
import json

from loading import *
from type import *


API_ERROR_CAUSES = {
    "You have already looked up this name recently": "Already loaded"}


class Stats:
    def __init__(self, token: str, players_info: list[list[str, ...], str]):
        self.token = token
        self.players, self.name_type = players_info

    def player_lst_stats(self) -> Player_stats:
        """Get list of all listed players stat"""
        return [self.get_stats(self.get_raw_stats(player), player, n, len(self.players)) for n, player in enumerate(self.players)]

    def get_raw_stats(self, player_name: str) -> dict:
        """Get raw json file text according to player name."""
        return dict(requests.get("https://api.hypixel.net/player?key={}&{}={}".format(self.token, self.name_type, player_name)).json())

    def get_stats(self,
                  stats: dict[str, ...],
                  name: str,
                  pos: int,
                  total: int) -> Player_stats:
        """Returns a stat dictionary with usefull stats"""
        print("Loaded {}/{} players".format((pos + 1), total))
        try:
            bw_stats = stats["player"]["stats"]["Bedwars"]
            return (stats["player"]["playername"],
                    round(bw_stats["Experience"]/5000),
                    bw_stats["wins_bedwars"],
                    round(bw_stats["final_kills_bedwars"]/bw_stats["final_deaths_bedwars"], 2))

        except (IndexError, TypeError, KeyError):
            if stats["success"]:
                if stats["player"]:
                    return (name, "No Stats", "No Stats", "No Stats")
                else:
                    return (name, "Nicked", "Nicked", "Nicked")
            else:
                error = API_ERROR_CAUSES[stats["cause"]]
                return (name, error, error, error)
