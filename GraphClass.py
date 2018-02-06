#pylint: disable = E1101
#pylint: disable = C0330
from vector2 import Vector2
from NodeClass import Node

class Graph(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = []

    def create_grid(self):
        '''creating the grid with nodes'''
        num_nodes = self.width * self.height
        x = 0
        y = 0
        for i in range(0, (num_nodes)):
            new_node = Node(x, y)
            self.nodes.append(new_node)


    