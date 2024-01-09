import Client
import DB_Methods
import flaskapp
import Server_Methods
import Client_Requests
import time
import threading
import os
from JTRWorker import JTRWorker
from datetime import datetime
import pathlib


def run_server():

    flaskapp.app.run(port=5000)


def main():

    while True:
        print("1. Server")
        print("2. Client")
        print("3. Exit")

        option = int(input("Your choice: "))

        if option == 1:
            path = pathlib.Path("./john_hash_files")
            path.mkdir(exist_ok=True)
            path = pathlib.Path("./reports")
            path.mkdir(exist_ok=True)
            path = pathlib.Path("./DB")
            path.mkdir(exist_ok=True)
            path = pathlib.Path("./DB/FlaskApp_DB.db")
            if not path.is_file():
                DB_Methods.new_db()
            run_server()
        elif option == 2:
            path = pathlib.Path("./saved_files")
            Client.client_screen()
        elif option == 3:
            print("Exiting...")
            break
        else:
            print("Invalid Option:")



if __name__ == '__main__':

    main()
