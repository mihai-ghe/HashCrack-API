# import flask module
from flask import Flask, request, make_response, send_file
from datetime import datetime
import csv
import DB_Methods
import os
from JTRWorker import JTRWorker

# create instance of flask application
app = Flask(__name__)

worker_dictionary = {}


def build_wordlist_dictionary():

    percentage_dict = {}

    folderpath = "./wordlists"

    total_size = 0
    total_percentage = 0

    for path, dirs, files in os.walk(folderpath):
        for file in files:
            filepath = os.path.join(path, file)
            file_size = os.path.getsize(filepath)

            percentage_dict[file] = file_size
            total_size += file_size

    for file in percentage_dict.keys():
        percentage_dict[file] = (100 * percentage_dict[file]) / total_size

    for file, percentage in percentage_dict.items():

        total_percentage += percentage

    return percentage_dict


# Send Hashes to the DB
@app.route("/send", methods=["POST"])
def send():

    key = request.authorization.token
    user_data = DB_Methods.check_key(key)

    if not user_data:

        response = make_response('Not Authorized!', 401)

    else:

        json = request.json
        DB_Methods.enter_hash(json['hash'], json['format'], user_data[0][0])
        response = make_response('Added hash to Database', 201)

    response.content_type = 'text/plain'
    return response


# Get status of ongoing cracking threads
@app.route("/status", methods=['GET'])
def status():

    key = request.authorization.token
    user_data = DB_Methods.check_key(key)

    if not user_data:

        response = make_response("Not Authorized!", 401)

    else:

        user_id = user_data[0][0]

        hash_value = request.args.get('hash')
        hash_id = request.args.get('id')

        if hash_id and hash_value:
            response = make_response("Bad Request!", 400)

        elif not hash_id and not hash_value:

            user_hashes = DB_Methods.check_hash(user_id=user_id)

            if not user_hashes:

                response = make_response("No hashes found!", 404)

            else:

                message = ''

                for hash_data in user_hashes:

                    if hash_data[3] == "In Progress":
                        progress = worker_dictionary[hash_data[0]].get_status()
                        message += f"ID: {hash_data[0]}, hash: {hash_data[1]}, format: {hash_data[2]}, plaintext: {hash_data[3]}, {progress}\n"
                    else:
                        message += f"ID: {hash_data[0]}, hash: {hash_data[1]}, format: {hash_data[2]}, plaintext: {hash_data[3]}\n"

                response = make_response(message, 200)

        else:

            hash_data = None

            if hash_value:
                hash_data = DB_Methods.check_hash(value=hash_value)
            elif hash_id:
                hash_data = DB_Methods.check_hash(hash_id=hash_id)

            if not hash_data:

                response = make_response("No such hash found!", 404)

            else:

                if hash_data[0][3] == "In Progress":
                    progress = worker_dictionary[hash_data[0][0]].get_status()
                    # print(progress + 'PROGRESS HERE')
                    message = f"ID: {hash_data[0][0]}, hash: {hash_data[0][1]}, format: {hash_data[0][2]}, plaintext: {hash_data[0][3]}, {progress}\n"
                else:
                    message = f"ID: {hash_data[0][0]}, hash: {hash_data[0][1]}, format: {hash_data[0][2]}, plaintext: {hash_data[0][3]}\n"

                response = make_response(message, 200)

    response.content_type = "text/plain"
    return response


# Check whether the respective hash has an entry in the DB
@app.route("/check", methods=['GET'])
def check():

    key = request.authorization.token
    user_data = DB_Methods.check_key(key)

    message = 'Not Authorized!'

    if not user_data:

        response = make_response(message, 401)
        response.content_type = 'text/plain'
        return response

    hash_value = request.args.get('hash')
    result = DB_Methods.check_hash(value=hash_value)

    if result:

        message = f"ID: {result[0][0]}, hash: {result[0][1]}, format: {result[0][2]}, plaintext: {result[0][3]}"
        response = make_response(message, 200)

    else:

        message = f"This hash does not have a DB entry: {hash_value}"
        response = make_response(message, 200)

    response.content_type = 'text/plain'
    return response


