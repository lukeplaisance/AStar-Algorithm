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
    screen.fill((100, 20, 95))
    grid = Graph(45, 40)
    grid.create_grid()
    graph_visual = VisualGraph(grid, 28, screen)
    start_node = Rectangle(screen, (0, 255, 0), Vector2(0, 419), (25, 25))
    end_node = Rectangle(screen, (255, 0, 0), Vector2(700, 419), (25, 25))
    graph_visual.gen_visual()
    draw_path = []
    start_node_good = None
    end_node_good = None
    a_star = Astar(start_node_good, end_node_good, grid)
    drag_start = False
    drag_end = False
    pressed_space = False
    event_list = []
    while True:
        screen.fill((100, 20, 95))

        for i in graph_visual.node_visual:
            i.draw()
            start_node.draw_rect()
            end_node.draw_rect()
        pygame.event.pump()
        event_list = pygame.event.get()
        for event in event_list:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_node.pygame_object.collidepoint(event.pos):
                        drag_start = True
                    elif end_node.pygame_object.collidepoint(event.pos):
                        drag_end = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if drag_start is True:
                        for node in graph_visual.node_visual:
                            if start_node.pygame_object.colliderect(node.shape.rect):
                                start_node.pos.x_position = node.shape.pos.x_position
                                start_node.pos.y_position = node.shape.pos.y_position
                                start_node_good = node
                                a_star.start_node = start_node_good.node
                                drag_start = False
                    if drag_end is True:
                        for node in graph_visual.node_visual:
                            if end_node.pygame_object.colliderect(node.shape.rect):
                                end_node.pos.x_position = node.shape.pos.x_position
                                end_node.pos.y_position = node.shape.pos.y_position
                                end_node_good = node
                                a_star.end_node = end_node_good.node
                                drag_end = False
            elif event.type == pygame.MOUSEMOTION:
                if drag_start:
                    start_node.pos.x_position = mouse_x
                    start_node.pos.y_position = mouse_y
                elif drag_end:
                    end_node.pos.x_position = mouse_x
                    end_node.pos.y_position = mouse_y

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                pressed_space = True
                a_star.path()
                draw_path = a_star.paths
                a = 0
            if pressed_space:
                count = 0
                count_two = 1
                while count <= len(draw_path):
                    line_start = Vector2(draw_path[count].get_x() * 30,
                                        draw_path[count].get_y() * 30)
                    line_end = Vector2(draw_path[count_two].get_x() * 30,
                                    draw_path[count_two].get_y() * 30)
                    draw_path.append(Line(screen, (250, 135, 0), (Vector2(line_start.x_position,
                    line_start.y_position), Vector2(line_end.x_position, line_end.y_position)), 3))
                    count += 1
                    count_two += 1

        pygame.display.update()
        pygame.display.flip()



main()