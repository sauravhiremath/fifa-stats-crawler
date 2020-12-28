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

- Setup virtualenv (optional, but recommended)
  ```
  virtualenv -p python3.6 env
  source env/bin/activate
  ```
- Install project dependencies <br>

  ```python
  pip install -r requirements.txt
  ```

- Run the crawler with _./fifa-crawler_ as current directory (This the main scrapy crawler directory)

  Make sure to change the filenames to read and write appropriately: <br/> 
  > `players_url.json` --> scraping urls <br/> 
  > `players_stats_raw.json` --> scraping player stats

  - First run the URL spider (To get all players urls)
    ```python
    scrapy crawl players_url
    ```
  - After successfull, run the stats spider (To get the players statistics from URLs from above)
    ```python
    scrapy crawl players_stats
    ```

# Scope/Aim as an indiviual project

- Update the crawler periodically to reflect changes on [Sofifa platform](https://sofifa.com/players).

# Future features

- Add analysis projects on the crawled data.
- Update the crawler to perform scraping to obtain _Teams_ data (currently player-data)
- Improve speed of the crawler

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
