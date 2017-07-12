class User(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password


class BucketList(object):

    def __init__(self):

        self.items = {}

    def add_bucketlist(self, title):
        self.items.update({title: []})

    def edit_title(self, title):
        if title in self.items.keys():
            pass

    def add_items(self, title, item):
        if title in self.items.keys():
            self.items.update({title: item})

    def edit_items(self, item):
        if item in self.items.values():
            self.items.update({})




