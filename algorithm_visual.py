import pygame
from visusal_grid import *
from draggable_node import DragableRect
from draw_shapes import *
from NodeClass import Node

class Visual_Algorithm(object):
    '''class to show the algorithm in the pygame window'''
    #Prototype : def __init__(self, algorithm, screen)
    #Argument : self, algorithm, screen
    #Description : constructor to initialize visuals
    #Precondition : none
    #Postcondition : constructor to initialize visuals
    #Protection Level : Public
    def __init__(self, algorithm, screen):
        '''function to initialize the values for the visual algorithm'''
        self.algorithm = algorithm
        self.screen = screen
        self.visual_grid = VisualGraph(self.algorithm.grid, 35, screen)
        self.visual_grid.gen_visual()
        self.algorithm.path()
        self.start_node_visual = DragableRect(self.screen, Vector2
                                              (900, 400), [30, 30], (93, 255, 115))
        self.end_node_visual = DragableRect(self.screen, Vector2
                                            (900, 450), [30, 30], (252, 130, 65))

    #Prototype : def update(self, events)
    #Argument : self, events
    #Description : function to update the visuals every frame
    #Precondition : an instance of the Visual Algorithm class
    #Postcondition :  functions to update the visuals every frame
    #Protection Level : Public
    def update(self, events):
        '''updates the visuals every frame'''
        self.visual_grid.update(events)
        self.start_node_visual.update(events)
        self.end_node_visual.update(events)
        self.set_start_node()
        self.set_end_node()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.algorithm.path()

        for node in self.algorithm.open_list:
            visual = self.visual_grid.get_visual(node)
            if visual is not None:
                visual.is_open_list = True
        for node in self.algorithm.close_list:
            visual = self.visual_grid.get_visual(node)
            if visual is not None:
                visual.is_closed_list = True
        if self.algorithm.path_list is not None:
            for node in self.algorithm.path_list:
                visual = self.visual_grid.get_visual(node)
                if visual is not None:
                    visual.is_path = True
        start_visual = self.visual_grid.get_visual(self.algorithm.start_node)
        if start_visual is not None:
            start_visual.is_start = True
        end_visual = self.visual_grid.get_visual(self.algorithm.end_node)
        if end_visual is not None:
            end_visual.is_goal = True

    #Prototype : def draw(self)
    #Argument : self
    #Description : draws the grid and to draggable nodes
    #Precondition : an instance of the Visual Algorithm class
    #Postcondition :  draws the grid and the draggable nodes
    #Protection Level : Public
    def draw(self):
        '''draws the algorithm to the screen'''
        self.visual_grid.draw()
        self.start_node_visual.draw()
        self.end_node_visual.draw()

    #Prototype : def set_start_node(self)
    #Argument : self
    #Description : sets the start node to its visual
    #Precondition : an instance of the Visual Algorithm class
    #Postcondition :  sets the start node to its visual
    #Protection Level : Public
    def set_start_node(self):
        '''sets the start node to the visual start node'''
        if not self.start_node_visual.is_dragged:
            for node_visual in self.visual_grid.node_visual:
                if self.start_node_visual.shape.pygame_object.colliderect(node_visual.shape.rect):
                    if self.algorithm.start_node is node_visual.node:
                        return
                    self.start_node_visual.shape.pos = node_visual.shape.pos
                    old_start = self.visual_grid.get_visual(self.algorithm.start_node)
                    if old_start is not None:
                        old_start.is_start = False
                        self.algorithm.start_node.is_start = False
                    self.algorithm.start_node = node_visual.node

     #Prototype : def set_end_node(self)
	 #Argument : self
	 #Description : sets the end node to its visual
	 #Precondition : an instance of the Visual Algorithm class
	 #Postcondition :  sets the end node to its visual
	 #Protection Level : Public
    def set_end_node(self):
        '''sets the end node to the visual end node'''
        if not self.end_node_visual.is_dragged:
            for node_visual in self.visual_grid.node_visual:
                if self.end_node_visual.shape.pygame_object.colliderect(node_visual.shape.rect):
                    if self.algorithm.end_node is node_visual.node:
                        return
                    self.end_node_visual.shape.pos = node_visual.shape.pos
                    old_goal = self.visual_grid.get_visual(self.algorithm.end_node)
                    if old_goal is not None:
                        old_goal.is_goal = False
                        self.algorithm.end_node.is_goal = False
                    self.algorithm.end_node = node_visual.node

     #Prototype : def clear_path(self, events)
	 #Argument : self, events
	 #Description : clears the grid of the node visuals
	 #Precondition : an instance of the Visual Algorithm class
	 #Postcondition :  clears the grid of the node visuals
	 #Protection Level : Public
    def clear_path(self, events):
        '''clears the highlighted path to use the path again'''
        self.algorithm.reset_path()
        for node in self.visual_grid.node_visual:
            node.parent = None
            node.reset_visual()

     #Prototype : def highlight_path(self)
	 #Argument : self
	 #Description : gives the algorithm path a visual 
	 #Precondition : an instance of the Visual Algorithm class
	 #Postcondition :  gives the algorithm path a visual
	 #Protection Level : Public
    def highlight_path(self):
        '''highlights the path to show how it got the end node'''
        if self.algorithm.path_list is None:
            return
        path_visual_nodes = []
        for node in self.algorithm.path_list:
            visual = self.visual_grid.get_visual(node)
            if visual is not None:
                path_visual_nodes.append(visual)
        for visual in path_visual_nodes:
            parent_visual = self.visual_grid.get_visual(visual.node.parent)
            if parent_visual is not None:
                pygame.draw.lines(self.visual_grid.surface, (30, 195, 198), True,
                                  [[visual.shape.pos.x_position + (visual.shape.scale[0] / 2),
                                  visual.shape.pos.y_position + (visual.shape.scale[1] / 2)],
                                   [parent_visual.shape.pos.x_position + (parent_visual.shape.scale[0] / 2),
                                   parent_visual.shape.pos.y_position + (parent_visual.shape.scale[1] / 2)]], 4)
        return
