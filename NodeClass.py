#pylint: disable = E1101
#pylint: disable = C0330
#pylint: disable = W0312

class Node(object):
    '''class that creates the nodes and its properties'''
    #Prototype : def __init__(self, pos)
    #Argument : self, pos
    #Description : constructor for the Node class
    #Precondition : none
    #Postcondition : constructor for the Node class
    #Protection Level : Public
    def __init__(self, pos):
        '''constructor'''
        self.position = pos
        self.parent = None
        self.h_score = 0
        self.g_score = 0
        self.f_score = 0
        self.is_traversable = True
        self.is_goal = False
        self.is_start = False

    #Prototype : def set_parent(self, pos)
    #Argument : self, other
    #Description : sets the parent of a node to another
    #Precondition : an instance of the Node class
    #Postcondition : sets the parent of a node to another
    #Protection Level : Public
    def set_parent(self, other):
        '''sets the parent of a node to another'''
        self.parent = other
        return self.parent

    #Prototype : def calc_g(self, pos)
    #Argument : self, other
    #Description : returns the G score of the node
    #Precondition : an instance of the Node class
    #Postcondition : returns the G score of the node
    #Protection Level : Public
    def calc_g(self, other):
        '''returns the G score of the node'''
        if self.parent is None:
            if ((self.position.x_position is other.position.x_position and
                self.position.y_position is not other.position.y_position)
            or (self.position.x_position is not other.position.x_position and
                self.position.y_position is other.position.y_position)):
                self.g_score = other.g_score + 10
            else:
                self.g_score = other.g_score + 14
        elif self.parent is not None:
            tent_g = self.g_score
            if ((self.position.x_position is other.position.x_position and
                self.position.y_position is not other.position.y_position)
            or (self.position.x_position is not other.position.x_position and
                self.position.y_position is other.position.y_position)):
                tent_g = other.g_score + 10
            else:
                tent_g = other.g_score + 14
            if tent_g < self.g_score:
                self.g_score = tent_g
                self.set_parent(other)

    #Prototype : def calc_h(self, pos)
    #Argument : self, other
    #Description : returns the H score of the node
    #Precondition : an instance of the Node class
    #Postcondition : returns the H score of the node
    #Protection Level : Public
    def calc_h(self, other):
        '''returns the H score of the node'''
        x_distance = abs(other.position.x_position - self.position.x_position)
        y_distance = abs(other.position.y_position - self.position.y_position)
        total = x_distance + y_distance
        self.h_score = total * 10
        return self.h_score

    #Prototype : def calc_f(self, pos)
    #Argument : self, other
    #Description : returns the F score of the node
    #Precondition : an instance of the Node class
    #Postcondition : returns the F score of the node
    #Protection Level : Public
    def calc_f(self):
        '''returns the F score of the node'''
        self.f_score = self.g_score + self.h_score
        return self.f_score


