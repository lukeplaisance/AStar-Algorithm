#pylint: disable = E1101
#pylint: disable = C0330
import pygame

class Shape(object):
    '''default class for all shapes'''
    #Prototype : def __init__(self, surface, color, pos)
    #Argument : self, surface, color, pos
    #Description : default class for all shapes
    #Precondition : none
    #Postcondition :  default class for all shapes
    #Protection Level : Public
    def __init__(self, surface, color, pos):
        self.pos = pos
        self.color = color
        self.surface = surface

    #Prototype : def change_color(self, color)
    #Argument : self, color
    #Description : changes the color of the shapes
    #Precondition : an instance of the Shape class
    #Postcondition :  changes color of the shapes
	#Protection Level : Public
    def change_color(self, color):
        '''function to change the color of a shape'''
        self.color = color

    #Prototype : def __getitem__(self, index)
	#Argument : self, index
    #Description : overloading the index operator
	#Precondition : an instance of the Shape class
	#Postcondition :  overloading the index operator
	#Protection Level : Public
    def __getitem__(self, index):
        '''overloading the index operator'''
        return self.rect[index]

class Rectangle(Shape):
    '''class for the properties of a rectangle'''
    #Prototype : def change_color(self, surface, color, pos, scale)
    #Argument : self, surface, color, pos, scale
    #Description : initializes the properties of a rectangle
    #Precondition : an instance of the Shape class
    #Postcondition :  initializes the properties of a rectangle
    #Protection Level : Public
    def __init__(self, surface, color, pos, scale):
        Shape.__init__(self, surface, color, pos)
        self.scale = scale
        self.rect = pygame.rect.Rect(self.pos.x_position, self.pos.y_position, 25, 25)
        self.pygame_object = pygame.draw.rect(self.surface, (self.color[0],
            self.color[1], self.color[2]), (self.pos.x_position, self.pos.y_position,
            self.scale[0], self.scale[1]))

    #Prototype : def draw_rect(self)
	#Argument : self
	#Description : draws the square to the screen
	#Precondition : an instance of the Shape class
	#Postcondition :  draws the square to the screen
	#Protection Level : Public
    def draw_rect(self):
        '''draws a square to the screen'''
        self.pygame_object = pygame.draw.rect(self.surface, (self.color[0],
        self.color[1], self.color[2]), (self.pos.x_position, self.pos.y_position,
        self.scale[0], self.scale[1]))
        self.rect = pygame.rect.Rect(self.pos.x_position, self.pos.y_position, 25, 25)

class Line(Shape):
    '''class for the properties of a line'''
    #Prototype : def __init__(self, surface, color, pos)
	#Argument : self, surface, color, pos
	#Description : initializes all the properties of a line
	#Precondition : none
	#Postcondition :  initializes all the properties of a line
	#Protection Level : Public
    def __init__(self, surface, color, pos, length):
        Shape.__init__(self, surface, color, pos)
        self.length = length
        self.pygame_object = None

    #Prototype : def draw_line(self)
	#Argument : self
	#Description : draws a line to the screen
	#Precondition : an instance of the Shape class
	#Postcondition :  draws a square to the screen
	#Protection Level : Public
    def draw_line(self):
        '''draws a line to the screen'''
        self.pygame_object = pygame.draw.line(self.surface, (self.color[0], self.color[1], self.color[2]),
        (self.pos.x_position, self.pos.y_position), self.length)

class Circle(Shape):
    '''class for the properties of a circle'''
    #Prototype : def change_color(self, surface, color, pos, radius)
	#Argument : self, surface, color, pos, radius
	#Description : initializes the properties of a circle
	#Precondition : an instance of the Shape class
	#Postcondition :  initializes the properties of a circle
	#Protection Level : Public
    def __init__(self, surface, color, pos, radius):
        Shape.__init__(self, surface, color, pos)
        self.radius = radius
        self.pygame_object = None

    #Prototype : def draw_circle(self)
	#Argument : self
	#Description : draws the circle to the screen
	#Precondition : an instance of the Shape class
	#Postcondition :  draws the circle to the screen
	#Protection Level : Public
    def draw_circle(self):
        '''draws a circle to the screen'''
        self.pygame_object = pygame.draw.circle(self.surface, (self.color[0], self.color[1], self.color[2]),
        (self.pos.x_position, self.pos.y_position), self.radius)

class Text(Shape):
    '''class to display text onto the screen'''
    #Prototype : def change_color(self, surface, color, pos, text, size)
	#Argument : self, surface, color, pos, text, size
	#Description : initializes the properties of text
	#Precondition : an instance of the Shape class
	#Postcondition :  initializes the properties of text
	#Protection Level : Public
    def __init__(self, surface, color, pos, text, size):
        Shape.__init__(self, surface, color, pos)
        self.text = text
        self.size = size
        self.font = pygame.font.SysFont('aharoni', self.size)
        render = self.font.render(self.text, 0, (self.color[0], self.color[1], self.color[2]))
        self.surface.blit(render, (self.pos.x_position, self.pos.y_position))

    #Prototype : def draw(self)
	#Argument : self
	#Description : draws text to the screen
	#Precondition : an instance of the Shape class
	#Postcondition :  draws text to the screen
	#Protection Level : Public
    def draw(self):
        '''draws text to the screen'''
        render = self.font.render(self.text, 0, (self.color[0], self.color[1], self.color[2]))
        self.surface.blit(render, (self.pos.x_position, self.pos.y_position))

    #Prototype : def draw_over_text(self)
	#Argument : self
	#Description : draws text onto another surface
	#Precondition : an instance of the Shape class
	#Postcondition :  draws text onto another surface
    #Protection Level : Public
    def draw_over_text(self, rect):
        '''draws the text onto another drawn object'''
        render = self.font.render(self.text, 0, (self.color[0], self.color[1], self.color[2]))
        self.surface.blit(render, (rect[0] + self.pos.x_position, rect[1] + self.pos.y_position))
