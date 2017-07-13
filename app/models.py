class User(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password


class BucketList(object):

    bucketlists = {}

    def addtitle(self, title):
        if title in self.bucketlists.keys():
            return False
        else:
            self.bucketlists.update({title: []})
            return True

    def additems(self, title, item):
        if title in self.bucketlists.keys():
            self.bucketlists.update({title: item})
            return True
        return False

    def edittitle(self, title, new_title):
        if title in self.bucketlists.keys():
            self.bucketlists[new_title] = self.bucketlists.pop(title)
            return True
        return False

    def edit_items(self, item, new_item):
        pass

    def deletelist(self, title):
        if title in self.bucketlists.keys():
            del(self.bucketlists[title])
            return True
        return False

    def deleteitem(self, title, item):
        pass

