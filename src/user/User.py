class User:
    def __init__(self, userName, userEmail, userPassword):
        self.userName = userName
        self.userEmail = userEmail
        self.userPassword = userPassword

    def get_userName(self):
        return self.userName

    def set_userName(self, userName):
        self.userName = userName
