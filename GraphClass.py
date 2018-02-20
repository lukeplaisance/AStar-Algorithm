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

    def get_neighbors(self, node):
        '''function to find the neighbors or the current node'''
        valid_neighbors = [(node.pos + Vector2(0, 1)), #Top
                          (node.pos + Vector2(0, -1)), #Bottom
                          (node.pos + Vector2(-1, 0)), #Left
                          (node.pos + Vector2(1, 0)), #Right
                          (node.pos + Vector2(1, 1)), #Top Right
                          (node.pos + Vector2(-1, 1)), #Top Left
                          (node.pos + Vector2(1, -1)), #Bot Right
                          (node.pos + Vector2(-1, -1))] #Bot Left
        neighbors = []
        for n in self.nodes:
            for pos in valid_neighbors:
                if n.pos == pos:
                    neighbors.append(n)
        return neighbors

    