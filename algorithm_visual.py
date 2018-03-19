import pygame
from visusal_grid import *
from draggable_node import DragableRect
from draw_shapes import *
from NodeClass import Node

class Visual_Algorithm(object):
    def __init__(self, algorithm, screen):
        self.algorithm = algorithm
        self.screen = screen
        self.visusal_grid = VisualGraph(self.algorithm.grid, 35, screen)
        self.visusal_grid.gen_visual()
        self.algorithm.path()
        self.start_node_visual = DragableRect(self.screen, Vector2(500, 500), [30, 30], (93, 255, 115))
        self.end_node_visual = DragableRect(self.screen, Vector2(550, 550), [30,30], (252, 130, 65))

    def update(self, events):
        self.visusal_grid.update(events)
        self.start_node_visual.update(events)
        self.end_node_visual.update(events)
        self.set_start_node()
        self.set_end_node()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.algorithm.path()

        for node in self.algorithm.open_list:
            visual = self.visusal_grid.get_visual(node)
            if visual is not None:
                visual.is_open_list = True
        for node in self.algorithm.close_list:
            visual = self.visusal_grid.get_visual(node)
            if visual is not None:
                visual.is_closed_list = True
        if self.algorithm.path_list is not None:
            for node in self.algorithm.path_list:
                visual = self.visusal_grid.get_visual(node)
                if visual is not None:
                    visual.is_path = True
        start_visual = self.visusal_grid.get_visual(self.algorithm.start_node)
        if start_visual is not None:
            start_visual.is_start = True
        end_visual = self.visusal_grid.get_visual(self.algorithm.end_node)
        if end_visual is not None:
            end_visual.is_goal = True

    def draw(self):
        self.visusal_grid.draw()
        self.start_node_visual.draw()
        self.end_node_visual.draw()

    def set_start_node(self):
        if not self.start_node_visual.is_dragged:
            for node_visual in self.visusal_grid.node_visual:
                if self.start_node_visual.shape.pygame_object.colliderect(node_visual.shape.rect):
                    if self.algorithm.start_node is node_visual.node:
                        return
                    self.start_node_visual.shape.pos = node_visual.shape.pos
                    old_start = self.visusal_grid.get_visual(self.algorithm.start_node)
                    if old_start is not None:
                        old_start.is_start = False
                        self.algorithm.start_node.is_start = False
                    self.algorithm.start_node = node_visual.node

    def set_end_node(self):
        if not self.end_node_visual.is_dragged:
            for node_visual in self.visusal_grid.node_visual:
                if self.end_node_visual.shape.pygame_object.colliderect(node_visual.shape.rect):
                    if self.algorithm.end_node is node_visual.node:
                        return
                    self.end_node_visual.shape.pos = node_visual.shape.pos
                    old_goal = self.visusal_grid.get_visual(self.algorithm.end_node)
                    if old_goal is not None:
                        old_goal.is_goal = False
                        self.algorithm.end_node.is_goal = False
                    self.algorithm.end_node = node_visual.node

    #def set_wall(self, events):
     #   for event in events:
      #      if pygame.MOUSEBUTTONDOWN:

    def highlight_path(self):
        if self.algorithm.path_list is None:
            return
        path_visual_nodes = []
        for node in self.algorithm.path_list:
            visual = self.visusal_grid.get_visual(node)
            if visual is not None:
                path_visual_nodes.append(visual)
        for visual in path_visual_nodes:
            parent_visual = self.visusal_grid.get_visual(visual.node.parent)
            if parent_visual is not None:
                pygame.draw.lines(self.visusal_grid.surface, (30, 195, 198), True,
                                  [[visual.shape.pos.x_position + (visual.shape.scale[0] / 2),
                                  visual.shape.pos.y_position + (visual.shape.scale[1] / 2)],
                                   [parent_visual.shape.pos.x_position + (parent_visual.shape.scale[0] / 2),
                                   parent_visual.shape.pos.y_position + (parent_visual.shape.scale[1] / 2)]], 4)
        return

