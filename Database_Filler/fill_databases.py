"""
Driver file to fill the influxDB database
Author : Dominik Ondusko
Contact: dominik@blockseedinvestments.com
"""

import databases
import subprocess
import pathlib

def fill_database():
    """ Program main entry point definition """
    db_conn = databases.InfluxDB('../configurations.ini', 'InfluxDBConnectionInfo')
    cmc_path = pathlib.Path(__file__).parent.joinpath('CMC')
    subprocess.Popen(['scrapy', 'crawl', 'coinSpider'], shell = True, cwd = cmc_path)