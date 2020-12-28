[![Python supported versions](https://img.shields.io/pypi/pyversions/scrapy?style=for-the-badge)](https://www.python.org/) 
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge)](http://perso.crans.org/besson/LICENSE.html) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](https://github.com/sauravhiremath/fifa-api/issues)


# Football Players Statistics WebCrawler

This project is a sub-module for [Multiplayer Football Draft Simulator](https://github.com/sauravhiremath/fifa).

# About

A web-crawler to scrape all football players' information from [Sofifa](https://sofifa.com/players) and exporting it to JSON format. Perform data cleaning and analytics on the obtained data

- Crawler: Built on scrapy using python3
- Analytics: IPynb noteboook python3

Further exported to the [Football Draft Backend](https://github.com/sauravhiremath/fifa-api) to serve from an endpoint

# Steps to run the project

## Easy Run

```
chmod +x ./run.sh
./run.sh
```

## Manual Setup and Run

- Setup virtualenv (optional, but recommended)
  ```
  virtualenv -p python3.8 env
  source env/bin/activate
  ```
- Install project dependencies <br>

  ```python
  pip install -r requirements.txt
  ```

- Run the crawler with _./fifa-crawler_ as current directory (This the main scrapy crawler directory)
  ```
  cd fifa_crawler
  ```

- First run the URL spider (To get all players urls)
  ```bash
  scrapy crawl players_urls
  ```

- After successfull, run the stats spider (To get the players statistics from URLs from above)
  ```bash
  scrapy crawl players_stats
  ```

# Scope/Aim as an indiviual project

- Update the crawler periodically to reflect changes on [Sofifa platform](https://sofifa.com/players).

# Future features

- Add analysis projects on the crawled data.
- Update the crawler to perform scraping to obtain _Teams_ data (currently player-data)
- Improve speed of the crawler

# Metadata

<details>
  <summary>Click here to expand meta view, or <a href="https://github.com/sauravhiremath/fifa-stats-crawler/blob/master/data/meta/meta.md">go-here</a> for a detailed view</summary>

  <details>
  <summary>id</summary>

  * **type**: string

  * **example**: "158023"
  </details>

  <details>
  <summary>name</summary>

  * **type**: string

  * **example**: "Lionel Andrés Messi Cuccittini"
  </details>

  <details>
  <summary>short_name</summary>

  * **type**: string

  * **example**: "L. Messi"
  </details>

  <details>
  <summary>photo_url</summary>

  * **type**: string

  * **example**: "https://cdn.sofifa.com/players/158/023/21_120.png"
  </details>

  <details>
  <summary>primary_position</summary>

  * **type**: string

  * **example**: "RW"
  </details>

  <details>
  <summary>positions</summary>

  * **type**: string[]

  * **example**: ["RW", "ST", "CF"]
  </details>

  <details>
  <summary>age</summary>

  * **type**: string

  * **example**: "33"
  </details>

  <details>
  <summary>birth_date</summary>

  * **type**: string (DateFormat is `YYYY/MONTH_NAME_SHORT/DD`)

  * **example**: "1987/Jun/24"
  </details>

  <details>
  <summary>height</summary>

  * **type**: integer (in cms)

  * **example**: 170
  </details>

  <details>
  <summary>weight</summary>

  * **type**: integer (in kg)

  * **example**: 72
  </details>

  <details>
  <summary>Overall Rating</summary>

  * **type**: integer

  * **example**: 93
  </details>

  <details>
  <summary>Potential</summary>

  * **type**: integer

  * **example**: 93
  </details>

  <details>
  <summary>Value</summary>

  * **type**: string (in euros)

  * **example**: "€103.5M"
  </details>

  <details>
  <summary>Wage</summary>

  * **type**: string (in euros)

  * **example**: "€560K"
  </details>

  <details>
  <summary>Preferred Foot</summary>

  * **type**: enum["Left", "Right"]

  * **example**: "Left"
  </details>

  <details>
  <summary>Weak Foot</summary>

  * **type**: integer (range 1-5)

  * **example**: 4
  </details>

  <details>
  <summary>Skill Moves</summary>

  * **type**: integer (range 1-5)

  * **example**: 4
  </details>

  <details>
  <summary>International Reputation</summary>

  * **type**: integer (range 0-5)

  * **example**: 5
  </details>

  <details>
  <summary>Work Rate</summary>

  * **type**: enum["Medium/Low"]

  * **example**: "Medium/Low"
  </details>

  <details>
  <summary>Body Type</summary>

  * **type**: enum["Unique", "Normal (170-185)", "Normal (185+)", "Lean (170-185)", "Lean (185+)", "Stocky (170-185)", "Normal (170-)", "Stocky (185+)", "Stocky (185+)", "Stocky (170-)", ]

  * **example**: "Unique"
  </details>

  <details>
  <summary>Real Face</summary>

  * **type**: enum["Yes", "No"]

  * **example**: "Yes"
  </details>

  <details>
  <summary>Release Clause</summary>

  * **type**: string (in euros)

  * **example**: "€212.2M"
  </details>

  <details>
  <summary>teams</summary>

  * **type**: map<string, integer> (including international and domestic clubs)

  * **example**: 
  ```json
  {
  "FC Barcelona": 84,
  "Argentina": 83
  }
  ```
  </details>

  <details>
  <summary>attacking</summary>

  * **type**: map<attackOptions, integer>

  <details>
  <summary>attackOptions</summary>

  * **type**: enum["Crossing", "Finishing", "HeadingAccuracy", "ShortPassing", "Volleys"]
  </details>

  * **example**: 
  ```json
  {
      "Crossing": 85,
      "Finishing": 95,
      "HeadingAccuracy": 70,
      "ShortPassing": 91,
      "Volleys": 88
  }
  ```
  </details>

  <details>
  <summary>skill</summary>

  * **type**: map<skillOptions, integer>
  <details>
  <summary>skillOptions</summary>

  * **type**: enum["Dribbling", "Curve", "FKAccuracy", "LongPassing", "BallControl"]
  </details>

  * **example**: 
  ```json
  {
      "Dribbling": 96,
      "Curve": 93,
      "FKAccuracy": 94,
      "LongPassing": 91,
      "BallControl": 96
  }
  ```
  </details>

  <details>
  <summary>movement</summary>

  * **type**: map<movementOptions, integer>

  <details>
  <summary>movementOptions</summary>

  * **type**: enum["Acceleration", "SprintSpeed", "Agility", "Reactions", "Balance"]
  </details>

  * **example**: 
  ```json
  {
      "Acceleration": 91,
      "SprintSpeed": 80,
      "Agility": 91,
      "Reactions": 94,
      "Balance": 95
  }
  ```
  </details>

  <details>
  <summary>power</summary>

  * **type**: map<powerOptions, integer>

  <details>
  <summary>powerOptions</summary>

  * **type**: enum["ShotPower", "Jumping", "Stamina", "Strength", "LongShots"]
  </details>

  * **example**: 
  ```json
  {
      "ShotPower": 86,
      "Jumping": 68,
      "Stamina": 72,
      "Strength": 69,
      "LongShots": 94
  }
  ```
  </details>

  <details>
  <summary>mentality</summary>

  * **type**: map<mentalityOptions, integer>

  <details>
  <summary>mentalityOptions</summary>

  * **type**: enum["Aggression", "Interceptions", "Positioning", "Vision", "Penalties", "Composure"]
  </details>

  * **example**: 
  ```json
  {
      "Aggression": 44,
      "Interceptions": 40,
      "Positioning": 93,
      "Vision": 95,
      "Penalties": 75,
      "Composure": 96
  }
  ```
  </details>

  <details>
  <summary>defending</summary>

  * **type**: map<defendingOptions, integer>

  <details>
  <summary>defendingOptions</summary>

  * **type**: enum["DefensiveAwareness", "StandingTackle", "SlidingTackle"]
  </details>

  * **example**: 
  ```json
  {
      "DefensiveAwareness": 32,
      "StandingTackle": 35,
      "SlidingTackle": 24
  }
  ```
  </details>

  <details>
  <summary>goalkeeping</summary>

  * **type**: map<goalkeepingOptions, integer>

  <details>
  <summary>goalkeepingOptions</summary>

  * **type**: enum["GKDiving", "GKHandling", "GKKicking", "GKPositioning", "GKReflexes"]
  </details>

  * **example**: 
  ```json
  {
      "GKDiving": 6,
      "GKHandling": 11,
      "GKKicking": 15,
      "GKPositioning": 14,
      "GKReflexes": 8
  }
  ```
  </details>

  <details>
  <summary>player_traits</summary>

  * **type**: string["Technical Dribbler (AI)","Long Shot Taker (AI)","Flair","Speed Dribbler (AI)","Injury Prone","Long Passer (AI)","Playmaker (AI)","Power Header","Dives Into Tackles (AI)","Outside Foot Shot","Team Player","Finesse Shot","Leadership","Solid Player","Early Crosser","Long Throw-in","Comes For Crosses","Power Free-Kick","GK Long Throw","Cautious With Crosses","Rushes Out Of Goal","Saves with Feet","Chip Shot (AI)","Giant Throw-in","One Club Player"]

  * **example**: 
  ```json
  [
      "Finesse Shot",
      "Long Shot Taker (AI)",
      "Speed Dribbler (AI)",
      "Playmaker (AI)",
      "Outside Foot Shot",
      "One Club Player",
      "Team Player",
      "Chip Shot (AI)"
  ]
  ```
  </details>

  <details>
  <summary>player_hashtags</summary>

  * **type**: string["#Strength","#Acrobat","#Engine","#Speedster","#Dribbler","#Aerial Threat","#Tactician","#FK Specialist","#Crosser","#Distance Shooter","#Clinical Finisher","#Playmaker","#Tackling","#Complete Midfielder","#Complete Forward","#Poacher","#Complete Defender"] (Each tag starts with `#`)

  **example**:
  ```json
  [
      "#Dribbler",
      "#Distance Shooter",
      "#FK Specialist",
      "#Acrobat",
      "#Clinical Finisher",
      "#Complete Forward"
  ]
  ```
  </details>

  <details>
  <summary>logos</summary>

  * **type**: map<groupNames, logoAttributes>

  <details>
  <summary>groupNames</summary>

  * **type**: enum["country", "club", "nationalClub"]
  </details>

  <details>
  <summary>logoAttributes</summary>

  * **type**: map<enum["name", "url"], string>

  * **logoAttributes examples**:
  ```json
  {
      "name": "Argentina",
      "url": "https://cdn.sofifa.com/flags/ar.png"
  }
  ```
  </details>

  * **examples**:
  ```json
  {
      "country": {
      "name": "Argentina",
      "url": "https://cdn.sofifa.com/flags/ar.png"
      },
      "club": {
      "name": "FC Barcelona",
      "url": "https://cdn.sofifa.com/teams/241/60.png"
      },
      "nationalClub": {
      "name": "Argentina",
      "url": "https://cdn.sofifa.com/teams/1369/60.png"
      }
  }
  ```
  </details>
</details>

# Contributing tot the Project

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features

## Making a PR

- Fork the repo and clone it on your machine.
- Add a upstream link to main branch in your cloned repo

  ```
   git remote add https://github.com/sauravhiremath/fifa-stats-crawler.git

  ```

- Keep your cloned repo upto date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)

  ```
  git pull upstream master
  ```

- Create your feature branch
  ```
  git checkout -b <feature-name>
  ```
- Commit all the changes
  ```
  git commit -am "Meaningful commit message"
  ```
- Push the changes for review
  ```
  git push origin <branch-name>
  ```
- Create a PR from our repo on Github.

### Additional Notes

- Code should be properly commented to ensure it's readability.
- If you've added code that should be tested, add tests as comments.
- In python use docstrings to provide tests.
- Make sure your code properly formatted.
- Issue that pull request!

## Issue suggestions/Bug reporting

When you are creating an issue, make sure it's not already present. Furthermore, provide a proper description of the changes. If you are suggesting any code improvements, provide through details about the improvements.

**Great Issue suggestions** tend to have:

- A quick summary of the changes.
- In case of any bug provide steps to reproduce
  - Be specific!
  - Give sample code if you can.
  - What you expected would happen
  - What actually happens
  - Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

### Additional References:

More step by step guide with pictures for creating a pull request can be found [here](https://opensource.com/article/19/7/create-pull-request-github)
