class User(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password


class BucketList(object):

    def __init__(self, title, activities):
        self.title = title
        self.activities = activities
        self.items =[]

    def add_list(self):
        pass

    def add_items(self):
        pass


