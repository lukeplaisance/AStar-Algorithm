#pylint: disable = E1101
#pylint: disable = C0330
from GraphClass import Graph

class Astar(object):
    '''class for the A* algorithm'''
    def __init__(self, graph):
        '''constructor'''
        self.grid = graph
        self.open_list = []
        self.close_list = []

    def get_neighbors(self):

    