class User(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password


class BucketList(object):

    def __init__(self):

        self.bucketlists = {}

    def add_bucketlist(self, title):
        self.bucketlists.update({title: []})

    def edit_title(self, title, new_title):
        if title in self.bucketlists.keys():
            self.bucketlists[new_title] = self.bucketlists.pop(title)

    def add_items(self, title, item):
        if title in self.bucketlists.keys():
            self.bucketlists.update({title: item})

    # def edit_items(self, item, new_item):
    #         item_index = self.bucketlists.





