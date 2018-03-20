#pylint: disable = E1101
#pylint: disable = C0330
import pygame
from visusal_grid import *
from algorithm_visual import Visual_Algorithm
from A_starClass import Astar
from GraphClass import Graph

class Application(object):
    '''class that runs everythings'''
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 720))
        self.algorithm = Astar(Graph(25, 25))
        self.visual_algorithm = Visual_Algorithm(self.algorithm, self.screen)
        self.running = True
        self.events = []

    def update(self):
        '''updates the appplications each frame'''
        while self.running:
            pygame.event.pump()
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            self.visual_algorithm.update(self.events)
            self.draw()

    def draw(self):
        '''draws the graph a algorithm to the screen'''
        self.screen.fill((55, 0, 65))
        self.visual_algorithm.draw()
        self.visual_algorithm.highlight_path()
        pygame.display.update()
        pygame.display.flip()

def main():
    app = Application()
    app.update()

main()