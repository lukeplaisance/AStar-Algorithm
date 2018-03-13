#pylint: disable = E1101
#pylint: disable = C0330
from GraphClass import Graph
from NodeClass import Node
from vector2 import Vector2

class Astar(object):
    '''class for the A* algorithm'''
    def __init__(self, start, end, graph):
        '''constructor'''
        self.grid = graph
        self.open_list = []
        self.close_list = []
        self.paths = None
        self.start_node = start
        self.current_node = start
        self.end_node = end

    def get_current(self):
        '''returns the node with the lowest f_score and makes it the new current'''
        #add the starting node to the open_list
        self.open_list.sort(key=lambda x: x.f_score)
        self.current_node = self.open_list[0]

    def path(self):
        self.current_node = self.start_node
        '''function to find the easiest path to the end node'''
        #Add the starting square (or node) to the open list.
        self.open_list.append(self.current_node)
        #Repear until goal is in closed list or open list is empty
        while not self.close_list.__contains__(self.end_node):
            #Look for lowest f in open list
            self.get_current()
            #Switch lowest f to closed list
            self.open_list.remove(self.current_node)
            self.close_list.append(self.current_node)
            #get neighbors of lowest f
            neighbors = self.grid.get_neighbors(self.current_node)
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
                if neighbor.is_traversable is True and not self.close_list.__contains__(neighbor):
                    if not self.open_list.__contains__(neighbor):
                        self.open_list.append(neighbor)
                        neighbor.calc_g(self.current_node)
                        neighbor.calc_h(self.end_node)
                        neighbor.calc_f()
                        neighbor.set_parent(self.current_node)
                    elif self.open_list.__contains__(neighbor):
                        neighbor.calc_g(self.current_node)
                        neighbor.calc_h(self.end_node)
                        neighbor.calc_f()
        paths = []
        while self.current_node.parent is not None:
            paths.append(self.current_node)
            self.current_node = self.current_node.parent
        self.paths = paths

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
            if node.position.y_position == self.grid.width - 1:
                print line
                line = ""


#GRID = Graph(10, 10)
#GRID.create_grid()
#START = GRID.nodes[99]
#START.is_start = True
#END = GRID.nodes[33]
#END.is_goal = True
#GRID.nodes[43].set_non_trav()
#GRID.nodes[44].set_non_trav()
#GRID.nodes[45].set_non_trav()
#GRID.nodes[46].set_non_trav()
#GRID.nodes[47].set_non_trav()
#GRID.nodes[48].set_non_trav()
#GRID.nodes[49].set_non_trav()
#GRID.nodes[56].set_non_trav()
#GRID.nodes[66].set_non_trav()
#TEST_1 = Astar(START, END, GRID)
#TEST_1.path()
#TEST_1.display_graph()
#a = 60
                    