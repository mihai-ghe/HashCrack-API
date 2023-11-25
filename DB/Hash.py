class Hash:

    value = None
    form = None
    cracked = False

    def __init__(self, value, form):

        self.value = value
        self.form = form

    def __str__(self):

        print("hash_object {", self.value, ':', self.form, '}')
