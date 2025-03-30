
import requests
import json
import argparse

from players_in_lobby import *
from players_in_guild import *
from players_stats import *
from type import *
from display import *


def argument_parser() -> argparse.ArgumentParser:
    """Parse user line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--lobby", action='store_const', const=1)
    parser.add_argument("-g", "--guild", nargs=1)

    return parser


def main() -> ConsoleEffect:
    token = param_loading("api_key")
    to_get = argument_parser().parse_args()
    if to_get.guild:
        players = In_guild(token, to_get.guild[0]).get_in_guild()
    else:
        players = get_in_lobby()

    stats = Stats(token, players).player_lst_stats(), int(param_loading("Spaces_lenght"))
    Display(stats).display_stats()


if __name__ == "__main__":
    main()
