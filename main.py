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


def run_server():

    flaskapp.app.run(port=5000)


def main():

    while True:
        print("1. Server")
        print("2. Client")
        print("3. Exit")

        option = int(input("Your choice: "))

        if option == 1:
            run_server()
        elif option == 2:
            Client.client_screen()
        elif option == 3:
            print("Exiting...")
            break
        else:
            print("Invalid Option:")


if __name__ == '__main__':

    main()
