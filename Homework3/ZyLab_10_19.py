"""Anthony Tran
PSID: 1957342
ZyLab 10.19"""


class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        output = self.item_name, self.item_quantity, '@ $' + str(self.item_price), '=', '$' + str(
            self.item_price * self.item_quantity)
        output_cost = self.item_quantity * self.item_price
        return output, output_cost

    def print_item_description(self):
        output = '{}: {}, %d oz.'.format(self.item_name, self.item_description, self.item_quantity)
        print(output)
        return output


class ShoppingCart:
    def __init__(self, int_customer_name='none', int_current_date='January 1, 2016', cart_items=None):
        if cart_items is None:
            cart_items = []
        self.customer_name = int_customer_name
        self.current_date = int_current_date
        self.cart_items = cart_items

    def add_item(self, var):
        self.cart_items.append(var)

    def remove_item(self):
        print('REMOVE ITEM FROM CART')
        string = str(input('Enter name of item to remove:\n'))
        check = False
        for item in self.cart_items:
            if item.item_name == string:
                self.cart_items.remove(item)
                check = True
                break
            else:
                check = False
        if not check:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self):
        print('CHANGE ITEM QUANTITY')

        name = str(input('Enter the item name:\n'))
        check = False
        for item in self.cart_items:
            if item.item_name == name:
                new_quantity = int(input('Enter the new quantity:\n'))
                item.item_quantity = new_quantity
                check = True
                break
            else:
                check = False
        if not check:
            int(input('Enter the new quantity:\n'))
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        num_cart = 0
        for var in self.cart_items:
            num_cart = num_cart + var.item_quantity
        return num_cart

    def get_cost_of_cart(self):
        cost_cart = 0
        for var in self.cart_items:
            cost_calc = (var.item_quantity * var.item_price)
            cost_cart += cost_calc
        return cost_cart

    def print_total(self):
        print('OUTPUT SHOPPING CART')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('Number of Items:', self.get_num_items_in_cart())
        print()
        total = 0
        for var in self.cart_items:
            print(var.item_name, var.item_quantity, '@ $' + str(var.item_price), '=', '$' + str(
                var.item_price * var.item_quantity))
            total += (var.item_quantity * var.item_price)

        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        print()
        print('Total: $' + str(total))

    def print_descriptions(self):
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        print(self.customer_name + '\'s Shopping Cart - ' + self.current_date.format(end='\n'))
        print('\nItem Descriptions')

        for var in self.cart_items:
            print(var.item_name + ': ' + var.item_description)



def print_menu(cart_select):
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            'i - Output items\' descriptions\n'
            'o - Output shopping cart\n'
            'q - Quit\n')

    select = ''
    while select != 'q':
        print(menu)
        select = input('Choose an option:\n')
        while select != 'a' and select != 'r' and select != 'c' \
                and select != 'i' and select != 'o' and select != 'q':
            select = input('Choose an option:\n')

        if select == 'a':
            print('ADD ITEM TO CART')
            item_name = str(input('Enter the item name:\n'))
            item_description = str(input('Enter the item description:\n'))
            item_price = int(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))
            var = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart_select.add_item(var)

        if select == 'o':
            cart_select.print_total()
        elif select == 'i':
            cart_select.print_descriptions()
        elif select == 'r':
            cart_select.remove_item()
        elif select == 'c':
            cart_select.modify_item()


if __name__ == '__main__':
    customer_name = str(input('Enter customer\'s name:\n'))
    current_date = str(input('Enter today\'s date:\n'))
    print('\nCustomer name:', customer_name)
    print('Today\'s date:', current_date)
    c_info = ShoppingCart(customer_name, current_date)
    print_menu(c_info)
