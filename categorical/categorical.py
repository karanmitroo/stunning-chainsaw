
# class Tree:
#     def __init__(node, parent=None):
#         node.parent = parent
#         node.children = []
#         node.weights = []
        

class Node:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []
        self.weights = []
        self.frequency = 0
        
        
root = Node()