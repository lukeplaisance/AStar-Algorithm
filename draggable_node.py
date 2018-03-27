import pygame
from draw_shapes import Rectangle
from vector2 import Vector2
from NodeClass import Node
from visusal_grid import VisualNode

class DragableRect(object):
    '''class to drag the start and end node'''
    #Prototype : def __init__(self, surface, pos, scale, color)
    #Argument : self, surface, pos, scale, color
    #Description : constructor to initialize the class variables
    #Precondition : none
    #Postcondition :  constructor to initialize the class variables
    #Protection Level : Public
    def __init__(self, surface, pos, scale, color):
        '''function to initialize the values for draggables nodes'''
        self.shape = Rectangle(surface, color, pos, scale)
        self.is_hovered = False
        self.is_dragged = False
        self.color = color

    #Prototype : def hover(self)
    #Argument : self
    #Description : changes the node's' color if the mouse is hovered over
    #Precondition : an instance of the DraggableRect class
    #Postcondition : changes the node's' color if the mouse is hovered over
    #Protection Level : Public
    def hover(self):
        '''function to change the color of the node when the mouse is over it'''
        if self.shape.rect.collidepoint(pygame.mouse.get_pos()):
            self.shape.change_color((255, 0, 220))
            self.is_hovered = True
        else:
            self.shape.change_color(self.color)
            self.is_hovered = False

    #Prototype : def pick_up(self)
    #Argument : self
    #Description : makes the node able to be dragged
    #Precondition : an instance of the DraggableRect class
    #Postcondition :  makes the node able to be dragged
    #Protection Level : Public
    def pick_up(self, events):
        '''function to make the start and end nodes draggable'''
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.is_hovered:
                self.is_dragged = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.is_dragged = False

    #Prototype : def update(self, events)
    #Argument : self, events
    #Description : updates the mouse's position and keeps track if the node is dragged
    #Precondition : an instance of the DraggableRect class
    #Postcondition : updates the mouse's position and keeps track if the node is dragged
    #Protection Level : Public
    def update(self, events):
        '''updates the mouse position for the start and end node'''
        self.hover()
        self.pick_up(events)
        if self.is_dragged:
            mouse_pos = pygame.mouse.get_pos()
            self.shape.pos = Vector2(mouse_pos[0] - (30 /2), mouse_pos[1] - (30 / 2))

    #Prototype : def draw(self)
    #Argument : self
    #Description : draws the draggable node to the screen
    #Precondition : an instance of the DraggableRect class
    #Postcondition :  draws the draggable node to the screen
    #Protection Level : Public
    def draw(self):
        '''draws the draggable node'''
        self.shape.draw_rect()
