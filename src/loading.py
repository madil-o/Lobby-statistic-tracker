
import configparser
import json

from type import *


def param_loading(to_load: str) -> dict:
    """Load user's parameters."""
    config = configparser.ConfigParser()
    config.read("settings.conf")
    return config["PLAYER"][to_load]


def temp_load() -> list[Player_stats, ...]:
    """Load stats from temp file."""
    return json.loads(open("/tmp/bw_stats.txt", r))["stats"]

def temp_dmp(stats: list[Player_stats, ...]) -> FileWriting:
    """Dump players stats in temporary json file."""
    stats = temp_load()
    
        