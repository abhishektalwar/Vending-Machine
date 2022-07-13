import time


class Item:
    """
    Class for initializing the Items
    """

    def __init__(self, name, code, price, quantity):
        self.name = name
        self.price = price
        self.code = code
        self.quantity = quantity

    def __str__(self):
        return self.name


class VendingMachine:
    """
    Class for vending machine
    """

    def __init__(self):
        candy_bar = Item(name="Candy Bar", code=1, price=200, quantity=10)
        chips = Item(name="Chips", code=2, price=150, quantity=10)
        soda = Item(name="Soda", code=3, price=100, quantity=5)
        self.items = [candy_bar, chips, soda]
        self.allowed_changes = [200, 100, 25, 10, 5]
        self.money_in_vending_machine = 0

    def display_menu(self):
        """
        Function to display the items
        :return:
        """
        for item in self.items:
            print(f"[{item.code}] - {item.name} = ${item.price / 100:.2f}")


def welcome_flush():
    """
    Function for Welcome Message
    :return:
    """
    for char in "Welcome to:\n--Neurotrack Vending Machine--\n":
        print(char, end='', flush=True)
        time.sleep(0.1)


def get_the_denominations(allowed_denominations, change):
    """
    Function for getting the exact denomination counts to be returned
    :param allowed_denominations:
    :param change:
    :return:
    """
    return_denominations_dict = {}
    for denomination in allowed_denominations:
        max_of_this_denomination = change // denomination
        change -= max_of_this_denomination * denomination
        return_denominations_dict[denomination] = max_of_this_denomination
    return return_denominations_dict


def main():
    """
    Main function to run
    :return:
    """
    welcome_flush()
    vending_machine = VendingMachine()
    vending_machine.display_menu()
    item_codes = [item.code for item in vending_machine.items]
    while True:
        try:
            user_input = int(input("Please enter the code of the item:"))
        except ValueError:
            print("Value has to be a number!!. Try Again!!")
            continue
        if user_input not in item_codes:
            print(f"Item for code : {user_input} is not available. Try again for the available items!")
            continue
        else:
            for item in vending_machine.items:
                if user_input == item.code:
                    selected_item = item
                    print(f"Selected Item: {selected_item} and its price is : ${selected_item.price / 100:.2f}\nLeft "
                          f"quantity for {selected_item}: {selected_item.quantity}")
                    while True:
                        try:
                            requested_quantity = int(input(f"Enter the quantity required for {selected_item}: "))
                        except ValueError:
                            print("Value has to be a number!!. Try Again!!")
                            continue
                        else:
                            if requested_quantity > selected_item.quantity:
                                print(f"Sorry only {selected_item.quantity} is left. Please select accordingly! ")
                            else:
                                selected_item.quantity -= requested_quantity
                                break
            break
    total_price_to_be_paid = selected_item.price * requested_quantity
    while vending_machine.money_in_vending_machine < total_price_to_be_paid:
        price_left_to_be_paid = total_price_to_be_paid - vending_machine.money_in_vending_machine
        print(f"Money inserted so far: {vending_machine.money_in_vending_machine}\nYou have to pay more:"
              f"${price_left_to_be_paid / 100:.2f}")
        while True:
            try:
                money_inserted = int(input(f"Enter the money:"))  # money to enter in cents value
            except ValueError:
                continue
            else:
                vending_machine.money_in_vending_machine += money_inserted
                break
    change_to_return = vending_machine.money_in_vending_machine - total_price_to_be_paid
    print(f"You have inserted extra: {change_to_return}")
    denominations_to_return = get_the_denominations(allowed_denominations=vending_machine.allowed_changes,
                                                    change=change_to_return)
    print(f"Please collect your change:\n{denominations_to_return}\n")
    print(f"After this transaction only {selected_item.quantity} {selected_item} is left !")


# Press the button in the gutter to run the script.
if __name__ == '__main__':
    main()
