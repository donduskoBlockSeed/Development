""" Driver file to run any sub-driver file based on arguments
Author : Dominik Ondusko
Contact: dominik@blockseedinvestments.com """

from fill_databases import fill_database

def main():
    """This function decides what driver file to run"""
    fill_database()

if __name__ == '__main__':
    main()
