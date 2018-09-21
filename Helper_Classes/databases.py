"""
Author : Dominik Ondusko
Contact: dominik@blockseedinvestments.com
A file to handle database operations
"""

from influxdb import DataFrameClient
from configuration import Configuration

class InfluxDB:
    """Object definition for the InfluxDB client"""
    minGDAXDFClient = DataFrameClient(host, port, user, password, config_info.getField(
        'minuteDBName'))
    hourGDAXDFClient = DataFrameClient(host, port, user, password, config_info.getField(
        'hourlyDBName'))
    dayGDAXDFClient = DataFrameClient(host, port, user, password, config_info.getField(
        'dailyDBName'))
    CMCDFClient = DataFrameClient(host, port, user, password, config_info.getField(
        'CMCDBName'))

    def __init__(self, config_file, setting_name):
        self.config_info = config_file
        self.host = self.config_info.get_field('host', setting_name)
        self.port = self.config_info.get_field('port', setting_name)
        self.user = self.config_info.get_field('user', setting_name)
        self.password = self.config_info.get_field('password', setting_name)

    @property
    def config_info(self):
        """The configuration object for the database"""
        return self.config_info

    @config_info.setter
    def config_info(self, name):
        self.config_info = Configuration(name)

    @property
    def host(self):
        """The host name to connect to the database"""
        return self.host

    @host.setter
    def host(self, name):
        self.host = name

    @property
    def port(self):
        """The port number of the database"""
        return self.port

    @port.setter
    def port(self, num):
        self.port = num

    @property
    def user(self):
        """The username of the client connecting"""
        return self.user

    @user.setter
    def user(self, name):
        self.user = name

    @property
    def password(self):
        """The password of the client connecting"""
        return self.password

    @password.setter
    def password(self, name):
        self.password = name
