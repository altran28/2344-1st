"""Anthony Tran
PSID: 1957342
ZyLab 10.17"""


class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@ $' + str(self.item_price), '=',
              '$' + str(self.item_price * self.item_quantity))


if __name__ == "__main__":
    print("Item 1")

    name = input('Enter the item name:\n')
    price = int(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))

    first_item = ItemToPurchase(name, price, quantity)

    print("\nItem 2")

    name2 = input('Enter the item name:\n')
    price2 = int(input('Enter the item price:\n'))
    quantity2 = int(input('Enter the item quantity:\n'))

    second_item = ItemToPurchase(name2, price2, quantity2)

    print('\nTOTAL COST')
    first_item.print_item_cost()
    second_item.print_item_cost()
    total_cost = (price * quantity) + (price2 * quantity2)
    print("\nTotal: $" + str(total_cost))
