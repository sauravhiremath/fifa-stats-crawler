# Football Players Statistics WebCrawler

This project is a sub-module for [Multiplayer Football Draft Simulator](https://github.com/sauravhiremath/fifa).

# About

A web-crawler to scrape all football players' information from [Sofifa](https://sofifa.com/players) and exporting it to JSON format. Perform data cleaning and analytics on the obtained data

* Crawler: Built on scrapy using python3
* Analytics: IPynb noteboook python3

Further exported to the [Football Draft Backend](https://github.com/sauravhiremath/fifa-api) to serve from an endpoint

# Steps to run the project

* Install project dependencies <br>
    ```python
    pip install -r requirements.txt
    ```

* Run the crawler with _./fifa-crawler_ as current directory (This the main scrapy crawler directory)
    > Make sure to change the filenames to read and write appropriately: <br>
    > `players_url.json` --> scraping urls <br>
    > `players_stats_raw.json` --> scraping player stats

    * First run the URL spider (To get all players urls)
        ```python
        scrapy crawl players_url
        ```
    * After successfull, run the stats spider (To get the players statistics from URLs from above)
        ```python
        scrapy crawl players_stats
        ```



# Scope/Aim as an indiviual project

* Update the crawler periodically to reflect changes on [Sofifa platform](https://sofifa.com/players).

# Future features

* Add analysis projects on the crawled data.
* Update the crawler to perform scraping to obtain *Teams* data (currently player-data)
* Improve speed of the crawler
