import sqlite3
import Hash
import secrets


def enter_hash(hash_obj):

    db_connection = None

    query = "INSERT INTO Hashes (Hash, Type) VALUES (%s, %s);"

    values = (hash_obj.value, hash_obj.form)

    try:

        # Connect to the DB
        db_connection = sqlite3.connect('./DB/FlaskApp_DB.db')
        cursor = db_connection.cursor()

        # Enter Hash information in DB
        cursor.execute(query)

        # Fetch result and print it
        result = cursor.fetchall()
        print('SQL Response is {}'.format(result))

    # Handle Errors
    except sqlite3.Error as Error:

        print('Error Occurred -', Error)

    # Close DB
    finally:

        if db_connection:
            db_connection.close()


def check_hash(value):

    db_connection = None

    query = "SELECT * FROM Hashes WHERE Hash = %s;"

    values = (value)

    try:

        # Connect to the DB
        db_connection = sqlite3.connect('./DB/FlaskApp_DB.db')
        cursor = db_connection.cursor()

        # Enter Hash information in DB
        cursor.execute(query)

        # Fetch result and print it
        result = cursor.fetchall()
        print('SQL Response is {}'.format(result))

    # Handle Errors
    except sqlite3.Error as Error:

        print('Error Occurred -', Error)

    # Close DB
    finally:

        if db_connection:
            db_connection.close()


# Add a new user to the DB
def add_user(username):

    # Note: Before adding new users check the user related to the current API Key
    # Only the admin should have the ability to add new Users

    new_api_key = secrets.token_urlsafe(32)

    print(f"The new user's API Key is: {new_api_key}\n"
          f"Save it somewhere secure, as you will need to use"
          f"it whenever you make a request to the API")

    db_connection = None

    query = "INSERT INTO Users (UserName, API_Key) VALUES (%s, %s);"

    values = (username, new_api_key)

    try:

        # Connect to the DB
        db_connection = sqlite3.connect('./DB/FlaskApp_DB.db')
        cursor = db_connection.cursor()

        # Add User to the DB
        cursor.execute(query)

        # Fetch result and print it
        result = cursor.fetchall()
        print('SQL Response is {}'.format(result))

    except sqlite3.Error() as Error:

        print('Error Occurred -', Error)

    finally:

        if db_connection:
            db_connection.close()
