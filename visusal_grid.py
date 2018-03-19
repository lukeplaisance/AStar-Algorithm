#pylint: disable = E1101
#pylint: disable = C0330
import pygame
from draw_shapes import Rectangle
from vector2 import Vector2
from A_starClass import Astar
from draw_shapes import Shape
from NodeClass import Node
import time

class VisualNode(object):
    '''class to see the node on the grid'''
    def __init__(self, node, surface, pos, scale):
        self.node = node
        self.shape = Rectangle(surface, (0, 0, 0), pos, scale)
        self.is_start = False
        self.is_goal = False
        self.is_open_list = False
        self.is_closed_list = False
        self.is_path = False

    def update(self):
        '''updtaes the nodes every frame'''
        if self.is_start is True:
            self.shape.change_color((0, 255, 0))
        elif self.is_goal is True:
            self.shape.change_color((255, 0, 0))
        elif self.is_closed_list is True:
            self.shape.change_color((225, 240, 110))
        elif self.is_open_list is True:
            self.shape.change_color((106, 0, 255))
        elif self.is_path is True:
            self.shape.change_color((255, 225, 0))
        else:
            self.shape.change_color((0, 0, 0))

    def draw(self):
        '''function to draw the node'''
        self.shape.draw_rect()

class VisualGraph(object):
    '''class to see the grid in the window'''
    def __init__(self, graph, offset, surface):
        self.graph = graph
        self.graph.create_grid()
        self.offset = offset
        self.surface = surface
        self.node_visual = []

    def gen_visual(self):
        '''function to generate the visual graph'''
        count = 0
        for x in range(0, self.graph.width * self.offset, self.offset):
            for y in range(0, self.graph.height * self.offset, self.offset):
                new_node = VisualNode(self.graph.nodes[count], self.surface,
                                        Vector2(x, y), (30, 30))
                self.node_visual.append(new_node)
                count += 1

    def get_visual(self, node):
        '''gets the visual from the node_visual list'''
        for visual in self.node_visual:
            if visual.node == node:
                return visual
        return None

    def update(self, events):
        for node in self.node_visual:
            node.update()

    def draw(self):
        for node in self.node_visual:
            node.draw()

