from data import *
from home import product
from bill import bill
from delete import delete


class order:
    def ordering():
        key_list = [i for i in data.stock]

        loop = True
        while loop == True:
            run = True
            while run == True:
                print("\nItems avaiable in store-")
                for products in range(len(key_list) - 1):
                    print(key_list[products].upper(), end=", ")
                print(key_list[-1].upper(), "\n")

                print("Enter the item that is to be ordered")
                a = input("- ")
                if a not in data.shelf:
                    print("Item not found in the store, try different item.")
                else:
                    print(
                        "Item found,\n",
                        "Priced at- ",
                        data.shelf.get(a),
                        "\n",
                        "Quantity available- ",
                        data.stock.get(a),
                    )
                    run = False
            print("Enter the required quantity")
            b = int(input("- "))
            if b > data.stock.get(a):
                print("Sorry requied quantity isn't available")
                print("Quantity available- ", data.stock.get(a))
            elif b == 0:
                print("item not added")
            else:
                item = product(a, data.shelf.get(a), b)
                item()
                print("Do you wish to continue?")
                choice = input("- ")
                if choice == "yes":
                    loop = True
                elif choice == "no":
                    loop = False
                    print("Would you like to delete any item from order?")
                    order = input("- ")
                    if order == "yes":
                        delete.remove_item()
                    else:
                        pass
                    bill.display_bill()
