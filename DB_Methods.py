import sqlite3


def enter_hash(hash_value, hash_type, user_id):

    db_connection = None

    query = "INSERT INTO Hashes (Hash, Type, User_ID) VALUES (?, ?, ?);"

    values = (hash_value, hash_type, user_id)

    try:

        # Connect to the DB
        db_connection = sqlite3.connect('./DB/FlaskApp_DB.db')
        cursor = db_connection.cursor()

        # Enter Hash information in DB
        cursor.execute(query, values)

        # Fetch result and print it
        result = cursor.fetchall()
        db_connection.commit()
        # print('SQL Response is {}'.format(result))

    # Handle Errors
    except sqlite3.Error as Error:

        print('Error Occurred -', Error)

    # Close DB
    finally:

        if db_connection:
            db_connection.close()


def check_hash(value):

    db_connection = None

    query = "SELECT * FROM Hashes WHERE Hash = %s;" % value

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


def check_key(api_key):

    db_connection = None

    result = None

    query = f"SELECT * FROM Users WHERE API_Key = '{api_key}'"

    try:

        # Connect to the DB
        db_connection = sqlite3.connect('./DB/FlaskApp_DB.db')
        cursor = db_connection.cursor()

        # Add User to the DB
        cursor.execute(query)

        # Fetch result and print it
        result = cursor.fetchall()

    except sqlite3.Error as Error:

        print('Error Occurred -', Error)

    finally:

        if db_connection:
            db_connection.close()

    # print(result)

    if result:
        return result
    else:
        return None


# Add a new user to the DB
def add_user(username, key):

    # Note: Before adding new users check the user related to the current API Key
    # Only the admin should have the ability to add new Users

    rvalue = 0

    db_connection = None

    query = "INSERT INTO Users(UserName, API_Key) VALUES(?, ?);"

    values = (username, key)

    try:

        # Connect to the DB
        db_connection = sqlite3.connect('./DB/FlaskApp_DB.db')
        cursor = db_connection.cursor()

        # Add User to the DB
        cursor.execute(query, values)
        db_connection.commit()

        # Fetch result and print it
        result = cursor.fetchall()
        print('SQL Response is {}'.format(result))

    except sqlite3.Error as Error:

        print('Error Occurred -', Error)
        rvalue = 1

    finally:

        if db_connection:
            db_connection.close()

    return rvalue
