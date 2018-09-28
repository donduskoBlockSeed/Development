"""
Define here the models for your scraped items

See documentation in:
https://doc.scrapy.org/en/latest/topics/items.html
"""

import scrapy

class DataPoint(scrapy.Item):
    """
    define the fields for your item here like:
    name = scrapy.Field()
    """
    coinName = scrapy.Field()
    dates = scrapy.Field()
    opens = scrapy.Field()
    highs = scrapy.Field()
    lows = scrapy.Field()
    closes = scrapy.Field()
    volumes = scrapy.Field()
    mcaps = scrapy.Field()
