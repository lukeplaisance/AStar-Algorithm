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
        self.close_list.append(min(self.open_list, key=("f_score")))
        index = self.open_list = sorted(self.open_list, key=lambda x: x.f_score)
        return index

    def get_neighbors(self):
        '''function to find the neighbors or the current node'''
        self.get_current()
        valid_neighbors = [(self.current_node.pos + Vector2(0, 1)), #Top
                          (self.current_node.pos + Vector2(0, -1)), #Bottom
                          (self.current_node.pos + Vector2(-1, 0)), #Left
                          (self.current_node.pos + Vector2(1, 0)), #Right
                          (self.current_node.pos + Vector2(1, 1)), #Top Right
                          (self.current_node.pos + Vector2(-1, 1)), #Top Left
                          (self.current_node.pos + Vector2(1, -1)), #Bot Right
                          (self.current_node.pos + Vector2(-1, -1))] #Bot Left

        for position in valid_neighbors:
            for node in self.grid.nodes:
                #is node.position == position
                    #add to a neighbor list
                if (node.position == position and node not in
                    self.open_list and node.is_traversable):
                    self.open_list.append(node)
                node.calc_g(self.current_node)
                node.calc_h(self.end_node)
                node.calc_f()
                node.set_parent(self.current_node)
                    