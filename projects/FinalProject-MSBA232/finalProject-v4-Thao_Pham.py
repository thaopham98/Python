"""
`*args` is used to pass a variable number of arguments to display()
"""
def display(*args, show="both"):
    """
    Displays the menu, inventory, or both based on the `show` parameter.
    :param menu_inventory: Combined dictionary containing menu and inventory details.
    :param show: Determines what to display. Options: "menu", "inventory", "both", "options".
    """
    if show == "inventory":
        print(f'\nPastry Store Inventory')
        for idx, (item, details) in enumerate(menu_inventory.items(), 1):
            print(f'{idx}. {item}: {details["quantity"]}')
    elif show == "menu":
        print(f'\nPastry Store Menu')
        for idx, (item, details) in enumerate(menu_inventory.items(), 1):
            status = "Sold Out" if details["quantity"] == 0 else f"${details["price"]:.2f}"
            print(f'{idx}. {item}: {status}')
    elif show == "options":
        print('\n+++ Options +++')
        for letter, option in options.items():
            print(f'{letter}: {option}')
    elif show == "both":

        print(f'\nPastry Store Inventory')
        for idx, (item, details) in enumerate(menu_inventory.items(), 1):
            print(f'{idx}. {item}: {details["quantity"]}')
        
        print(f'\nPastry Store Menu')
        for idx, (item, details) in enumerate(menu_inventory.items(), 1):
            status = "Sold Out" if details["quantity"] == 0 else f"${details["price"]:.2f}"
            print(f'{idx}. {item}: {status}')

def validateItemSelection(item_keys):
    """
    Validates that the user's input is within the valid range of item numbers.
    :param item_keys: A list of item keys to validate against.
    :return: The selected item's index (0-based).
    """
    while True:
        try:
            itemN = int(input(f"Enter the item number (1 to {len(item_keys)}): "))
            if 1 <= itemN <= len(item_keys):
                return itemN - 1  # Convert to 0-based index
            else:
                print(f"Error: Item number {itemN} is out of bounds. Please try again.")
        except ValueError:
            print("Error: Please enter a valid integer.")



def addItem(menu_inventory):
    while True:
        itemName = input('\nEnter the item name: ').strip() # Removes leading and trailing whitespaces from the input.

        # Check if the input is empty
        if not itemName:
            print("Error: Item Name cannot be empty. Please try again.")
            continue

        # Check if the item already exists
        if itemName in menu_inventory.keys():
            print(f"Error: '{itemName}' already exists. Please enter a new item name.")
        else:
            break  # Exit loop if input is valid and does not already exist

    
    """ Checking for input errors for price """
    while True:
        try:
            itemPrice = float(input('\nEnter the item price: '))
            if itemPrice < 0:
                print('Error: Price cannot be negative. Please enter a valid price again.')
            else:
                break
        except ValueError:
            print("Error: Please enter a numeric value for the price.")

    """ Checking for input errors for quantity """
    while True:
        try:
            itemQuantity = int(input('\nEnter the item quantity: '))
            if itemQuantity < 0:
                print("Error: Quantity cannot be negative. Please enter a valid quantity again.")
            else:
                break
        except ValueError:
            print("Error: Please enter an integer value for the quantity.")

    """ Add the new item to the combined dictionary """
    menu_inventory[itemName] = {"price": itemPrice, "quantity": itemQuantity}

    """ Display the updated menu and inventory """
    display(menu_inventory, show="both")
    

def removeItem(menu_inventory):
    display(menu_inventory, show='both')
    while True:
        try:
            itemN = int(input('\nEnter the item number you want to remove: '))

            if len(menu_inventory) < itemN < 1:
                itemN = int(input("Error: Invalid input. Please enter a valid number: "))

            """Get the key of the selected item"""
            item_to_remove = list(menu_inventory.keys())[itemN - 1]

            """Remove the item from menu_inventory"""
            menu_inventory.pop(item_to_remove)
            break

        except ValueError:
                print("Error: Please enter a valid integer.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}.")
    display(menu_inventory, show='both')


