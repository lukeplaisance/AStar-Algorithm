#pylint: disable = E1101
#pylint: disable = C0330
from vector2 import Vector2
from NodeClass import Node

class Graph(object):
    '''class that makes the grid'''
    #Prototype : def __init__(self, width, height)
    #Argument : self, width, height
    #Description : constructor to create the grid
    #Precondition : none
    #Postcondition : constructor to create the grid
    #Protection Level : Public
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = []

    #Prototype : def create_grid(self, node)
    #Argument : self, node
    #Description : creating the grid with nodes
    #Precondition : an instance if the Graph class
    #Postcondition : creating the grid with nodes
    #Protection Level : Public
    def create_grid(self):
        '''creating the grid with nodes'''
        for i in range(0, self.width):
            for j in range(0, self.height):
                new_node = Node(Vector2(i, j))
                self.nodes.append(new_node)

    #Prototype : def get_neighbors(self, node)
    #Argument : self, node
    #Description : function to find the neighbors of the current node
    #Precondition : an instance if the Graph class
    #Postcondition : function to find the neighbors of the current node
    #Protection Level : Public
    def get_neighbors(self, node):
        '''function to find the neighbors of the current node'''
        valid_neighbors = [(node.position + Vector2(0, 1)), #Top
                          (node.position + Vector2(0, -1)), #Bottom
                          (node.position + Vector2(-1, 0)), #Left
                          (node.position + Vector2(1, 0)), #Right
                          (node.position + Vector2(1, 1)), #Top Right
                          (node.position + Vector2(-1, 1)), #Top Left
                          (node.position + Vector2(1, -1)), #Bot Right
                          (node.position + Vector2(-1, -1))] #Bot Left
        neighbors = []
        for n in self.nodes:
            for pos in valid_neighbors:
                if n.position == pos:
                    neighbors.append(n)
        return neighbors

    #Prototype : def __getitem__(self, index)
    #Argument : self, index
    #Description : overloading the index operator
    #Precondition : an instance if the Graph class
    #Postcondition : overloading the index operator
    #Protection Level : Public
    def __getitem__(self, index):
        '''overloading the index operator'''
        return self.nodes[index]

    