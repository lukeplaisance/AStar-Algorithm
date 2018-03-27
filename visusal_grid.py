#pylint: disable = E1101
#pylint: disable = C0330
import pygame
from draw_shapes import Rectangle
from vector2 import Vector2
from A_starClass import Astar
from draw_shapes import *
from NodeClass import Node
import time

class VisualNode(object):
    '''class to see the node on the grid'''
    #Prototype : def __init__(self, surface, pos, scale)
	#Argument : self, surface, color, pos, text, size
	#Description : class to visualize the nodes
	#Precondition : none
	#Postcondition :  class to visualize the nodes
	#Protection Level : Public
    def __init__(self, node, surface, pos, scale):
        self.node = node
        self.shape = Rectangle(surface, (0, 0, 0), pos, scale)
        self.start_node_text = Text(surface, (255, 255, 255), Vector2(940, 400), "start node", 18)
        self.end_node_text = Text(surface, (255, 255, 255), Vector2(940, 450), "end node", 18)
        self.is_start = False
        self.is_goal = False
        self.is_open_list = False
        self.is_closed_list = False
        self.is_path = False
        self.is_wall = False

    #Prototype : def reset_viusal(self)
	#Argument : self
	#Description : resets the visuals to default
	#Precondition : an instance of the VisualNode class
	#Postcondition :  resets the visuals to default
	#Protection Level : Public
    def reset_visual(self):
        '''resets the visuals to default'''
        self.is_open_list = False
        self.is_closed_list = False
        self.is_path = False
        self.node.parent = None

    #Prototype : def update(self, events)
	#Argument : self, events
	#Description : updates the nodes every frame
	#Precondition : an instance of the VisualNode class
	#Postcondition :  updates the nodes every frame
	#Protection Level : Public
    def update(self, events):
        '''updates the nodes every frame'''
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
        elif self.is_wall is True:
            self.shape.change_color((0, 0, 0))
        else:
            self.shape.change_color((180, 180, 180))
        self.toggle_wall(events)

    #Prototype : def draw(self)
	#Argument : self
	#Description : function to draw the nodes
	#Precondition : an instance of the VisualNode class
	#Postcondition :  draws the nodes
	#Protection Level : Public
    def draw(self):
        '''function to draw the node'''
        self.shape.draw_rect()
        self.start_node_text.draw()
        self.end_node_text.draw()

    #Prototype : def toggle_wall(self, events)
	#Argument : self, events
	#Description : places a wall on the grid when you press the "w" key
	#Precondition : an instance of the VisualNode class
	#Postcondition :  places a wall on the grid when you press the "w" key
	#Protection Level : Public
    def toggle_wall(self, events):
        '''places a wall on the grid when you press the "w"" key'''
        if self.shape.rect.collidepoint(pygame.mouse.get_pos()):
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.is_wall = not self.is_wall
                        self.node.is_traversable = not self.node.is_traversable

class VisualGraph(object):
    '''class to see the grid in the window'''
    #Prototype : def __init__(self, graph, offset, surface)
	#Argument : self, graph, offset, surface
	#Description : class to see the grid in the pygame window
	#Precondition : none
	#Postcondition :  class to see the grid in the pygame window
	#Protection Level : Public
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

    #Prototype : def gen_visual(self)
	#Argument : self
	#Description : generates the visual grid
	#Precondition : an instance of the VisualGrpah class
	#Postcondition :  generates the visual grid
	#Protection Level : Public
    def get_visual(self, node):
        '''gets the visual from the node_visual list'''
        for visual in self.node_visual:
            if visual.node == node:
                return visual
        return None

    #Prototype : def get_visual(self, node)
	#Argument : self, node
	#Description : gets the visual from the node_visual list
	#Precondition : an instance of the VisualGrpah class
	#Postcondition :  gets the visual from the node_visual list
	#Protection Level : Public
    def update(self, events):
        '''updates the visual nodes every frame'''
        for node in self.node_visual:
            node.update(events)

    #Prototype : def get_visual(self, events)
	#Argument : self, events
	#Description : updates the visual nodes every frame
	#Precondition : an instance of the VisualGrpah class
	#Postcondition :  updates the visual nodes every frame
	#Protection Level : Public
    def draw(self):
        '''draws the visual nodes to the screen'''
        for node in self.node_visual:
            node.draw()


