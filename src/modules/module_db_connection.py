import mysql
from mysql.connector import errorcode
from src.messages.confirmation_messages import message_confirmation
from src.messages.error_messages import error_manipulation


# MySQL server configuration.
db_connection_config = {
    'user': 'XXXX',
    'password': 'XXXX',
    'host': 'XXXX',
    'port': 32768,
    'database': 'db_sales',
    'raise_on_warnings': True
}


"""
Function: open_db_connection
----------------------------
Establishes a connection to the database.

Behavior:
- Attempts to connect to the database using the configuration provided in `db_connection_config`.
- If successful, returns the database connection object.
- If a connection error occurs:
  - Prints a specific error message for access denial or a missing database.
  - Prints the general error for other issues.
  - Exits the program.
"""

def open_db_connection():
    try:
        db_connection = mysql.connector.connect(**db_connection_config)
        return db_connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(err)
        exit()


def close_db_connection(db_connection):
    return db_connection.close()


"""
Function: select_record
------------------------
Executes an SQL query and retrieves records from a database.

Parameters:
- query (str): the SQL query to execute.
- number_of_records (int): specifies the number of records to return. 
  - If 1, fetches a single record using fetchone().
  - Otherwise, fetches all records using fetchall().
- parameter1 and parameter2 (any): optional parameter to include in the SQL query.

Behavior:
- Dynamically determines the number of parameters to include in the query based on which parameters are not `None`.
- Commits the transaction to save changes to the database.

Returns:
- result (tuple | list): the retrieved record(s) from the query.
  - If number_of_records == 1: returns a single record as a tuple.
  - Otherwise: returns a list of tuples representing multiple records.
"""

def select_record(query, number_of_records, parameter1, parameter2):
    db_connection = open_db_connection()
    cursor_select = db_connection.cursor()
    if parameter1 is None:
        cursor_select.execute(query)
    elif parameter2 is None:
        cursor_select.execute(query, (parameter1,))
    else:
        cursor_select.execute(query, (parameter1, parameter2))
    if number_of_records == 1:
        result = cursor_select.fetchone()
    else:
        result = cursor_select.fetchall()
    cursor_select.close()
    db_connection.close()
    return result


"""
Function: manipulate_record
---------------------------
Executes an SQL query to manipulate records in a database (e.g., INSERT, UPDATE, DELETE).

Parameters:
- query (str): the SQL query to execute.
- parameterN (any): parameter to include in the SQL query.

Behavior:
- Dynamically determines the number of parameters to include in the query based on which parameters are not `None`.
- Commits the transaction to save changes to the database.

Returns:
- None: The function does not return a value but prints:
  - `message_confirmation` if the operation is successful.
  - `error_manipulation` if an error occurs.
"""

def manipulate_record(query, parameter1, parameter2, parameter3, parameter4):
    try:
        db_connection = open_db_connection()
        cursor_select = db_connection.cursor()
        if parameter2 is None:
            cursor_select.execute(query, (parameter1,))
        elif parameter3 is None:
            cursor_select.execute(query, (parameter1, parameter2,))
        elif parameter4 is None:
            cursor_select.execute(query, (parameter1, parameter2, parameter3,))
        else:
            cursor_select.execute(query, (parameter1, parameter2, parameter3, parameter4))
        db_connection.commit()
        cursor_select.close()
        db_connection.close()
        print(message_confirmation)
    except mysql.connector.Error:
        print(error_manipulation)