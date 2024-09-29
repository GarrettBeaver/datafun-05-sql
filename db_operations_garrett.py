'''
Module 5 - This file will demonstrate basic usage of Python SQL integration.  It will:

- Manipulate that data by calling sql queries sorted into distinct files
'''

#####################################
# Import modules
#####################################
import logging
import sqlite3
from pathlib import Path
import pandas as pd

#the same basic function is used in both scripts, so I import the generic script from the other file
from db_initialize_garrett import execute_sql_from_file

#####################################
# Declare global variables
#####################################

#where the database file will be created
db_file_path = Path("project_rental.db")
#raw data for rental table
rental_data_path = Path("data").joinpath("rentals.csv")
#raw data for vehicles data
vehicle_data_path = Path("data").joinpath("vehicles.csv")
db_file = Path("project_rental.sqlite3")

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')


#####################################
# Define a main() function for this module.
#####################################


def main() -> None:
    '''The main function calls all sql queries in the sql folder.
    '''


    #run all sql scripts
    execute_sql_from_file(db_file_path, Path("sql").joinpath("delete_records.sql"))
    execute_sql_from_file(db_file_path, Path("sql").joinpath("insert_records.sql"))
    execute_sql_from_file(db_file_path, Path("sql").joinpath("query_aggregration.sql"))
    execute_sql_from_file(db_file_path, Path("sql").joinpath("query_filter.sql"))
    execute_sql_from_file(db_file_path, Path("sql").joinpath("query_group_by.sql"))
    execute_sql_from_file(db_file_path, Path("sql").joinpath("query_sorting.sql"))
    execute_sql_from_file(db_file_path, Path("sql").joinpath("query_join.sql"))
    logging.info("All SQL operations completed successfully")
    logging.info("Program ended")  


#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
