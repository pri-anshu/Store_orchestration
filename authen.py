import getpass
from new_user import new_user
from store_updating import store_updating


class authen:
    database = {"madee": "hahaha"}

    def authentication():
        trial = 0

        username = input("--> Enter your Username: ")
        password = getpass.getpass("--> Enter your password: ")

        if username in authen.database.keys():
            while trial < 2:
                if password == authen.database.get(username):
                    print("     ACCESS GRANTED\n\n")
                    authen.admin_usecase(username)
                    return
                else:
                    password = getpass.getpass("--> Enter your password again: ")
                    trial += 1
        else:
            print("-- Invalid username! --")
            exit(0)

    def admin_usecase(z):
        print(
            "System--> Select one from below options\n  -> 1. new user\n  -> 2. edit store"
        )
        flag = input("{}--> ".format(z))
        if flag == "new user":
            authen.database.update(new_user.new_user(z))
        elif flag == "edit store":
            store_updating.add_stock(z)
        else:
            print("System--> Invalid input")
