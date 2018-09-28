"""
Driver file to pull Deltix data into csv files
Author : Dominik Ondusko
Contact: dominik@blockseedinvestments.com
"""

import configuration
import subprocess
import pathlib
import os

def create_bat_file():
    """Create the batch file to run the tickdb commands"""  
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = pathlib.Path(dir_path).joinpath('exec.bat')
    exec_path = pathlib.Path(dir_path).joinpath('commands.txt')
    exec = 'tickdb -exec exec {} -exit'.format(exec_path)
    f = open(file_path, 'w+')
    f.write(exec)
    f.close()

def create_command_file(db_addr):
    """Create the command file to execute"""
    exec = 'set db {}'.format(db_addr)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = pathlib.Path(dir_path).joinpath('commands.txt')
    f = open(file_path, 'w+')
    f.write(exec)
    f.close()

def save_to_csvs():
    """Save all streams for a day to csv files"""
    config = configuration.Configuration('../configurations.ini')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = pathlib.Path(dir_path).joinpath('exec.bat')
    print(file_path)
    setting_name = 'DeltixDatabases'
    streams = config.get_field('dbs', setting_name)
    db_addr = config.get_field('dbAddress', setting_name)
    for stream in streams:
        create_command_file(db_addr)
        create_bat_file()
        subprocess.Popen([str(file_path)], shell = True)