import Client_Requests
from ClientGUI import entry_1, entry_2, entry_3, entry_4, entry_5, entry_6, entry_7


def client_screen():

    print("\n")
    print("----------HashCrack API Client----------")
    key = input("Enter your API Key: ")

    while True:

        print("Select what you would like to do:")
        print("1. Add a hash")
        print("2. Check to see if a hash exists")
        print("3. Get a file containing all hashes")
        print("4. Start the Cracking Process for a specific hash")
        print("5. Get the status of a/all hashes")
        print("6. Stop the Cracking Process for a specific hash")
        print("7. Exit")

        choice = int(input("Your Choice: "))

        if choice == 1:
            add_hash(key)
            continue
        elif choice == 2:
            check_hash(key)
            continue
        elif choice == 3:
            get_all(key)
            continue
        elif choice == 4:
            start(key)
            continue
        elif choice == 5:
            status(key)
            continue
        elif choice == 6:
            stop(key)
            continue
        elif choice == 7:
            print("Exiting...")
            break


def add_hash(auth):

    hash_value = input("Enter the hash: ")
    hash_form = input("Enter the hash format: ")

    Client_Requests.send_hash(hash_value, hash_form, auth)


def check_hash(auth):

    hash_value = input("Enter the hash: ")

    Client_Requests.check(hash_value, auth)


def get_all(auth):

    file_format = input("Enter the file format for the hash file: ")

    if file_format == 'csv':
        Client_Requests.get_all('csv', auth)
    else:
        Client_Requests.get_all('raw', auth)


def start(auth):

    hash_value = input("Enter the hash: ")
    hash_id = input("Enter the hash id: ")

    Client_Requests.start(auth, hash_value, hash_id)


def status(auth):

    hash_value = input("Enter the hash: ")
    hash_id = input("Enter the hash id: ")

    Client_Requests.get_status(auth, hash_value, hash_id)


def stop(auth):

    hash_value = input("Enter the hash: ")
    hash_id = input("Enter the hash id: ")

    Client_Requests.end(auth, hash_value, hash_id)
