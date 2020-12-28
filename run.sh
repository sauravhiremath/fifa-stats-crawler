#!/bin/bash

# Check environment
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac

DIRECTORY = "data/json"

if [ ! -d "$DIRECTORY" ]; then
  printf "[*] Required Directories and Files not found, creating now..\n"
  printf "[*] Creating Directory - $DIRECTORY\n"
  printf "[*] Creating File - $DIRECTORY/players_urls.json\n"
  printf "[*] Creating File - $DIRECTORY/players_stats.json\n"
  if [ machine == 'MingGw' ] then
    mkdir "data\json"
    type NUL >> players_urls.json
    type NUL >> players_stats.json
  else
    mkdir $DIRECTORY
    touch players_urls.json
    touch players_stats.json
fi

printf "[*] Starting FIFA players urls crawler...\n\n\n"
scrapy crawl players_urls.json && \
printf "[*] FUFA players URLS CRAWL COMPLETED\n"

printf "[*] Starting FIFA players stats crawler...\n\n\n"
scrapy crawl players_stats.json -L INFO
printf "[*] FIFA players STATS CRAWL COMPLETED\n"
