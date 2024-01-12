import DB_Methods
import flaskapp
import threading
from sys import stderr
import pathlib
import argparse
import Server_Methods
import time
from ClientGUI import window


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

        server_thread = threading.Thread(target=run_server)

        server_thread.start()

        window.withdraw()

        time.sleep(2)

        while True:
            print("Hash-Crack_API Server")
            print("1. Add a new user")
            print("Press CTRL+C to quit")

            option = input("Your option: ")

            if option == "1":
                Server_Methods.add_user()
            else:
                print("Invalid option!")
                continue

    elif args.instance == "client":

        path = pathlib.Path("./saved_files")
        path.mkdir(exist_ok=True)
        window.mainloop()

    else:
        print("Required instance is invalid!\n Use \'python3 HashCrackAPI -h\' for help!", file=stderr)


if __name__ == '__main__':

    main()
