#pylint: disable = E1101
#pylint: disable = C0330
import pygame
from algorithm_visual import Visual_Algorithm
from A_starClass import Astar
from GraphClass import Graph

class Application(object):
    '''class that runs everythings'''
    #Prototype : def __init__(self)
	#Argument : self
	#Description : class that runs everything
	#Precondition : none
	#Postcondition :  class that runs everything
	#Protection Level : Public
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 720))
        self.algorithm = Astar(Graph(25, 25))
        self.visual_algorithm = Visual_Algorithm(self.algorithm, self.screen)
        self.running = True
        self.events = []

    #Prototype : def update(self)
	#Argument : self
	#Description : updates the drawings and path each frame
	#Precondition : an instance of the Application class
	#Postcondition :  updates the drawings and path each frame
	#Protection Level : Public
    def update(self):
        '''updates the appplications each frame'''
        while self.running:
            pygame.event.pump()
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.visual_algorithm.clear_path(self.events)
                    if event.key == pygame.K_ESCAPE:
                        return
            self.visual_algorithm.update(self.events)
            self.draw()

    #Prototype : def draw(self)
	#Argument : self
	#Description : draws the graph and algorithm to the screen
	#Precondition : an instance of the Application class
	#Postcondition :  draws the graph and algorithm to the screen
	#Protection Level : Public
    def draw(self):
        '''draws the graph and algorithm to the screen'''
        if self.events is not None:
            self.screen.fill((0, 0, 0))
            self.visual_algorithm.draw()
            self.visual_algorithm.highlight_path()
            pygame.display.update()
            pygame.display.flip()

#Prototype : def main()
#Argument : none
#Description : main function to run the application
#Precondition : an instance of the Application class
#Postcondition :  main function to run the application
#Protection Level : Public
def main():
    '''main function to run the application'''
    app = Application()
    app.update()

main()