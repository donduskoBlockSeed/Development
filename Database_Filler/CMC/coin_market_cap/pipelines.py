"""
Define your item pipelines here

Don't forget to add your pipeline to the ITEM_PIPELINES setting
See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
"""

import pandas
import numpy
import databases

class coin_market_cap(object):
    """The pipeline object to send parsed items"""
    db_conn = databases.InfluxDB('../../configurations.ini', 'InfluxDBConnectionInfo')
    
    def process_item(self, item, spider):
        """Process the item that was parsed""" 
        data = pandas.DataFrame(index = pandas.to_datetime(item['dates']))
        data['Close'] = item['closes'] 
        data['High'] = item['highs']
        data['Low'] = item['lows']
        data['Open'] = item['opens']
        data['Volume'] = item['volumes']
        data['Volume'] = data.Volume.str.replace(',', '')
        data['MarketCap'] = item['mcaps']  
        data['MarketCap'] = data.MarketCap.str.replace(',', '')
        data.replace('-', numpy.NaN, inplace = True)
        data = data.astype(float)
        data['Average'] = data[['High', 'Low']].sum(axis = 1) / 2
        db_table = '{}-USD'.format(item['coinName'][0].replace(')', '').replace('(', ''))
        return 'Wrote to {}.'.format(db_table)
