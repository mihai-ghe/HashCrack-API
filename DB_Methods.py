import sqlite3
import hashlib


def enter_hash():

    db_connection = None

    try:

        # Connect to the DB
        db_connection = sqlite3.connect('./DB/FlaskApp.db')
        cursor = db_connection.cursor()

        # Enter Hash information in DB
        query = 'select sqlite_version();'
        cursor.execute(query)

        # Fetch result and output
        result = cursor.fetchall()
        print('SQLite Version is {}'.format(result))

    # Handle Errors
    except sqlite3.Error as error:

        print('Error Occured - ', error)

    # Close DB
    finally:

        if db_connection:
            db_connection.close()
            print('Database Connection closed')