"""
Driver file to fill the influxDB database
Author : Dominik Ondusko
Contact: dominik@blockseedinvestments.com
"""

from databases import InfluxDB
from subprocess import Popen
from pathlib import Path

def fill_database():
    """ Program main entry point definition """
    db_conn = InfluxDB('../configurations.ini', 'InfluxDBConnectionInfo')
    cmc_path = Path(__file__).parent.joinpath('CMC')
    Popen(['scrapy', 'crawl', 'coinSpider'], shell = True, cwd = cmc_path)