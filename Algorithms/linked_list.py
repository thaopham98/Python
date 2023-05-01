#creating a node
class Node:
    def __init__(self, data = None):
        self.data = data #the value of a node
        self.next = None #the node it's pointing to.

class LinkedList:
    def __init__(self):
        self.head = None # Head node of the list
    
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

#Link head to node1
list1.head.next = node1
#Link node1 to node2
node1.next = node2

list1.printing()
