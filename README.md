# Fifa 20 crawler

This project is a sub-module of [Fifa Custom Team Builder](https://github.com/sauravhiremath/fifa).<br>

# About

A web-crawler to scrape all football players' information from [Sofifa](https://sofifa.com/players) and pre-processess it to JSON format. And analytics on the obtained data<br><br>

* Crawler: Built on scrapy using python3
* Analytics: IPynb noteboook python3

Further exported to the [Fifa Custom Team Builder Backend](https://github.com/sauravhiremath/fifa-api) backend to serve as an API.

# Steps to run the project


* Install project dependencies <br>
    ``` python
        pip install -r requirements.txt
    ```

* Run the crawler from `fifa-crawler` as current directory (This the main scrapy crawler directory)
    > Make sure to change the filenames to read and write appropriately: \n
    > `players_url.json` --> scraping urls
    > `players_stats_raw.json` --> scraping player stats

    * First run the players url spider
        ``` python
            scrapy crawl players_url
        ```
    * After successfull, run the stats spider
        ``` python
            scrapy crawl players_stats
        ```



# Scope/Aim as an indiviual project

* Update the crawler periodically to reflect changes on [Sofifa platform](https://sofifa.com/players).

# Future features

* Add analysis projects on the crawled data.
* Update the crawler to perform scraping to obtain *Teams* data (currently player-data)
* Improve speed of the crawler