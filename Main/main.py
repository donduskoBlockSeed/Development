""" Driver file to run any sub-driver file based on arguments
Author : Dominik Ondusko
Contact: dominik@blockseedinvestments.com """

import fill_databases
import argparse
import deltix_handle

def get_arguments(test_args = None):
    """Return the argument parse object with the parsed arguments"""
    parser = argparse.ArgumentParser(description = 'Select an action to do.')
    parser.add_argument('-fill', action = 'store_true', help = 'Fill the influxdb database with any new data')
    parser.add_argument('-deltix', action = 'store_true', help = 'Store Deltix collected data to csv format and clean existing database')
    if test_args == None:
        return parser.parse_args()
    else:
        return parser.parse_args(test_args)

if __name__ == '__main__':
    args = get_arguments(['-deltix'])
    if args.fill:
        fill_databases.fill_database()
    if args.deltix:
        deltix_handle.save_to_csvs()