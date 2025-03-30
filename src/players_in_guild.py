
import requests
import json


class In_guild:
    def __init__(self, token: str, guild_name: str):
        self.token = token
        self.guild_name = guild_name

    @property
    def raw_guild(self):
        """Get raw guild json."""
        return dict(requests.get("https://api.hypixel.net/guild?key={}&name={}".format(self.token, self.guild_name)).json())["guild"]["members"]

    def get_player_lst(self, stats: dict[str, ...]) -> list[str, ...]:
        """Get all players uuid."""
        return [stat["uuid"] for stat in stats]

    def get_in_guild(self) -> list[list[str, ...], str]:
        """Get all players uuid in a guild."""
        return self.get_player_lst(self.raw_guild), "uuid"
