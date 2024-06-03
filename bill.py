from tabulate import tabulate


class bill:
    slip = {}

    def add_to_bill(name, quan, price):
        bill.slip[name.upper()] = quan, price
        head = ["Item", "Quantity", "Rate"]
        table = []
        for key, values in bill.slip.items():
            table.append([key] + list(values))
        print(tabulate(table, headers=head, tablefmt="grid"))

    def display_bill():
        head = ["Item", "Quantity", "Rate"]
        table = []
        for key, values in bill.slip.items():
            table.append([key] + list(values))

        sum = 0
        for i in bill.slip:
            sum = sum + bill.slip[i][1]
        table.append(["TOTAL PRICE"] + [""] + [sum])
        print("\nGenerating bill")
        print(tabulate(table, headers=head, tablefmt="grid"))
        print("Thank you for shopping")
        exit(0)
