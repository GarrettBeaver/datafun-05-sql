'''
Module 5 - SQL project
'''



#####################################
# Import modules
#####################################
import logging
import sqlite3
from pathlib import Path





'''
Configure logging to write to a file named log.txt.
Log the start of the program using logging.info().
Log the end of the program using logging.info().
Log exceptions using logging.exception().
Log other major events using logging.info().
Log the start and end of major functions using logging.debug().
'''

'''
1create_tables.sql - create your database schema using sql
2. insert_records.sql - insert at least 10 additional records into each table.

3. update_records.sql - update 1 or more records in a table.
UPDATE Vehicles
SET DailyRate = 42.00
WHERE Year < 2020;

4delete_records.sql - delete 1 or more records from a table.
DELETE FROM Vehicles
WHERE VehicleID = 1;

5.query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.
SELECT AVG(DailyRate) AS AverageDailyRate
FROM Vehicles;

SELECT Year, COUNT(*) AS NumberOfVehicles
FROM Vehicles
GROUP BY Year;


6. query_filter.sql - use WHERE to filter data based on conditions.
SELECT VehicleID, Make, Model, Year
FROM Vehicles
WHERE Year = 2020 OR Year = 2021;

7.query_sorting.sql - use ORDER BY to sort data.
SELECT VehicleID, Make, Model, DailyRate
FROM Vehicles
ORDER BY DailyRate DESC;

8.query_group_by.sql - use GROUP BY clause (and optionally with aggregation)
SELECT Year, SUM(DailyRate) AS TotalRateByYear
FROM Vehicles
GROUP BY Year;

9.query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.
SELECT Customers.Name, Orders.OrderID, Orders.OrderDate, Orders.TotalAmount
FROM Customers
INNER JOIN Orders
ON Customers.CustomerID = Orders.CustomerID
WHERE Customers.Country = 'USA';
'''


#####################################
# Declare global variables
#####################################

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

# Define the database file in the current root project directory
db_file = pathlib.Path("project.sqlite3")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)


def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")


#####################################
# Define a main() function for this module.
#####################################

#The main function calls get_byline() to retrieve the byline.
def main() -> None:
    logging.info("Program started") # add this at the beginning of the main method


    # Create database schema and populate with data
    #... your code here to perform all required operations

    logging.info("All SQL operations completed successfully")


 

    paths_to_verify = [sql_file_path, author_data_path, book_data_path]
    verify_and_create_folders(paths_to_verify)
    
    create_database(db_file_path)
    create_tables(db_file_path, sql_file_path)
    insert_data_from_csv(db_file_path, author_data_path, book_data_path)

    logging.info("Program ended")  # add this at the end of the main method
#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
