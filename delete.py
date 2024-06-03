from bill import bill


class delete:
    def remove_item():
        print("Please enter the item you would like to delete-")
        item = input("- ")
        if item in bill.slip:
            bill.slip.pop(item)
            print("Removing ", item, " from the bill.")

        else:
            print("Item not found in bill")
