"""
Web scraper to scrape data from coinmarketcap
Author : Dominik Ondusko
Contact: dominik@blockseedinvestments.com
"""

import datetime
import scrapy
import requests
import lxml

class CoinSpider(scrapy.Spider):
    """The cmc scraper object"""
    name = 'coinSpider'

    def start_requests(self):
        """Begin sending requests to webpages"""
        for url in self.urls:
           yield scrapy.Request(url, self.parse)

    def parse(self, response):
        """Method to parse a response object"""
        item = scrapy.loader.ItemLoader(item = DataPoint(), response = response)
        item.add_xpath('dates', '//*[@id="historical-data"]/div/div[2]/table/tbody/tr/td[1]/text()')
        item.add_xpath('opens', '//*[@id="historical-data"]/div/div[2]/table/tbody/tr/td[2]/text()')
        item.add_xpath('highs', '//*[@id="historical-data"]/div/div[2]/table/tbody/tr/td[3]/text()')
        item.add_xpath('lows', '//*[@id="historical-data"]/div/div[2]/table/tbody/tr/td[4]/text()')
        item.add_xpath('closes', '//*[@id="historical-data"]/div/div[2]/table/tbody/tr/td[5]/text()')
        item.add_xpath('volumes', '//*[@id="historical-data"]/div/div[2]/table/tbody/tr/td[6]/text()')
        item.add_xpath('mcaps', '//*[@id="historical-data"]/div/div[2]/table/tbody/tr/td[7]/text()')
        item.add_xpath('coinName', '/html/body/div[2]/div/div[1]/div[3]/div[1]/h1/span/text()')
        yield item.load_item()

    @property
    def urls(self):
        """The urls to scrape"""
        start_date = '20130428'
        end_date = str(datetime.datetime.utcnow().date()).replace('-', '')
        page = requests.get('https://coinmarketcap.com/all/views/all/')
        tree = lxml.html.fromstring(page.content)
        urls = ['https://coinmarketcap.com{}historical-data/?start={}&end={}'.format(
            x, start_date, end_date) for x in tree.xpath('//tr/td/span/a/@href')]
        return urls
