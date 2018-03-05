#pylint: disable = E1101
#pylint: disable = C0330
from GraphClass import Graph
from NodeClass import Node
from vector2 import Vector2

class Astar(object):
    '''class for the A* algorithm'''
    def __init__(self):
        '''constructor'''
        self.grid = None
        self.open_list = []
        self.close_list = []
        self.paths = None
        self.start_node = None
        self.current_node = None
        self.end_node = None

    def get_current(self):
        '''returns the node with the lowest f_score and makes it the new current'''
        #add the starting node to the open_list
        self.open_list.sort(key=lambda x: x.f_score)
        self.current_node = self.open_list[0]
        self.open_list.remove(self.current_node)
        self.close_list.append(self.current_node)

    def path(self, start, end, graph):
        '''function to find the easiest path to the end node'''
        self.current_node = start
        self.end_node = end
        #Add the starting square (or node) to the open list.
        self.open_list.append(start)
        #Repear until goal is in closed list or open list is empty
        while not self.close_list.__contains__(end):
            #Look for lowest f in open list
            self.get_current()
            #Switch lowest f to closed list
            valid_neighbors = [(self.current_node.position + Vector2(0, 1)), #Top
                          (self.current_node.position + Vector2(0, -1)), #Bottom
                          (self.current_node.position + Vector2(-1, 0)), #Left
                          (self.current_node.position + Vector2(1, 0)), #Right
                          (self.current_node.position + Vector2(1, 1)), #Top Right
                          (self.current_node.position + Vector2(-1, 1)), #Top Left
                          (self.current_node.position + Vector2(1, -1)), #Bot Right
                          (self.current_node.position + Vector2(-1, -1))] #Bot Left
            neighbors = []
            for n in graph:
                for pos in valid_neighbors:
                    if n.position == pos:
                        neighbors.append(n)
                #get neighbors of lowest f
                #for each neighbor that is traversable or not in closed list
                for neighbor in neighbors:
                    #if node is in open list
                        #check to see if it is a better path to go to it from current node rather than
                        # its current parent
                        # If it is a better path reparent it and re calc f score and re assign g score
                    #if not in open list
                    #calcualte g score normally
                    #calc h score
                    #calc f score
                    if neighbor.traversable is True and self.close_list.__contains__(neighbor) is False:
                        if self.open_list.__contains__(neighbor):
                            neighbor.calculate_g_score(self.current_node)
                            neighbor.calculate_h_score(end)
                            neighbor.calculate_f_score()
                        else:
                            self.open_list.append(neighbor)
                            neighbor.calculate_g_score(self.current_node)
                            neighbor.calculate_h_score(end)
                            neighbor.calculate_f_score()
                            neighbor.set_parent(self.current_node)
        paths = []
        while self.current_node is not None:
            paths.append(self.current_node)
            self.current_node = self.current_node.parent
        self.paths = paths
        return paths

    def display_graph(self):
        '''function to display the grid and the path to the goal node'''
        line = ""
        for node in self.grid.nodes:
            if node == self.end_node:
                line += "[G]"
            elif node == self.start_node:
                line += "[S]"
            elif self.paths.__contains__(node):
                line += "[*]"
            elif not node.is_traversable:
                line += "[X]"
            else:
                line += "[ ]"
            if node.position.y_pos == self.grid.width - 1:
                print line
                line = ""

