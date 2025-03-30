
# A hypixel bedwars stat tracker.

A python side-project to track statstics of users in your games.

  ![Image](https://github.com/user-attachments/assets/24e2e55f-8909-4cdf-a88b-fee89eef747c)
<p align="center">  
  Example of stat tracking in a bedwars game.
</p>

## Features

* Get stats in your current lobby
* Get stats in a guild

## Installation & Configuration

git clone https://github.com/madil-o/Lobby-statistic-tracker
cd Bw_Stat_Tracker/src/
python3 launch.py

Then enter your hypixel token. You can set your latest.log file directory by hand changing the log_path value in the settings.conf file if your minecraft configuration isn't available.

* You can get your token by running /token on the hypixel server.

* If your minecraft configuration (system, launcher) isn't avaible, please let me know by opening an issue. You can set your latest.log file directory by hand changing the log_path value in the settings.conf file.

## Usage

### Commands

To list players stats in your lobby, run /who in game, then type in your Bw_Stat_Tracker/src/ directory:
python3 main.py -l

To list players stats in a guild, please run:
python3 main.py -g "Guild name"

### Responses types

* Already Loaded: API wont respond because this name has been recently searched.
* No stats: The player has stats missing (no wins for example).
* Nicked: The player name has not been found: he is nicked.
