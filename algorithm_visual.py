from visusal_grid import *
from draggable_node import DragableRect

class Visual_Algorithm(object):
    def __init__(self, algorithm, screen):
        self.algorithm = algorithm
        self.screen = screen
        self.visusal_grid = VisualGraph(self.algorithm.grid, 35, screen)
        self.visusal_grid.gen_visual()
        self.algorithm.path()
        self.start_node_visual = DragableRect(self.screen, Vector2(500,500), [25,25], (194, 252, 195))
        self.end_node_visual = DragableRect(self.screen, Vector2(550,550), [25,25], (252, 194, 194))

    def update(self,events):
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
        if self.algorithm.paths is not None:
            for node in self.algorithm.paths:
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