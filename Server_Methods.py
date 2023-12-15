import secrets
import DB_Methods


def add_user():

    username = input("Enter the new user's username: ")

    # Generate new API Key and make sure it is not a duplicate

    while True:

        new_api_key = secrets.token_urlsafe(32)

        if DB_Methods.check_key(new_api_key):

            continue

        else:

            break

    # Communicate the u

    print(f"The new user's API Key is: {new_api_key}\n"
          f"Save it somewhere secure, as you will need to use"
          f"it whenever you make a request to the API")

    res = DB_Methods.add_user(username, new_api_key)

    if res:
        print("Error Occurred during DB interaction!\n"
              "User was not added...")

    return new_api_key
