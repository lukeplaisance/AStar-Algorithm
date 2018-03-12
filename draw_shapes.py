#pylint: disable = E1101
#pylint: disable = C0330
import pygame
from vector2 import Vector2
from NodeClass import Node
from GraphClass import Graph

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
    def __init__(self, surface, color, pos, scale):
        Shape.__init__(self, surface, color, pos)
        self.pygame_object = None
        self.scale = scale
        self.rect = pygame.rect.Rect(self.pos.x_position, self.pos.y_position, 25, 25)

    def draw_rect(self):
        '''draws a square to the screen'''
        self.pygame_object = pygame.draw.rect(self.surface, (self.color[0],
        self.color[1], self.color[2]), (self.pos.x_position, self.pos.y_position,
        self.scale[0], self.scale[1]))

class Line(Shape):
    '''class for the properties of a line'''
    def __init__(self, surface, color, start_pos, end_pos, width):
        Shape.__init__(self, surface, color, start_pos, end_pos, width)
        self.width = width
        self.pygame_object = None
        self.line = pygame.line.Line(start_pos, end_pos, 3)

    def draw_line(self):
        '''draws a line to the screen'''
        self.pygame_object = pygame.draw.line(self.surface, (self.color[0], self.color[1], self.color[2]),
        (self.pos.x_position, self.pos.y_position), self.width)

class Circle(Shape):
    '''class for the properties of a circle'''
    def __init__(self, surface, color, pos, radius):
        Shape.__init__(self, surface, color, pos)
        self.radius = radius
        self.pygame_object = None

    def draw_circle(self):
        '''draws a circle to the screen'''
        self.pygame_object = pygame.draw.circle(self.surface, (self.color[0], self.color[1], self.color[2]),
        (self.pos.x_position, self.pos.y_position), self.radius)
