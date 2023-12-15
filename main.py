import DB_Methods
import flaskapp
import Server_Methods
import Client
import time
import threading


def run_server():

    flaskapp.app.run(port=5000)


def main():

    server_worker = threading.Thread(target=run_server)

    server_worker.start()

    time.sleep(3)

    # auth = Server_Methods.add_user()

    Client.send_hash("HASHHAHSHASH", "raw-sha1", 'yV5QdlcKwOsatZI8CO_rneSdEhRxORdrhi6Y64fk2yA')


if __name__ == '__main__':

    main()
