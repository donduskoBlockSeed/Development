"""
A file to handle parsing the configuration file
Author : Dominik Ondusko
Contact: dominik@blockseedinvestments.com
"""

import configparser
import pathlib

class Configuration:
    """Configuration object definition"""
    def __init__(self, filename):
        self.file = filename

    @property
    def file(self):
        """Stores the filename of the configuration file"""
        return self._file

    @file.setter
    def file(self, name):
        name = pathlib.Path(name)
        if name.exists():
            self._file = configparser.ConfigParser()
            self._file.read(name)
        else:
            raise IOError('{} does not exist.'.format(name.resolve()))

    def get_field(self, field, setting_name):
        """Method to retrieve fields from the configuration file """
        ret_field = self.file.get(setting_name, field)
        if ',' in ret_field:
            ret_field = [X.strip() for X in ret_field.split(',')]
            ret_field = [int(X) if self.isint(X) else float(X) if self.isfloat(X) else X for i, X in enumerate(ret_field)]
            if '' in ret_field:
                ret_field.remove('')
        return ret_field

    def isfloat(self, val):
        """Check if str value is float"""
        try:
            float(val)
        except ValueError:
            return False
        else:
            return True

    def isint(self, val):
        """Check if str value is int"""
        try:
            float(val)
            int(val)
        except ValueError:
            return False
        else:
            return True
