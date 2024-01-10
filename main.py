import DB_Methods
import flaskapp
import Server_Methods
import Client_Requests
import time
import threading
import os
from sys import stderr
from JTRWorker import JTRWorker
from datetime import datetime
import pathlib
import ClientGUI
import argparse


def run_server():

    flaskapp.app.run(port=5000)


def main():

    parser = argparse.ArgumentParser(description="An API made for security workers looking to send hashes to their cracking rig")

    parser.add_argument('instance', type=str, help="Choose whether to run the client or the server\n Example: python3 HashCrackAPI server / client")

    args = parser.parse_args()

    if args.instance == "server":

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
    elif args.instance == "client":
        path = pathlib.Path("./saved_files")
        path.mkdir(exist_ok=True)
        ClientGUI.window.mainloop()
    else:
        print("Required instance is invalid!\n Use \'python3 HashCrackAPI -h\' for help!", file=stderr)




if __name__ == '__main__':

    main()
