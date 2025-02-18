class User:
    """class User"""

    def __init__(self, username, password):
        print("initializing User")
        self.username = username
        self.password = password

    def show_user(self):
        return f"User: {self.username}"
