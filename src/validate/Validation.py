class Validation:
    def __init__(self, userEmail, userPassword):
        self.userEmail = userEmail
        self.userPassword = userPassword

    def check_password(userPassword):
        input_password = input("Enter the password: ")


obj_validation = Validation()


def check_Email(userEmail):
    e = userEmail
    r = "abcdefghijklmnopqrstuvwxyz._0123456789/\*-"
    if "@" in e:
        t = e.partition("@")
        if all(i in r for i in t[0]):
            if all(j in r for j in t[2]) and (t[2].endswith(".com") or t[2].endswith(".in")):

                return True


            else:
                print("Invalid Email!!")
                return False

    else:
        print("Invalid Email!!")

        return False
