"""
Define here the models for your scraped items

See documentation in:
https://doc.scrapy.org/en/latest/topics/items.html
"""

from scrapy import Item, Field


class DataPoint(Item):
    """
    define the fields for your item here like:
    name = scrapy.Field()
    """
    dates = Field()
    opens = Field()
    highs = Field()
    lows = Field()
    closes = Field()
    volumes = Field()
    mcaps = Field()
