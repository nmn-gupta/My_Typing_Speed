class Validation:
    def __init__(self, userEmail, userPassword):
        self.userEmail = userEmail
        self.userPassword = userPassword

    def check_password(userPassword):
        s = userPassword
        special = ",.#@$%&^*_-"
        flag = 1
        l = len(s)
        if any(i.isspace() for i in s):
            print("Inavalid Password!!")
            print("There shouldn't be any space!!")
            return False


        elif not (l >= 5):
            print("Inavalid Password!!")
            print("Password must contain atleast five characters!!")
            return False


        elif not (l <= 10):
            print("Inavalid Password!!")
            print("Password contains atmost ten characters!!")
            return False


        elif not (any(i.isdigit() for i in s)):
            print("Inavalid Password!!")
            print("Password must contains atleast one digit!!")
            return False

        elif not (any(i in special for i in s)):
            print("Inavalid Password!!")
            print("Password must contain atleast one special character!!")
            return False

        elif not (any(i.isupper() for i in s)):
            print("Inavalid Password!!")
            print("Password must contain atleast one upper case alphabet!!")
            return False


        elif not (any(i.islower() for i in s)):
            print("Inavalid Password!!")
            print("Password must contain atleast one lower case alphabet!!")
            return False


        else:
            return True


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
