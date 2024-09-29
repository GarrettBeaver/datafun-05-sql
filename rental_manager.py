'''
Module 5 - This file will demonstrate basic usage of Python SQL integration.  It will:
- Create a database
- Fill that database with data
- Manipulate that data by calling sql queries sorted into distinct files
'''

#####################################
# Import modules
#####################################
import logging
import sqlite3
from pathlib import Path
import pandas as pd

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
# Declare functions
#####################################

def verify_and_create_folders(paths):
    """Verify and create folders if they don't exist.
       requires "paths" argument as list of paths where folders should be created 
    """
    for path in paths:
        folder = path.parent
        #create folder if it does not exist
        if not folder.exists():
            print(f"Creating folder: {folder}")
            folder.mkdir(parents=True, exist_ok=True)
            logging.info("Folder" + path + "exists")
        else:
            print(f"Folder already exists: {folder}")



def create_database(db_path):
    """Create a new SQLite database file if it doesn't exist.
    Requires db_path where database is to be created.    
    """
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
        print("Database created successfully.")
        logging.info("Database created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating the database: {e}")

def insert_data_from_csv(db_path, vehicle_data_path, rental_data_path):
    """Read data from CSV files and insert the records into their respective tables.
    Arguements: db_path - Where database is located
                vehicle_data_path - file path of "vehicles.csv"
                rental_data_path  - file path of "rentals.csv"
    """
    try:
        #create dataframe of the two csv files
        vehicles_df = pd.read_csv(vehicle_data_path)
        rentals_df = pd.read_csv(rental_data_path)
        with sqlite3.connect(db_path) as conn:
            #load those dataframes to the table
            vehicles_df.to_sql("Vehicles", conn, if_exists="replace", index=False)
            rentals_df.to_sql("Rentals", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
            logging.info("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"Error inserting data: {e}")

def execute_sql_from_file(db_filepath, sql_file):
    '''This function will run a sql script on a database
    Arguments db_filepath - location of database that will have actions performed on it
              sql_file    - location of sql file             
    '''
    try:
        #read sql script file
        with sqlite3.connect(db_filepath) as conn:
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            #execute the script
            conn.executescript(sql_script)
            print(f"Executed SQL from {sql_file}")
            logging.info(f"Executed SQL from {sql_file}")
    except sqlite3.Error as e:
        print(f"Error executing: {e}")
        logging.error(f"Error executing: {e}")



#####################################
# Define a main() function for this module.
#####################################


def main() -> None:
    '''The main function calls all the functions created above, will create database, and query using sql.
    '''
    #log start of main function
    logging.info("Program started") # add this at the beginning of the main method

    #make sure folders exist
    paths_to_verify = [rental_data_path, vehicle_data_path]
    verify_and_create_folders(paths_to_verify)

    #create database and fill with intial data
    create_database(db_file_path)
    #create tables
    execute_sql_from_file(db_file_path, Path("sql").joinpath("create_tables.sql"))
    #fill table with data
    insert_data_from_csv(db_file_path, vehicle_data_path, rental_data_path)


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
