class User:
    def __init__(self, userEmail, userPassword):
        self.userEmail = userEmail
        self.userPassword = userPassword

    def get_userEmail(self):
        return self.userEmail

    def set_userEmail(self, userEmail):
        self.userEmail = userEmail

    def get_userPassword(self):
        return self.userPassword

    def set_userPassword(self, userPassword):
        self.userPassword = userPassword