"""
A file to handle parsing the configuration file
Author : Dominik Ondusko
Contact: dominik@blockseedinvestments.com
"""

from configparser import ConfigParser

class Configuration:
    """Configuration object definition"""
    def __init__(self, filename):
        self.file = filename

    @property
    def file(self):
        """Stores the filename of the configuration file"""
        return self.filename

    @file.setter
    def filename(self, name):
        self.file = ConfigParser().read(name)

    @classmethod
    def get_field(cls, field, setting_name):
        """Method to retrieve fields from the configuration file """
        ret_field = cls.file.get(setting_name, field)
        if ',' in ret_field:
            ret_field = [X.strip() for X in ret_field.split(',')]
            ret_field = [int(X) if cls.isint(X) else float(X) for i, X in enumerate(ret_field)]
            if '' in ret_field:
                ret_field.remove('')

    @classmethod
    def isfloat(cls, val):
        """Check if str value is float"""
        try:
            float(val)
        except ValueError:
            return False
        else:
            return True

    @classmethod
    def isint(cls, val):
        """Check if str value is int"""
        try:
            float(val)
            int(val)
        except ValueError:
            return False
        else:
            return True
