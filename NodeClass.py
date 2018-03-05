#pylint: disable = E1101
#pylint: disable = C0330
from vector2 import Vector2

class Node(object):
    '''class that creates the nodes and its properties'''
    def __init__(self, pos):
        '''constructor'''
        self.position = pos
        self.parent = None
        self.h_score = 0
        self.g_score = 0
        self.f_score = 0
        self.traversable = True
        self.is_goal = False
        self.is_start = False

    def set_parent(self, other):
        '''sets the parent of a node to another'''
        self.parent = other
        return self.parent

    def calculate_g_score(self, other):
        '''returns the G score of the node'''
        if self.parent is None:
            if ((self.position.x_pos is other.position.x_pos and
                self.position.y_pos is not other.position.y_pos)
            or (self.position.x_pos is not other.position.x_pos and
                self.position.y_pos is other.position.y_pos)):
                self.g_score = other.g_score + 10
            else:
                self.g_score = other.g_score + 14
        elif self.parent is not None:
            tent_g = self.g_score
            if ((self.position.x_pos is other.position.x_pos and
                self.position.y_pos is not other.position.y_pos)
            or (self.position.x_pos is not other.position.x_pos and
                self.position.y_pos is other.position.y_pos)):
                tent_g = other.g_score + 10
            else:
                tent_g = other.g_score + 14
            if tent_g < self.g_score:
                self.g_score = tent_g
                self.set_parent(other)

    def calculate_h_score(self, other):
        '''returns the H score of the node'''
        x_distance = abs(other.position.x_pos - self.position.x_pos)
        y_distance = abs(other.position.y_pos - self.position.y_pos)
        total = x_distance + y_distance
        self.h_score = total * 10
        return self.h_score

    def calculate_f_score(self):
        '''returns the F score of the node'''
        self.f_score = self.g_score + self.h_score
        return self.f_score

    def set_non_trav(self):
        '''sets a node to be non traversable'''
        self.is_traversable = False



