#pylint: disable = E1101
#pylint: disable = C0330
import pygame
from vector2 import Vector2
from draw_shapes import Rectangle
from draw_shapes import Line
from NodeClass import Node
from GraphClass import Graph
from A_starClass import Astar
from visusal_grid import VisualGraph
from visusal_grid import VisualNode

def main():
    '''function to test pygame'''
    pygame.init()
    screen_width = 1265
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((0, 0, 0))
    grid = Graph(45, 40)
    grid.create_grid()
    graph_visual = VisualGraph(grid, 28, screen)
    start_node = pygame.draw.rect(screen, (0, 255, 0), [25, 25])
    end_node = pygame.draw.rect(screen, (255, 0, 0), [25, 25])
    graph_visual.gen_visual()

    while True:
        screen.fill((0, 0, 0))

        for i in graph_visual.node_visual:
            i.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.event.pump()
        #if evene.type == pygame.MOUSEBUTTONDOWN:

        pygame.display.flip()



main()