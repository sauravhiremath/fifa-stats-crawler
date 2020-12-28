# -*- coding: utf-8 -*-
import scrapy
import json
import logging

class SofifaSpider(scrapy.Spider):
    name='players_stats'

    def __init__(self):
        with open('../data/json/players_url_dev.json') as json_data:
            self.players = json.load(json_data)
        self.player_count = 1

    def start_requests(self):
        urls = [
            'https://sofifa.com/player/158023?units=mks' # ---> Messi example page
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for player in response.css('.info'):
            player_name = player.xpath('//div[@class="info"]/h1/text()').get().split('(')[0].strip()
            player_info = player.xpath('//div[@class="meta bp3-text-overflow-ellipsis"]/text()').getall()
            player_info = [info for info in player_info if info != ' ']
            player_info = player_info + (player.xpath('//div[@class="meta bp3-text-overflow-ellipsis"]/span/text()').getall())
            player_url_photo = player.xpath('//div[@class="bp3-card player" ]//img/@data-src').getall()[0]

            # Add stats_names and values (Crossing, finishing) + goalkeeper stats_names and values (GK Diving, GK Reflexes)
            player_stats = player.xpath('//div[@class="card"]//ul//li/span[2]//text()').re(r'[\w ]+')
            player_stats.insert(-3, player.xpath('//div[@class="card"]//ul//li[text()=" Composure"]/text()').get()[1:])
            player_stats = player_stats + player.xpath('//div[@class="card" and h5="Goalkeeping"]//ul//li/text()').getall()
            player_stats_values = player.xpath('//div[@class="card" and h5 !="Profile" and h5 != "Traits"]/ul//li/span[1]//text()').getall()[-34:]

            # Overall rating, potential rating + value, wage names and values
            primary_stats = player.xpath('//div[@class="sub"]//text()').getall()
            primary_stats_values = player.xpath('//section[@class="card spacing"]/div/div[@class = "column col-3"]/div/span/text()').getall()
            primary_stats_values = primary_stats_values + [stat for stat in player.xpath('//section[@class="card spacing"]/div/div/div[not (@class)]/text()').getall() if stat != ' ']
            
            # Add the club and nationality names and the respective team rating
            player_teams = player.xpath('//div[@class="card"]//h5//a/text()').getall()
            player_teams_values = player.xpath('///div[@class="card"]//ul[contains(@class,"pl text-right")]//li[1]//span[1]/text()').re(r'\w+')

            # Add profile stats (Prefeered foot, Weak Foot, International Reputation) and its values
            player_profile_stats = player.xpath('//div[@class="card" and h5="Profile"]//label/text()').getall()
            player_profile_values = player.xpath('//div[@class="card" and h5="Profile"]//li[label != "ID"]/text()').getall()
            player_profile_values = [val for val in player_profile_values if val != ' ']
            player_profile_values = player_profile_values + (player.xpath('//div[@class="card" and h5="Profile"]//li/span[not (@class)]/text()').getall())

            # Add player specialities (#Acrobat, #Dribbler) and Traits (Finesse shot, Playmaker)
            player_tags = player.xpath('//div[@class="card" and h5="Player Specialities"]//ul//li//a/text()').getall()
            player_traits = player.xpath('//div[@class="card" and h5="Traits"]//ul//li//text()').getall()

            ###########################################################

            # Age 30 (Jun 24, 1987) 170cm 72kg'
            age, month, day, year, height, weight = player_info[0].split()
            age = age[:-4]
            month = month.replace('(', '')
            day = int(day.replace(',', ''))
            year = int(year.replace(')', ''))
            height = int(height[:-2])
            weight = int(weight[:-2])

            stats = {k:v for k, v in zip(primary_stats, primary_stats_values)}
            stats["Overall Rating"] = int(stats["Overall Rating"])
            stats["Potential"] = int(stats["Potential"])
            
            extra = {k:v for k, v in zip(player_profile_stats, player_profile_values)}
            extra["International Reputation"] = int(extra["International Reputation"])
            extra["Weak Foot"] = int(extra["Weak Foot"])
            extra["Skill Moves"] = int(extra["Skill Moves"])

            teams = {'teams':{k:int(v) for k, v in zip(player_teams, player_teams_values)}}

            # skills
            attacking = {'attacking':{k.replace(' ', ''):int(v) for k, v in zip(player_stats[:5], player_stats_values[:5])}}
            skill = {'skill':{k.replace(' ', ''):int(v) for k, v in zip(player_stats[5:10], player_stats_values[5:10])}}
            movement = {'movement':{k.replace(' ', ''):int(v) for k, v in zip(player_stats[10:15], player_stats_values[10:15])}}
            power = {'power':{k.replace(' ', ''):int(v) for k, v in zip(player_stats[15:20], player_stats_values[15:20])}}
            mentality = {'mentality':{k.replace(' ', ''):int(v) for k, v in zip(player_stats[20:26], player_stats_values[20:26])}}
            defending = {'defending':{k.replace(' ', ''):int(v) for k, v in zip(player_stats[26:29], player_stats_values[26:29])}}
            goalkeeping = {'goalkeeping':{k.replace(' ', ''):int(v) for k, v in zip(player_stats[29:], player_stats_values[29:])}}

            player_info_dict = {
                    'name': player_name,
                    'photo_url': player_url_photo,
                    'positions': [position for position in player_info[1:] if position.isupper()],
                    'age': age,
                    'birth_date': '{}/{}/{}'.format(year, month, day),
                    'height': height,
                    'weight': weight,
            }
            player_info_dict.update(stats)
            player_info_dict.update(extra)
            player_info_dict.update(teams)
            player_info_dict.update(attacking)
            player_info_dict.update(skill)
            player_info_dict.update(movement)
            player_info_dict.update(power)
            player_info_dict.update(mentality)
            player_info_dict.update(defending)
            player_info_dict.update(goalkeeping)
            player_skills_dict = {'player_traits': player_traits}
            player_info_dict.update(player_skills_dict)
            player_hashtags = {'player_hashtags': player_tags}
            player_info_dict.update(player_hashtags)

            logging.info('*******************  ' + str(self.player_count) + '  *******************' + '\n\n\n')
            yield player_info_dict

            if self.player_count < len(self.players):
                next_page_url = 'https://sofifa.com' + self.players[self.player_count]['player_url'] + '?units=mks'
                self.player_count += 1
                yield scrapy.Request(url=next_page_url, callback=self.parse)