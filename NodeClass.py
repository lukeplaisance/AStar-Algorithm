#pylint: disable = E1101
#pylint: disable = C0330
from vector2 import Vector2

class Node(object):
    '''class for the nodes'''
    def __init__(self, pos):
        '''constructor'''
        self.pos = Vector2(pos.x_position, pos.y_position)
        self.parent = None
        self.h_score = 0
        self.g_score = 0
        self.f_score = 0
        self.is_taversable = True

    def set_parent(self, other):
        '''sets the parent of a node to another'''
        self.parent = other
        return self.parent

    def calc_g(self, other):
        '''returns the G score of the node'''
        if (self.pos.x_position is other.pos.x_position
        or self.pos.y_position is other.pos.y_position):
            self.g_score += 10
        else:
            self.g_score += 14
        return self.g_score

    def calc_h(self, other):
        '''returns the H score of the node'''
        x_distance = other.pos.x_position - self.pos.x_position
        y_distance = other.pos.y_position - self.pos.y_position
        total = x_distance + y_distance
        self.h_score = total * 10
        return self.h_score

    def calc_f(self):
        '''returns the F score of the node'''
        self.f_score = self.g_score + self.h_score
        return self.f_score

    def set_non_trav(self):
        '''sets a node to be non traversable'''
        self.is_taversable = False
        return self.is_taversable



