#pylint: disable = E1101
#pylint: disable = C0330
import pygame
from vector2 import Vector2
from NodeClass import Node

class Shape(object):
    '''default class for all shapes'''
    def __init__(self, surface, color, pos):
        self.pos = pos
        self.color = color
        self.surface = surface

    def change_color(self, color):
        '''function to change the color of a shape'''
        self.color = color

class Rectangle(Shape):
    '''class for the properties of a rectangle'''
    def __inti__(self, surface, color, pos, scale):
        Shape.__init__(self, surface, color, pos)
        self.scale = scale

    def draw_rect(self):
        '''draws a square to the screen'''
        pygame.draw.rect(self.surface, (self.color[0], self.color[1], self.color[2]),
        (self.pos.x_position, self.pos.y_position, self.scale[0], self.scale[1]))

class Line(Shape):
    '''class for the properties of a line'''
    def __init__(self, surface, color, pos, length):
        Shape.__init__(self, surface, color, pos)
        self.length = length

    def draw_line(self):
        '''draws a line to the screen'''
        pygame.draw.rect(self.surface, (self.color[0], self.color[1], self.color[2]),
        (self.pos.x_position, self.pos.y_position, self.length))

class Circle(Shape):
    '''class for the properties of a circle'''
    def __init__(self, surface, color, pos, radius):
        Shape.__init__(self, surface, color, pos)
        self.radius = radius

    def draw_circle(self):
        '''draws a circle to the screen'''
        pygame.draw.rect(self.surface, (self.color[0], self.color[1], self.color[2]),
        (self.pos.x_position, self.pos.y_position, self.radius))

class Visual_Node(object):
    '''class to visually see the node'''
    def __init__(self, node):
        self.node = node
