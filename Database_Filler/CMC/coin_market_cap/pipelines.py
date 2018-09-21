"""
Define your item pipelines here

Don't forget to add your pipeline to the ITEM_PIPELINES setting
See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
"""

class coin_market_cap(object):
    """The pipeline object to send parsed items"""
    def process_item(self, item, spider):
        """Process the item that was parsed""" 
        print(item['dates'])
        #return item
