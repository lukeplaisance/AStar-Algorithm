import pygame
from draw_shapes import Rectangle
from vector2 import Vector2

class DragableRect(object):
    def __init__(self, surface, pos, scale, color):
        self.shape = Rectangle(surface, color, pos, scale)
        self.is_hoovered = False
        self.is_dragged = False
        self.color = color

    def hoover(self):
        if self.shape.rect.collidepoint(pygame.mouse.get_pos()):
            self.shape.change_color((255, 0, 220))
            self.is_hoovered = True
        else:
            self.shape.change_color(self.color)
            self.is_hoovered = False

    def pick_up(self, events):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and self.is_hoovered:
                    self.is_dragged = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.is_dragged = False

    def update(self, events):
        self.hoover()
        self.pick_up(events)
        if self.is_dragged:
            mouse_pos = pygame.mouse.get_pos()
            self.shape.pos = Vector2(mouse_pos[0] - (25 /2), mouse_pos[1] - (25 / 2))

    def draw(self):
        self.shape.draw_rect()
