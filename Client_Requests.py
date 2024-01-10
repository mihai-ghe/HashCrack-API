import requests


# Send hash to DB and start cracking
def send_hash(value, form, auth, host):

    url = host + "/send"

    json = {'hash': value, 'format': form}

    headers = {'Authorization': 'Bearer ' + auth}

    response = None

    try:

        response = requests.post(url, json=json, headers=headers)

    except requests.ConnectionError as Error:

        return f"Could not connect to host: {Error}"

    finally:
        if response.status_code == 401:
            return "Invalid API Authorization Key!"
        else:
            return response.text


# Check if hash has entry in DB
def check(value, auth, host):

    url = host + "/check"

    params = {'hash':  value}

    headers = {'Authorization': 'Bearer ' + auth}

    response = None

    try:

        response = requests.get(url, params=params, headers=headers)

    except requests.ConnectionError as Error:

        return f"Could not connect to host: {Error}"

    finally:
        if response.status_code == 401:
            return "Invalid API Authorization Key!"
        else:
            return response.text


# Terminate a cracking thread
def end(auth, host, hash_value=None, hash_id=None):

    url = host + "/end"

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

        return f"Could not connect to host: {Error}"

    finally:
        if response.status_code == 401:
            return "Invalid API Authorization Key!"
        else:
            return response.text


def get_all(file_format, auth, host):

    url = host + "/all"

    params = {'format':  file_format}

    headers = {'Authorization': 'Bearer ' + auth}

    response = None

    try:

        response = requests.get(url, params=params, headers=headers)

    except requests.ConnectionError as Error:

        return f"Could not connect to host: {Error}"

    finally:
        if response.status_code == 401:
            return "Invalid API Authorization Key!"
        else:

            filename = response.headers.get('content-disposition').split('=')[1].replace('\"', '')

            with open(f"./saved_files/{filename}", "wb") as downloaded_file:
                for chunk in response.iter_content():
                    downloaded_file.write(chunk)

            return "Saved file in ./saved_files!"


def start(auth, host, hash_value=None, hash_id=None):

    url = host + "/start"

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

        return f"Could not connect to host: {Error}"

    finally:
        if response.status_code == 401:
            return "Invalid API Authorization Key!"
        else:
            return response.text


def get_status(auth, host, hash_value=None, hash_id=None):

    url = host + "/status"

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

        return f"Could not connect to host: {Error}"

    finally:
        if response.status_code == 401:
            return "Invalid API Authorization Key!"
        else:
            return response.text
