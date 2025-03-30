
import os
import re

from loading import *


def get_in_lobby() -> list[str, ...]:
    """Get list of all players in lobby after /who."""
    logs = open(param_loading("log_path")).read()
    return logs_to_player(logs), "name"


def lst_after_x(lst: list[str, ...],
                element: str) -> list[str, ...]:
    """Return list after a given element."""
    index = [pos for pos, string in enumerate(lst) if string == element][-1]
    return lst[(index + 1):]


def logs_to_player(text: str) -> list[str, ...]:
    """Get all the players in the lobby."""
    players = (lst_after_x(re.findall(
        ".*\[CHAT] ONLINE: (.+, .*)|Sending you to.*", text), "")[-1]).split(", ")
    return players