def editItem(menu_inventory):
    display(menu_inventory, show='both')
    
    # itemN = int(input('Enter the item number you want to edit: ')) # selecting the item to edit

    # while True:  # Loop to validate the item number input
    #     try:
    #         itemN = int(input('\nEnter the item number you want to edit: '))  # Selecting the item to edit
    #         if itemN < 1 or itemN > len(menu_inventory):
    #             print(f"Error: Item number {itemN} is out of bounds. Please select a valid number between 1 and {len(menu_inventory)}.")
    #         else:
    #             break  # Exit loop when input is valid
    #     except ValueError:
    #         print("Error: Please enter a valid integer.")

    # """ Get the key of the selected item """
    # item_to_edit = list(menu_inventory.keys())[itemN - 1]

    item_keys = list(menu_inventory.keys())
    item_index = validateItemSelection(item_keys)
    item_to_edit = item_keys[item_index]


    print(f"You selected: {item_to_edit}")

    # Ask the user what they want to edit
    print("\nWhat would you like to edit?")
    print("n: Edit Name")
    print("p: Edit Price")
    print("q: Edit Quantity")
    choice = input("Enter your option (n/p/q): ").strip().lower()

    if choice == 'n':
        # Edit item name
        new_name = input(f"Enter a new name for '{item_to_edit}': ")
        if new_name in menu_inventory:
            print(f"Error: '{new_name}' already exists in the menu. No changes made.")
        else:
            # Update the dictionary key
            menu_inventory[new_name] = menu_inventory.pop(item_to_edit)
            print(f"Item name updated from '{item_to_edit}' to '{new_name}'.")
    elif choice == 'p':
        # Edit item price
        while True:
            try:
                new_price = float(input(f"Enter a new price for '{item_to_edit}': "))
                if new_price < 0:
                    print("Error: Price cannot be negative. Please try again.")
                else:
                    menu_inventory[item_to_edit]["price"] = new_price
                    print(f"Price of '{item_to_edit}' updated to ${new_price:.2f}.")
                    break
            except ValueError:
                print("Error: Please enter a valid numeric value for the price.")
    elif choice == 'q':
        # Edit item quantity
        while True:
            try:
                new_quantity = int(input(f"Enter a new quantity for '{item_to_edit}': "))
                if new_quantity < 0:
                    print("Error: Quantity cannot be negative. Please try again.")
                else:
                    menu_inventory[item_to_edit]["quantity"] = new_quantity
                    print(f"Quantity of '{item_to_edit}' updated to {new_quantity}.")
                    break
            except ValueError:
                print("Error: Please enter a valid integer value for the quantity.")
    else:
        print("Error: Invalid option selected. No changes made.")

    # Display updated menu and inventory
    display(menu_inventory, show="both")


def totalAmountItem(menu_inventory):
    # totalPItem = {} # Total Per Item
    print(f'Total Amount of Each Item: ')
    for item, details in menu_inventory.items():

        """ Saving the results in totalPItem """
        # totalPItem[item] = details["price"] * details["quantity"]
        # print(f'{item}: ${totalPItem[item]}')
        
        """ NOT Saving the results in totalPItem """
        print(f'{item}: ${details["price"] * details["quantity"]}')

def numItem(inventory):
    count = 0
    for i in inventory.values():
        count = count + i['quantity']
    print(f'Number of Inventory: {count} items')


"""
dict within a dict
"""
menu_inventory = {
    "Cheesecake": {"price": 6.99, "quantity": 50},
    "Croissant": {"price": 1.99, "quantity": 70},
    "Strawberry Short Cake": {"price": 6.99, "quantity": 39},
    "Cupcake": {"price": 1.99, "quantity": 40},
    "Chocolate Muffin": {"price": 1.99, "quantity": 0}
}

options = {'a': 'Add a new item',
           'd': 'Display menu and inventory',
           'e': 'Edit a item',
           'i': 'Inventory',
           'm': 'Menu',
        #    'n': 'Total Number of Inventory',
           'r': 'Remove an item',
           't': 'Total Amount per item',
           'x': 'Exit'
           }

def main():
    while True:
        display(options, show='options')
        try:
            select = str(input(('\nEnter a letter from one of the options above: '))).lower()

            if select == 'a':
                addItem(menu_inventory)
            elif select == 'd':
                display(menu_inventory, show='both')
            elif select == 'e':
                editItem(menu_inventory)
            elif select == 'i':
                display(options, show='inventory')
                numItem(menu_inventory)
            elif select == 'm':
                display(options, show='menu')
            # elif select == 'n':
            #     numItem(menu_inventory)
            elif select == 'r':
                removeItem(menu_inventory)
            elif select == 't':
                totalAmountItem(menu_inventory)
            elif select == 'x':
                print("\nExiting the system. Goodbye!\n")
                break
            else:
                print(f"Error: '{select}' is not a valid option. Please try again")
                continue
        
        except Exception as outOfBound:
            print(f'The option you entered, {select}, is {outOfBound}.')
    
if __name__ == "__main__":
    main()