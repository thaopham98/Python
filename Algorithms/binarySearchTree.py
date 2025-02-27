from calendar import c
from dataclasses import dataclass
class Node:
    def __init__(self, data):
        self.date = data
        self.left = None
        self.right = None

class binarySearchTree:
    def __init__(self):
        self.root = None

    """Adding a new value into the tree."""
    """ log2(n)"""
    def add(self, current, value ):
        if self.root == None:
            self.root = Node(value) #Creating a root.
        else:
            # Left child
            if value < current.value:
                if current.left == None:
                    current.left = Node(value)
                else:
                    self.add(current.left, value)
            # Right child
            else: 
                if current.right == None:
                    current.right = Node(value)
                else:
                    self.add(current.right, value)
    
    def visit(self, node):
        print(node.value)

    def preOrder(self, current):
        self.visit(current)
        self.preOrder(current.left)
        self.preOrder(current.right)

    def inOrder(self, current):
        self.inOrder(current.left)
        self.visite(current)
        self.inOrder(current.right)
    
    def postOrder(self, current):
        self.postOrder(current.left)
        self.postOrder(current.right)
        self.visit(current)
