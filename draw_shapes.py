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

class Rectangle(Shape):
    '''class to draw a square'''
    def __inti__(self, surface, color, pos, scale):
        self.scale = scale
        Shape.__init__(self, surface, color, pos, scale)

    def draw(self):
        '''draws a square to the screen'''
        pygame.draw.rect(self.surface, (self.color[0], self.color[1], self.color[2]),
        (self.pos.x_position, self.pos.y_position, self.scale[0], self.scale[1]))
