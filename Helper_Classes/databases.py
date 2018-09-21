"""
Author : Dominik Ondusko
Contact: dominik@blockseedinvestments.com
A file to handle database operations
"""

from influxdb import DataFrameClient
from configuration import Configuration

class InfluxDB:
    """Client connections to the InfluxDB server"""
    def __init__(self, config_file, setting_name):
        self.config_info = config_file
        self.host = self.config_info.get_field('host', setting_name)
        self.port = self.config_info.get_field('port', setting_name)
        self.user = self.config_info.get_field('user', setting_name)
        self.password = self.config_info.get_field('password', setting_name)

    @property
    def min_gdax_df_client(self):
        """The client connection to the GDAX database for minutely data"""
        return DataFrameClient(self.host, self.port, self.user, self.password,
                               self.config_info.getField('minuteDBName'))

    @property
    def hour_gdax_df_client(self):
        """The client connection to the GDAX database for hourly data"""
        return DataFrameClient(self.host, self.port, self.user, self.password,
                               self.config_info.getField('hourlyDBName'))

    @property
    def day_gdax_df_client(self):
        """The client connection to the GDAX database for daily data"""
        return DataFrameClient(self.host, self.port, self.user, self.password,
                               self.config_info.getField('dailyDBName'))

    @property
    def cmc_df_client(self):
        """The client connection to the CoinMarketCap database for daily data"""
        DataFrameClient(self.host, self.port, self.user, self.password,
                        self.config_info.getField('CMCDBName'))

    @property
    def config_info(self):
        """The configuration object for the database"""
        return self._config_info

    @config_info.setter
    def config_info(self, name):
        self._config_info = Configuration(name)

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
