#pylint: disable = E1101
#pylint: disable = C0330
import pygame
from vector2 import Vector2

class Shape(object):
    '''default class for all shapes'''
    def __init__(self, pos, color, surface):
        self.pos = pos
        self.color = color
        self.surface = surface

    def change_color(self, color):
        '''function to change the color of a shape'''
        self.color = color

class Square(Shape):
    '''class to draw a square'''
    def __inti__(self, pos, color, scale, surface):
        self.scale = scale
        Shape.__init__(self, pos, color, surface)