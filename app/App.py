from .models import User


class App:
    def __init__(self):
        self.users = {}

    def validate_on_signup(self, username, password):
        user = User(username, password)
        if username in self.users.keys():
            return False
        else:
            self.users.update({username: user})
            return True

    def validate_on_signin(self, username, password):
        if username in self.users.keys():
            if self.users[username].password == password:
                return True
        else:
            return False

    def signout(self):
        pass
