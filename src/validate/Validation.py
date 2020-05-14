from src.user.User import User


class Validation(User):
    def check_password(self):
        s = self.userPassword
        special = ",.#@$%&^*_-"
        flag = 1
        l = len(s)
        if any(i.isspace() for i in s):
            print("Inavalid Password!!")
            print("There shouldn't be any space!!")
        elif not (l >= 5):
            print("Inavalid Password!!")
            print("Password must contain atleast five characters!!")

        elif not (l <= 10):
            print("Inavalid Password!!")
            print("Password contains atmost ten characters!!")

        elif not (any(i.isdigit() for i in s)):
            print("Inavalid Password!!")
            print("Password must contains atleast one digit!!")

        elif not (any(i in special for i in s)):
            print("Inavalid Password!!")
            print("Password must contain atleast one special character!!")

        elif not (any(i.isupper() for i in s)):
            print("Inavalid Password!!")
            print("Password must contain atleast one upper case alphabet!!")

        elif not (any(i.islower() for i in s)):
            print("Inavalid Password!!")
            print("Password must contain atleast one lower case alphabet!!")

        else:
            print("Valid password")

    def check_Email(self):
        e = self.userEmail
        r = "abcdefghijklmnopqrstuvwxyz._0123456789/\*-"
        if "@" in e:
            t = e.partition("@")
            if all(i in r for i in t[0]):
                if all(j in r for j in t[2]) and (t[2].endswith(".com") or t[2].endswith(".in")):
                    print("Valid Email!!")
                else:
                    print("Invalid Email!!")

        else:
            print("Invalid Email!!")


obj = Validation("naman.gupta_cs18@gla.ac.in", "nA@33mn")
obj.check_Email()
obj.check_password()
