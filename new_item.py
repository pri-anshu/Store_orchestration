from data import *

class new_item:
    def add_new_item(item, z):
        print("System--> Item not found in the store.")
        print("System--> Do you wish to add new item?")
        temp = input("{}--> ".format(z))
        if temp == "yes":
            print("System--> Enter the quantity to be added-")
            quan = int(input("{}--> ".format(z)))
            if quan <= 0:
                print("System--> Can not add 0 item to stock")
            else:
                data.stock.update({item: quan})
                print("System--> Enter the price of item-")
                price = int(input("{}--> ".format(z)))
                data.shelf.update({item: price})

        elif temp == "no":
            print("-- Exiting, Thank you --")
            exit(0)
        else:
            print("System--> invalid input")
