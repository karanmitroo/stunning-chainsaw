class Node:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []
        self.weights = []
        self.frequency = 0
        
        
parent = Node()
root = Node(parent)