#pylint: disable = E1101
#pylint: disable = C0330
from vector2 import Vector2

class Node:
    '''class for the nodes'''
    def __init__(self, Vector2, parent):
        '''constructor'''
        self.pos = Vector2
        self.par = parent 

    def Calc_G(self):
        '''returns the G score of the node'''
        g_score = 0
        horizontal = self.pos - (1, 0) or self.pos + (1, 0)
        vertical = self.pos - (0, 1) or self.pos + (0, 1)
        topL = self.pos + (-1, 1)
        topR = self.pos + (1, 1)
        botL = self.pos + (-1, -1)
        botR = self.pos + (1, -1)
        if self.curr is 
            h_score = 10
        else:
            h_score = 14



