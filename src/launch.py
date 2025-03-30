
import configparser
import os
import sys

from type import *


class Launch:
    @property
    def key(self) -> str:
        """Get user's API key."""
        return input("Please paste your API key:\n")

    @property
    def pre_path(self) -> str:
        """Get pre-minecraft user path."""
        if sys.platform == "linux":
            return os.environ["HOME"], "/"
        elif sys.platform == "win32":
            return "{}\\AppData\\Roaming".format(os.environ["USERPROFILE"]), "\\"

    def get_log_path(self, sys_info: str) -> str:
        """Get user's log path."""
        pre_path, sep = sys_info
        logs_path = {1: ("[1] Vanilla/Forge", "{}.minecraft{}logs{}".format(*[sep for i in range(3)])),
                     2: ("[2] LunarClient", "{}.lunarclient{}offline{}1.8{}logs{}".format(*[sep for k in range(5)]))}
        print("What minecraft client do you use ?")
        for client in logs_path.items():
            print(client[1][0])

        return pre_path + logs_path[int(input())][1] + "latest.log"

    def dump_config(self) -> FileWriting:
        """Dump user configuration to a file."""
        config = configparser.ConfigParser()
        config['PLAYER'] = {"API_key": self.key,
                            "Log_path": self.get_log_path(self.pre_path),
                            "Spaces_lenght": 20}

        with open("settings.conf", "w") as configfile:
            config.write(configfile)


if __name__ == "__main__":
    Launch().dump_config()
