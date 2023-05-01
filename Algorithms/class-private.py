class Menu:
    def __init__(self) -> None:
        """ using private list """
        # self.__items = ['Cheesecake', 'Cupcake', 'Croissant']
        """ using private dict """
        self.__items = {'Cheesecake': 6.99, 
                        'Cupcake': 1.99, 
                        'Croissant': 2.99
                        }

    def menuItems(self):
        print('\n--- Menu ---')

        """ using private list """
        # for item in self.__items:
        #     print(item)

        """ using private dict """
        for item in self.__items:
            print(item , '- $',self.__items[item] )
            # print(self.__items[item]) #values
        print('\n')
    
    """private method"""
    def __addItem(self):
        name = input('Enter the name of the item: ')
        price = float(input('Enter the price of the item: '))
        print('\nAdding an item to the menu...\nAfter adding a new item...')
        self.__items[name] = price #Adding a new item.
        self.menuItems()

    """private method"""
    def __updateItem(self):
        name = input("Enter the exist item's name: ")
        if name in self.__items:
            price = float(input('Enter its price: '))
            print('\nUpdating an existing item on the menu...\nAfter update the item...')
            self.__items.update({name:price}) #Updating an existing item.
            self.menuItems()
        else:
            choice = input('The name you enter does not exist.\nDo you want to add it as a new item instead? (y/n):')
            if choice == 'y':
                self.__addItem()

    def options(self):
        print('\na - Adding a new item to the menu.')
        print('u - Updating an existing item on the menu.')
        option = input('Select an option: ')

        while option != 'e':
            if option == 'a':
                self.__addItem()
            elif option == 'u':
                self.__updateItem()
            
            print('\na - Adding a new item to the menu.')
            print('u - Updating an existing item on the menu.')
            option = input('Select an option: ')


order1 = Menu()
order1.menuItems()
order1.options()
