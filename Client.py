import requests


# Send hash to DB and start cracking
def send_hash(value, form, auth):

    url = "http://localhost:5000/send"

    json = {'hash': value, 'format': form}

    headers = {'Authorization': 'Bearer ' + auth}

    response = None

    try:

        response = requests.post(url, json=json, headers=headers)

    except requests.ConnectionError as Error:

        print("Could not connect to host:", Error)
        exit()

    finally:
        if response:
            print(response)


# Get progress of current cracking threads
def cracking_status():

    url = "http://localhost:5000/status"

    response = None

    try:

        response = requests.get(url)

    except requests.ConnectionError as Error:

        print("Could not connect to host:", Error)
        exit()

    finally:
        if response:
            print(response)


# Check if hash has entry in DB
def check(value):

    url = "http://localhost:5000/check"

    params = {'hash':  value}

    response = None

    try:

        response = requests.get(url, params=params)

    except requests.ConnectionError as Error:

        print("Could not connect to host:", Error)
        exit()

    finally:
        if response:
            print(response)


# Terminate a cracking thread
def end(thread_id):

    url = "http://localhost:5000/end"

    params = {'id': thread_id}

    response = None

    try:

        response = requests.put(url, params=params)

    except requests.ConnectionError as Error:

        print("Could not connect to host:", Error)
        exit()

    finally:
        if response:
            print(response)
