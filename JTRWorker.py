import subprocess
from threading import Thread
from time import sleep
from datetime import datetime
import DB_Methods


class JTRWorker(Thread):

    def __init__(self, wordlist_dict, hash_value, hash_form, hash_id):

        self.hash_id = hash_id
        self.hash_value = hash_value
        self.hash_form = hash_form
        self.plaintext = ''
        self.process = None
        self.output = ()
        self.wordlist_dict = wordlist_dict
        self.current_wordlist = None
        self.current_percentage = 0
        self.abort = False
        self.cracked = False
        Thread.__init__(self, daemon=True, args=wordlist_dict)

    def run(self):

        hash_file = f"./john_hash_files/hash_{datetime.today().strftime('%Y-%m-%d_%H:%M')}"

        with open(hash_file, 'w') as hash_fd:
            hash_fd.write('username:' + self.hash_value)

        for wordlist, percentage in self.wordlist_dict.items():

            if self.abort:
                return

            self.current_wordlist = wordlist

            wordlist_arg = "--wordlist=" + './wordlists/' + wordlist

            try:

                self.process = subprocess.Popen(['john', '--format=' + self.hash_form, wordlist_arg, hash_file], shell=False,
                                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

                self.output = self.process.communicate()[0].decode('utf-8')

                self.current_percentage += percentage

            except subprocess.CalledProcessError as Error:

                print("Error Occurred -", Error)
                print("Worker Crashed")
                self.abort = True

            for line in self.output.split('\n'):

                print(line)
                if "username" in line:

                    self.cracked = True
                    self.plaintext = line.split(' ', maxsplit=1)[0]

                    DB_Methods.update_hash_data('Plaintext', self.plaintext, self.hash_id)

                    break

            if self.cracked:
                self.abort = True

            sleep(3)

        DB_Methods.update_hash_data('Plaintext', 'Done - No Match Found', self.hash_id)

        self.abort = True

    def stop(self):

        if not self.process and not self.process.poll():

            self.process.terminate()

            self.abort = True

        else:

            self.abort = True

    def get_status(self):

        if not self.cracked:

            if self.abort:

                return "Progress: Completed; No Matches Found"

            else:
                return "Progress: %.2f; Current Wordlist: %s" % (self.current_percentage, self.current_wordlist)

        else:

            return "Progress: Completed; Match in Wordlist: %s" % self.current_wordlist
