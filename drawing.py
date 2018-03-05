#pylint: disable = E1101
#pylint: disable = C0330
import pygame
from vector2 import Vector2
from draw_shapes import Shape
from draw_shapes import Rectangle

def main():
    '''function to test pygame'''
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    screen.fill((0, 0, 0))
    m_position = Vector2(450, 650)
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.event.pump()
        if pygame.key.get_pressed()[pygame.K_w] != 0:
            m_position = m_position + Vector2(0, -1)
        if pygame.key.get_pressed()[pygame.K_a] != 0:
            m_position = m_position + Vector2(-1, 0)
        if pygame.key.get_pressed()[pygame.K_s] != 0:
            m_position = m_position + Vector2(0, 1)
        if pygame.key.get_pressed()[pygame.K_d] != 0:
            m_position = m_position + Vector2(1, 0)
        rectangle = Rectangle(m_position, (100, 0, 45), screen)

        rectangle.draw()
        pygame.display.flip()


main()