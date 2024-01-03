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
            print(response.text)


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
def check(value, auth):

    url = "http://localhost:5000/check"

    params = {'hash':  value}

    headers = {'Authorization': 'Bearer ' + auth}

    response = None

    try:

        response = requests.get(url, params=params, headers=headers)

    except requests.ConnectionError as Error:

        print("Could not connect to host:", Error)
        exit()

    finally:
        if response.status_code == 401:
            print("Invalid API Authorization Key")
        else:
            print(response.text)


# Terminate a cracking thread
def end(auth, hash_value=None, hash_id=None):

    url = "http://localhost:5000/end"

    params = None

    if hash_id:
        params = {'id': hash_id}
    elif hash_value:
        params = {'hash': hash_value}

    headers = {'Authorization': 'Bearer ' + auth}

    response = None

    try:

        response = requests.put(url, params=params, headers=headers)

    except requests.ConnectionError as Error:

        print("Could not connect to host:", Error)
        exit()

    finally:
        if response:
            print(response.text)


def get_all(file_format, auth):

    url = "http://localhost:5000/all"

    params = {'format':  file_format}

    headers = {'Authorization': 'Bearer ' + auth}

    response = None

    try:

        response = requests.get(url, params=params, headers=headers)

    except requests.ConnectionError as Error:

        print("Could not connect to host:", Error)
        exit()

    finally:
        if response.status_code == 401:
            print("Invalid API Authorization Key")
        else:

            filename = response.headers.get('content-disposition').split('=')[1].replace('\"', '')

            with open(f"./saved_files/{filename}", "wb") as downloaded_file:
                for chunk in response.iter_content():
                    downloaded_file.write(chunk)


def start(auth, hash_value=None, hash_id=None):

    url = "http://localhost:5000/start"

    params = None

    if hash_value:
        params = {'hash': hash_value}
    elif hash_id:
        params = {'id': hash_id}

    headers = {'Authorization': 'Bearer ' + auth}

    response = None

    try:

        response = requests.put(url, params=params, headers=headers)

    except requests.ConnectionError as Error:

        print("Could not connect to host:", Error)
        exit()

    finally:
        if response:
            print(response.text)


def get_status(auth, hash_value=None, hash_id=None):

    url = "http://localhost:5000/status"

    params = None

    if hash_value:
        params = {'hash': hash_value}
    elif hash_id:
        params = {'id': hash_id}

    headers = {'Authorization': 'Bearer ' + auth}

    response = None

    try:

        if not params:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url, params=params, headers=headers)

    except requests.ConnectionError as Error:

        print("Could not connect to host:", Error)
        exit()

    finally:
        if response:
            print(response.text)
