""" Driver file to fill the influxDB database
Author : Dominik Ondusko
Contact: dominik@blockseedinvestments.com """

from databases import InfluxDB

def main():
    """ Program main entry point definition """
    db_conn = InfluxDB('configurations.ini', 'InfluxDBConnectionInfo')
    #with ProcessPoolExecutor() as executor:
    #    executor.submit()

if __name__ == '__main__':
    main()
