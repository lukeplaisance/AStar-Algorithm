#pylint: disable = E1101
#pylint: disable = C0330
from draw_shapes import Rectangle
from vector2 import Vector2
import pygame
from A_starClass import Astar
from draw_shapes import Shape

class VisualNode(object):
    '''class to see the node on the grid'''
    def __init__(self, node, surface, pos, scale):
        self.node = node
        self.shape = Rectangle(surface, (0, 0, 0), pos, scale)
        self.is_start = False
        self.is_goal = False
        self.open_list = False
        self.closed_list = False

    def update(self):
        '''updtaes the nodes every frame'''
        if self.node.shape.is_start is True:
            self.node.shape.is_start.change_color((0, 255, 0))

    def draw(self):
        '''function to draw the node'''
        self.shape.draw_rect()

class VisualGraph(object):
    '''class to see the grid in the window'''
    def __init__(self, graph, offset, surface):
        self.graph = graph
        self.offset = offset
        self.surface = surface
        self.node_visual = []

    def gen_visual(self):
        '''function to generate the visual graph'''
        count = 0
        for x in range(0, self.graph.width * self.offset, self.offset):
            for y in range(0, self.graph.height * self.offset, self.offset):
                new_node = VisualNode(self.graph.nodes[count], self.surface,
                                        Vector2(x, y), (25, 25))
                self.node_visual.append(new_node)
                count += 1

    def get_visual(self, node):
        '''gets the visual from the node_visual list'''
        for visual in self.node_visual:
            if visual.node == node:
                return visual
        return None

class VisualPath(object):
    '''class for giving the visual for the Astar path'''
    def __init__(self, start, end, graph):
        self.start = start
        self.end = end
        self.graph = graph

    def path_visual(self):
        '''draws the path onto screen'''
        draw_path = []
        if draw_path is not None:
            for node in draw_path:
                visual = self.graph_visual.get_visual(node)
                parent_visual = self.graph_visual.get_visual(node.parent)
                if visual is not None and parent_visual is not None:
                    visual.shape.change_color((255, 150, 255))
                    pygame.draw.lines(self.surface, (0, 0, 255), True,
                    [[visual.shape.pos.x_position + (25 / 2),
                    visual.shape.pos.y_position + (25 / 2)],

                    [parent_visual.shape.pos.x_position + (25 / 2),
                    parent_visual.shape.pos.y_position + (25 / 2)]])

