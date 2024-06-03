from order import order
from authen import authen


class index:
    def start():
        flag = True
        print("WELCOME TO THE freshie-veggie STORE")
        while flag == True:
            choice = input("User or Admin or Exit? ")
            if choice == "user":
                order.ordering()
            elif choice == "admin":
                authen.authentication()
            elif choice == "exit":
                print("-- Exiting store --\n-- Thank you for visit! --")
                flag = False
            else:
                print("-- invalid input --")

    start()
