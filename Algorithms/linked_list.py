'''The class represents a single node in the linked list'''
class Node:
    def __init__(self, data = None):
        self.data = data #the value of a node
        self.next = None #the node it's pointing to.

class Linked:
    def __init__(self, test):
        self.test1 = test

'''The Class represents the entire list '''
class LinkedList:
    def __init__(self):
        self.head = None # Head node of the list

    '''Adding a new node to the end of the list'''
    def append(self,data):
        new_node = Node(data) # Creating a new node

        '''If the list is empty, creating a new node and set as the head node'''
        if not self.head:
            self.head = new_node
            return
        
        '''If the list is NOT empty, travesing to the end of the list and creating a new node'''
        current_node = self.head
        print(f'The list is not empty, creating a new node, {new_node.data}')

        print(f'Starting the traversing throught the list ...')
        while current_node.next: # As long as current_node is pointing to the next node,
            current_node = current_node.next # Setting current_node as the next node.
            
            '''Displaying the traversing through the list'''
            # if current_node.next:
            #     print(f'{current_node.data} -> {current_node.next.data}')
            # else:
            #     print(f'{current_node.data} -> None')

        '''
        When the last node is reached, the `next` property of the current_node
        is set to the `next_node` that is being added to the end of the list.
        This effectively appends the new_node to the end of the linked list. 
        '''
        current_node.next = new_node 
        print(f'The new node, {new_node.data} is added to the list')
        # After the while loop completes, current_node will be pointing to the last node in the list
        # So, we can append the new node to the end of the list

    '''Adding a new node to the beginning of the list'''
    def prepend(self, data):
        new_node = Node(data) # Creatint a new node

        """ 
        The new node must pointing to the current head first.
        Then, can safely set the new node as the new head.
        """
        new_node.next = self.head # Setting the new node points to the current head
        self.head = new_node # Setting the new node as the new head


    '''Displaying the contents of the list'''
    def printing(self):
        displaying = self.head #displaying the head node/ the starting node
        while displaying is not None: 
            print(displaying.data)
            displaying = displaying.next

"""A list with 3 nodes"""
list1 = LinkedList()
list1.head = Node("head")
node1 = Node('1')
node2 = Node('2')

'''Linking head to node1'''
list1.head.next = node1
'''Linking node1 to node2'''
node1.next = node2

list1.printing()

'''Appeding a new node to the list'''
list1.append('3')
list1.printing()