#pylint: disable = E1101
#pylint: disable = C0330
from GraphClass import Graph
from NodeClass import Node

class Astar(object):
    '''class for the A* algorithm'''
    def __init__(self, graph):
        '''constructor'''
        self.grid = graph
        self.open_list = []
        self.close_list = []

    def get_neighbors(self):
        '''function to find the neighbors or the current node'''
        current = Node(self.pos)
        valid_neighbors = [(current + (0, 1)), (current + (0, -1)), #Top , Bottom
                          (current + (-1, 0)), (current + (1, 0)), #Left, Right
                          (current + (1, 1)), (current + (-1, 1)), #Top Right, Top Left
                          (current + (1, -1)), (current + (-1, -1))] #Bot Right, Bot Left

        for i in range(0, 9):
            for j in range(0, self.grid.width * self.grid.height):
                if valid_neighbors[i] is self.grid.node[j]:
                    self.grid.node[j].parent = current
                    self.open_list.append(self.grid.node[j])