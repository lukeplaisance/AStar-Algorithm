#pylint: disable = E1101
#pylint: disable = C0330
from vector2 import Vector2
from NodeClass import Node

class Graph(object):
    '''class that makes the grid'''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = []

    def create_grid(self):
        '''creating the grid with nodes'''
        for i in range(0, self.width):
            for j in range(0, self.height):
                new_node = Node(Vector2(i, j))
                self.nodes.append(new_node)


GRID = Graph(10, 10)
GRID.create_grid()
print GRID


    