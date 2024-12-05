menu ={
    "Cheesecake": 6.99,
    "Croissant": 1.99,
    "Strawberry Short Cake":6.99,
    "Cupcake": 1.99, 
    "Chocolate Muffin": 1.99
}

inventory = {
    "Cheesecake": 50,
    "Croissant": 70,
    "Strawberry Short Cake": 39,
    "Cupcake": 40, 
    "Chocolate Muffin": 0
}

options = {'a': 'Add a new item',
           'd': 'Display menu and inventory',
           'e': 'Edit a item',
           'i': 'Inventory',
           'm': 'Menu',
           'r': 'Remove an item',
           't': 'Total Amount per item'
           }

o = {'a': 'Add a new item',
        'd': 'Display menu and inventory',
        'e': 'Edit existing item',
        'i': 'Inventory',
        'm': 'Menu',
        'r': 'Remove an item',
        't': 'Total Amount per item'
        }

def options(options):
    
    # print('\na: Add a new item' +
    #        '\nd: Display menu and inventory' +
    #        '\ne: Edit a item' +
    #        '\ni: Inventory' +
    #        '\nm: Menu' +
    #        '\nr: Remove an item'+
    #        '\nChoose an option from above: '
    #        )
    for l, m in options.items():
        print(f'{l}: {m}')
    

"""
Function to display the menu
"""
def display(*args):

    print(f'\nPastry Store Inventory')
    for item, (name, quantity) in enumerate(inventory.items(), 1):
        print(f'{item}. {name}: {quantity}')


    print(f'\nPastry Store Menu')
    for item, (name, price) in enumerate(menu.items(), 1):
        status = "Sold Out" if inventory[name] == 0 else f"${price:.2f}"
        print(f'{item}. {name}: {status}')



"""
Function to add an item 
"""
def addItem(menu, inventory):
    itemName = input('\nEnter the item name: ')

    """ Checking if the item exists"""
    while itemName in menu.keys():
        itemName = input(f'{itemName} has already exists. Please enter a new item name: ')
    
    """ Checking for input errors of price """
    while True:
        try: 
            itemPrice = float(input('\nEnter the item price: '))
            if itemPrice < 0:
                itemPrice = float(input('Error: Price cannot be negative. Please enter the item price again: '))
            else:
                break
        except ValueError:
            print("Error: Please enter a numeric value for the price.")
    menu[itemName] = itemPrice

    """ Checking for input errors of quantity """
    while True:
        try:
            itemQuantity = int(input('\nEnter the item quantity: '))
            if itemQuantity < 0:
                print("Error: Quantity cannot be negative. Please enter a valid quantity again: ")
            else:
                break
        except ValueError:
            print("Error: Please enter an integer value for the quantity: ")
    inventory[itemName] = itemQuantity

    display(menu, inventory)


"""
Function to remove an item
"""
def removeItem(menu, inventory):

    display(menu, inventory)
    
    while True: 
        try:
            itemN = int(input('\nEnter the item number you want to remove: ')) 
            if itemN < 1 or itemN > len(menu):
                itemN = int(input("Error: Invalid input. Please enter a valid number: "))
            
            """Get the key of the selected item"""
            item_to_remove = list(menu.keys())[itemN - 1]
            
            """Remove the item from both menu and inventory"""
            menu.pop(item_to_remove)
            inventory.pop(item_to_remove)
            break
        
        except ValueError:
                print("Error: Please enter a valid integer.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}.")

    display(menu, inventory)



"""
Function to 
"""

# options()


# display(menu, inventory)
# addItem(menu, inventory)
# removeItem(menu, inventory)


"""
Function to edit the menu
"""
def editItem():

    # choosing what to edit menu or inventory
    userInput1 = str(input('Where do you want to edit? (m or i): '))

    if userInput1 == 'm': # editing an item in the menu
        display(menu)
        item = int(input('Enter the item number that you want to edit: '))
        if item < 1 or item > len(menu):
                item = int(input("The number you entered, {item}, doen not exist."))
        
        """Get the key of the selected item"""
        item_to_edit = list(menu.keys())[item - 1] # storing the item's index 

        choice = input(f'\nn: Editing Name\np: Editing Price\nEnter your option: ')
        if choice == 'n':
            
            oldV = menu[item_to_edit] #storing the old value
            del menu[item_to_edit]
            itemName = input('Enter a new name: ')
            menu[itemName] = oldV
            display(menu)
        # itemPrice = float(input('Enter a new price: '))
    elif userInput1 == 'i':
        # item2 = int(input('Enter the item number that you want to edit: '))
        #     if item2 < 1 or item2 > len(menu):
                # item2 = int(input("The number you entered, {item2}, doen not exist."))

        # price = float(input('Enter your new price: '))
        # menu.update(price)
        pass
    
# editItem()

# display(menu)


def totalInventory(inventory):
    total = 0
    for i in inventory:
        total = total + inventory[i]
        # print(inventory[i])
    print(f'The total inventory: {total} items')
totalInventory(inventory)

# def totalAmountItem(menu, inventory):
#     totalItem= {}
    
#     for item, price in menu.items():
#         quantity = inventory[item]  # Get the corresponding quantity from the inventory
#         totalItem[item] = price * quantity
    
#     for k,v in totalItem.items():
#         print(f'{k}: ${v}')
# totalAmountItem(menu, inventory)

















def main():
    options(o)
    try: 
        option = str(input('Choose a letter from the options above: '))
        for i in o.keys():
            if i != option:
                print('The option is NOT available')
            elif i == 'a':
                addItem(menu, inventory)
            elif i == 'd':
                display(menu, inventory)
            elif i == 'e':
                editItem()
            elif i == 'i':
                display(inventory)
            elif i == 'm':
                display(menu)
            elif i == 'r':
                removeItem(menu, inventory)
            elif i == 't':
                totalAmountItem(menu, inventory)



    except ValueError:
        print(f'Error Input Type: Please enter a letter.')
    except Exception as outOfBound:
        print(f'The option you entered, {option}, is not on the list.')

if __name__ == "__main__":
    main()