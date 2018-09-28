"""
A file to handle database operations
Author : Dominik Ondusko
Contact: dominik@blockseedinvestments.com
"""

import influxdb
import configuration
import datetime

class InfluxDB:
    """Client connections to the InfluxDB server"""
    def __init__(self, config_file, setting_name):
        self.config_info = config_file
        self.setting_name = setting_name
        self.host = self.config_info.get_field('host', setting_name)
        self.port = self.config_info.get_field('port', setting_name)
        self.user = self.config_info.get_field('user', setting_name)
        self.password = self.config_info.get_field('password', setting_name)

    @property
    def min_gdax_df_client(self):
        """The client connection to the GDAX database for minutely data"""
        return influxdb.DataFrameClient(self.host, self.port, self.user, self.password,
                               self.config_info.get_field('minuteDBName', self.setting_name))
    
    @property
    def hour_gdax_df_client(self):
        """The client connection to the GDAX database for hourly data"""
        return influxdb.DataFrameClient(self.host, self.port, self.user, self.password,
                               self.config_info.get_field('hourlyDBName', self.setting_name))

    @property
    def day_gdax_df_client(self):
        """The client connection to the GDAX database for daily data"""
        return influxdb.DataFrameClient(self.host, self.port, self.user, self.password,
                               self.config_info.get_field('dailyDBName', self.setting_name))

    @property
    def cmc_df_client(self):
        """The client connection to the CoinMarketCap database for daily data"""
        return influxdb.DataFrameClient(self.host, self.port, self.user, self.password,
                        self.config_info.get_field('CMCDBName', self.setting_name))

    @property
    def config_info(self):
        """The configuration object for the database"""
        return self._config_info

    @config_info.setter
    def config_info(self, name):
        self._config_info = configuration.Configuration(name)

    @property
    def host(self):
        """The host name to connect to the database"""
        return self._host

    @host.setter
    def host(self, name):
        self._host = name

    @property
    def port(self):
        """The port number of the database"""
        return self._port

    @port.setter
    def port(self, num):
        self._port = num

    @property
    def user(self):
        """The username of the client connecting"""
        return self._user

    @user.setter
    def user(self, name):
        self._user = name

    @property
    def password(self):
        """The password of the client connecting"""
        return self._password

    @password.setter
    def password(self, name):
        self._password = name

    @property
    def setting_name(self):
        """Holds the setting name of the connection"""
        return self._setting_name

    @setting_name.setter
    def setting_name(self, name):
        self._setting_name = name

    def getData(self, source, coin_names, time_frame, from_date = None, to_date = None):
        """
        Query for minute data
        from_date and to_date should be datetime objects
        """
        assert time_frame in ['Minutely', 'Hourly', 'Daily'], RuntimeError('Check input parameters for your query.')
        assert source in ['GDAX', 'CoinMarketCap'], NotImplementedError('Source not supported')

        if from_date is not None:
            from_date = from_date.isoformat().replace('T', ' ')
        if to_date is not None:
            to_date = to_date.isoformat().replace('T', ' ')

        if source == 'GDAX':
            if time_frame == 'Minutely':
                client = self.min_gdax_df_client
            elif time_frame== 'Hourly':
                client = self.hour_gdax_df_client
            elif time_frame== 'Daily':
                client = self.day_gdax_df_client
        elif source == 'CoinMarketCap':
            assert time_frame == 'Daily', RuntimeError('CoinMarketCap only provides /"Daily/" data.')
            client = self.cmc_df_client

        if isinstance(coin_names, list):
            coins = ''
            for coin in coin_names:
                if coin == coin_names[0]:
                    coins += '\"{}\"'.format(coin)
                else:
                    coins += ',\"{}\"'.format(coin)
        elif isinstance(coin_names, str):
            coins = '\"{}\"'.format(coin_names)
        else:
           raise RuntimeError('You are trying to pass an invalid object type to represent your coin_names')

        if from_date is None and to_date is None:
            data = client.query('select * from {};'.format(coins))
        elif from_date is not None and to_date is not None:
            data = client.query('select * from {} where time > \'{}\' and time < \'{}\''.format(coins, from_date, to_date))
        elif from_date is not None and to_date is None:
            data = client.query('select * from {} where time > \'{}\''.format(coins, from_date))
        elif from_date is None and to_date is not None:
            data = client.query('select * from {} where time < \'{}\''.format(coins, to_date))

        if isinstance(coin_names, list):
            return data
        else:
            return data[coin_names]

    def get_first_date(self, db_conn, coin):
        """Get oldest date for a coin in influxDB"""
        try:
            last_date = db_conn.query('SELECT * FROM \"{}\" GROUP BY * ORDER BY ASC LIMIT 1;'.format(coin))
            last_date = datetime.datetime.strptime(str(last_date[coin].index[0])[:-6], '%Y-%m-%d %H:%M:%S')
        except KeyError as k:
            last_date = datetime.datetime(2013, 4, 28)
        except InfluxDBClientError as e:
            last_date = datetime.datetime(2013, 4, 28)

        return last_date