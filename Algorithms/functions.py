#containers
menuItems = ['Strawberry Short Cake', 'Cheesecake', 'Moon Cake', 'Egg Tart']
cart = [] #empty cart

#Displaying items in containers. 
def displayItems(l: list):
    if l == cart:
        print('\n\n--- Your cart ---\n')
    elif l == menuItems:
        print('\n\n--- Menu Items ---\n')
    item = 0
    for i in l:
        item+=1
        print(item, '.', i)

# staff()
def staff():
    displayItems(menuItems)
    print('\ni - Inserting new item.')
    print('d - Deleting an existing item.')
    print('e - Editting an existing item.')
    print('n - Non.')
    select = input('Do you want to change anything on the menu?: ')
    while select.lower() != 'n':
        if select.lower() == 'i':
            item = input('\nAdding new item to the menu.\nPlease enter new item name: ')
            item-=1
            menuItems.append(item)
        elif select.lower() == 'd':
            index = int(input('\nDeleting an existing item.\nPlease enter the index of the item: '))
            if index <= len(menuItems) and index >-1:
                menuItems.pop(index)
            else:
                print('OUT OF RANGE')
        elif select.lower() == 'e':
            pass
        else:
            print('\bWrong input')
        displayItems(menuItems)
        print('\ni - Inserting new item.')
        print('d - Deleting an existing item.')
        print('e - Editting an existing item.')
        print('n - Non.')
        select = input('Do you want to change anything on the menu?: ')

# customer()
def customer():
    displayItems(menuItems)
    print('\na - Adding an item to cart.')
    print('r - Removing an item from cart.')
    print('t - Total of items in the cart.')
    print('p - Printing the receipt and check-out.')
    print('n - Non.')
    select = input('Choose of one the selections: ')
    while select.lower() != 'n':
        if select.lower() == 'a':
            index = int(input('\nPlease enter the index of the item: '))
            index -= 1
            cart.append(menuItems[index])
        elif select.lower() == 'r':
            index = int(input('\nPlease enter the index of the item: '))
            index -= 1
            cart.pop(index)
        elif select.lower() == 't':
            total = len(cart)
            if total > 1:
                print('\nThere are', total, 'items in your cart.')
            elif total == 1:
                print('\nThere is ', total, 'item in your cart.')
            else:
                print('\nYour cart is empty.')
        elif select.lower() == 'p':
            total = len(cart)
            if total > 0:
                print('\nHere is your receipt.')
                item = 0
                for i in cart:
                    item+=1
                    print(item, '.', i)
            else:
                print('\nYour cart is empty.')       
        else: 
            print('\nWrong input')
        displayItems(cart)
        displayItems(menuItems)
        print('\na - Adding an item to cart.')
        print('r - Removing an item from cart.')
        print('t - Total price of items in the cart.')
        print('p - Printing the receipt and check-out.')
        print('n - Non.')
        select = input('Choose of one the selections: ')

# MAIN
choice = input('\nAre you a staff member or a customer of the pastry store? (s/c/n): ')
while choice.lower() !='n': 
    if choice.lower() =='s':
        staff()
    elif choice.lower() == 'c':
        customer()
    elif choice.lower() == 'n':
        break
    else:
        print('\nWrong input')
    choice = input('\n\nAre you a staff member or a customer of the pastry store? (s/c/n): ')