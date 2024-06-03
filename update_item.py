from data import *

class update_item:
    def add_items(item, z):
        print("System--> Enter the quantity to be added-")
        value = int(input("{}--> ".format(z)))
        quan = data.stock.get(item) + value
        data.stock.update({item: quan})

        print("System--> Do you wish to update the price?")
        temp = input("{}--> ".format(z))
        if temp == "yes":
            price = input("System--> Enter the price of the item:")
            data.shelf.update({item: price})
        else:
            print("System--> Adding item to stock without updating price")
