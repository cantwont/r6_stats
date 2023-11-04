# R6_Stats

Easily grab player stats for the game Rainbow 6: Siege
https://pypi.org/project/r6-stats/

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Getting Started

R6_Stats is a simple Python package aimed to get player stats for any platform in just a simple function. This project is still a work-in-progress (WiP) so expect bugs. Please open an issue so I can fix any errors!

## Prerequisites

```bash
pip install requests
pip install beautifulsoup4
pip install lxml
```

## Installation

This will be shortened in the future as I still have some debugging to do

```bash
pip install -i https://test.pypi.org/simple/ r6-stats
```
## Usage
```py
from r6_stats import *

platform = 'pc'
username = 'Spoit.M80'

print(get_profile_views(platform, username))
# 2833937


print(get_profile_level(platform, username))
# 522


print(get_season_info(platform, username))
# {'Heavy Mettle': {'MMR': '2,131', 'Matches': 'Matches 28', 'KD': 'K/D 0.80'}}
# (Spoit's season info was too long so I used mine 😂)


print(get_rank_image('CHAMPION'))
# https://imgur.com/Q5Qpcmt.png


print(get_general_stats(platform, username))
# {
#     "Headshot %": "61%",
#     "K/D": "1.73",
#     "Kills": "90,635",
#     "Deaths": "52,242",
#     "Wins": "10,332",
#     "Losses": "2,856",
#     "Win %": "74.4%",
#     "Time Played": "3,897h",
#     "Matches Played": "13,882",
#     "Player Level": "522",
# }


print(get_ranked_stats(platform, username))
# {
#     "Time Played": "3,551h 57m 9s",
#     "Wins": "9,212",
#     "Losses": "2,500",
#     "Matches Played": "11,718",
#     "Deaths": "46,482",
#     "Kills": "78,303",
#     "Win %": "78.6%",
#     "K/D": "1.68",
#     "Kills/Match": "6.68",
#     "Kills/Min": "0.37",
#     "Current Rank": "CHAMPION",
#     "Player Level": "522",
# }