@app.route("/all", methods=['GET'])
def get_all():

    key = request.authorization.token
    user_data = DB_Methods.check_key(key)

    if not user_data:

        response = make_response("Not Authorized!", 401)
        response.content_type = 'text/plain'
        return response

    file_format = request.args.get('format')
    result = DB_Methods.get_all()

    if not result:

        response = make_response("No Entries", 200)

    else:

        now = datetime.today().strftime('%Y-%m-%d_%H:%M')

        if file_format == 'csv':

            filepath = f'./reports/{now}.csv'

            fieldnames = ['ID', 'hash', 'format', 'plaintext', 'User_ID']

            with open(filepath, 'w') as csv_hash_list:

                writer = csv.writer(csv_hash_list)
                writer.writerow(fieldnames)
                writer.writerows(result)

            return send_file(filepath, download_name=f'{now}.csv')

        else:

            filepath = f"./reports/{now}.txt"

            for index in range(len(result)):
                result[index] = f"ID: {result[index][0]}, hash: {result[index][1]}, format: {result[index][2]}, plaintext: {result[index][3]}, User_ID: {result[index][4]}\n"

            with open(filepath, "w") as hash_list:
                hash_list.writelines(result)

            return send_file(filepath, download_name=f'{now}.txt')

    response.content_type = 'text/plain'
    return response


@app.route("/start", methods=['PUT'])
def start():

    key = request.authorization.token
    user_data = DB_Methods.check_key(key)

    if not user_data:

        response = make_response("Not Authorized!", 401)

    else:

        user_id = user_data[0][0]

        hash_value = request.args.get('hash')
        hash_id = request.args.get('id')

        if (hash_id and hash_value) or (not hash_id and not hash_value):
            response = make_response("Bad Request!", 400)

        else:

            hash_data = None

            if hash_value:
                hash_data = DB_Methods.check_hash(value=hash_value)
            elif hash_id:
                hash_data = DB_Methods.check_hash(hash_id=hash_id)

            if not hash_data:

                response = make_response("No such hash found!", 404)

            else:

                hash_id = hash_data[0][0]
                hash_uid = hash_data[0][4]
                hash_value = hash_data[0][1]
                hash_form = hash_data[0][2]

                if hash_uid != user_id:

                    response = make_response("You do not own this hash!", 403)

                else:

                    wordlist_dictionary = build_wordlist_dictionary()

                    new_worker = JTRWorker(wordlist_dictionary, hash_value, hash_form, hash_id)

                    new_worker.start()

                    worker_dictionary[hash_id] = new_worker

                    DB_Methods.update_hash_data('Plaintext', 'In Progress', hash_id)

                    response = make_response("Started Cracking Process!", 200)

    response.content_type = "text/plain"
    return response


# Terminate a cracking thread
@app.route("/end", methods=['PUT'])
def end():

    key = request.authorization.token
    user_data = DB_Methods.check_key(key)

    if not user_data:

        response = make_response("Not Authorized!", 401)

    else:

        user_id = user_data[0][0]

        hash_value = request.args.get('hash')
        hash_id = request.args.get('id')

        if (hash_id and hash_value) or (not hash_id and not hash_value):
            response = make_response("Bad Request!", 400)

        else:

            hash_data = None

            if hash_value:
                hash_data = DB_Methods.check_hash(hash_value)
            elif hash_id:
                hash_data = DB_Methods.check_hash(hash_id)

            if not hash_data:

                response = make_response("No such hash found!", 404)

            else:

                hash_id = hash_data[0][0]
                hash_uid = hash_data[0][4]

                if hash_uid != user_id:

                    response = make_response("You do not own this hash!", 403)

                else:

                    worker_dictionary[hash_id].stop()

                    del worker_dictionary[hash_id]

                    DB_Methods.update_hash_data('Plaintext', 'Stopped', hash_id)

                    response = make_response("Stopped Cracking Process!", 200)

    response.content_type = "text/plain"
    return response
