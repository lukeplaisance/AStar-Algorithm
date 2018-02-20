#pylint: disable = E1101
#pylint: disable = C0330
from GraphClass import Graph
from NodeClass import Node
from vector2 import Vector2

class Astar(object):
    '''class for the A* algorithm'''
    def __init__(self, graph):
        '''constructor'''
        self.grid = graph
        self.open_list = []
        self.close_list = []
        self.current_node = None
        self.end_node = None

    def get_current(self):
        '''returns the node with the lowest f_score and makes it the new current'''
        #add the starting node to the open_list
        self.open_list = sorted(self.open_list, key=lambda x: x.f_score)
        self.current_node = self.open_list[0]

    def path(self):
        '''function to find the easiest path to the end node'''
        while self.current_node not in self.close_list:
            self.get_current()
            neighbors = self.grid.get_neighbors(self.current_node)
            for neighbor in neighbors:
                if neighbor.is_traversable is True and neighbor not in self.close_list:
                    if self.open_list.__contains__(neighbor):
                        self.open_list.append(neighbor)
                        neighbor.calc_g(self.current_node)
                        neighbor.calc_h(self.end_node)
                        neighbor.calc_f()
                        neighbor.set_parent(self.current_node)
                    elif self.open_list.__contains__(neighbor):
                        neighbor.calc_g(self.current_node)


GRID = Graph(10, 10)
GRID.create_grid()
test = GRID.get_neighbors(Node(Vector2(1, 1)))
a = 60
                    