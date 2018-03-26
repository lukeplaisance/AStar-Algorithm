#pylint: disable = W0312
import math
class Vector2:
	'''math library for a 2D vector'''
	#Prototype : def __init__(self, xpos, ypos)
	#Argument : self, xpos, ypos
	#Description : constructor for the x and y position
	#Precondition : none
	#Postcondition : assigns x and y position
	#Protection Level : Public
	def __init__(self, xpos, ypos):
    		'''constructor'''
		self.x_position = xpos
		self.y_position = ypos

	#Prototype : def __add__(self, other)
	#Argument : self, other
	#Description : returns the sum of 2 vectors
	#Precondition : an instance of the vector2 class
	#Postcondition : returns the sum of 2 vectors
	#Protection Level : Public
	def __add__(self, other):
    		'''returns the sum of 2 vectors'''
		vec = Vector2(self.x_position + other.x_position,
					  self.y_position + other.y_position)
		return vec

	#Prototype : def __sub__(self, other)
	#Argument : self, other
	#Description : returns the difference of 2 vectors
	#Precondition : an instance of the vector2 class
	#Postcondition : returns the difference of 2 vectors
	#Protection Level : Public
	def __sub__(self, other):
    		'''returns the difference of 2 vectors '''
		vec = Vector2(self.x_position - other.x_position,
					  self.y_position - other.y_position)
		return vec

	#Prototype : def __mul__(self, other)
	#Argument : self, other
	#Description : returns the product of 2 vectors
	#Precondition : an instance of the vector2 class
	#Postcondition : returns the product of 2 vectors
	#Protection Level : Public
	def __mul__(self, other):
    		'''returns the product of 2 vectors'''
		vec = Vector2(self.x_position * other,
					  self.y_position * other)
		return vec

	#Prototype : def __eq__(self, other)
	#Argument : self, other
	#Description : compares two vectors to each other
	#Precondition : an instance of the vector2 class
	#Postcondition : compares two vectors to each other
	#Protection Level : Public
	def __eq__(self, other):
    		'''compares two vectors to each other'''
		if self.x_position == other.x_position and self.y_position == other.y_position:
    			return True
		return False

	#Prototype : def __magnitude__(self)
	#Argument : self
	#Description : returns the magnitude of the vector
	#Precondition : an instance of the vector2 class
	#Postcondition : returns the magnitude of the vector
	#Protection Level : Public
	def magnitude(self):
    		'''returns the magnitude'''
		xsq = self.x_position * self.x_position
		ysq = self.x_position * self.x_position
		sum = xsq + ysq
		mag = math.sqrt(sum)
		return mag

	#Prototype : def Dot(self, other)
	#Argument : self, other
	#Description : returns the dot product
	#Precondition : an instance of the vector2 class
	#Postcondition : returns the dot product
	#Protection Level : Public
	def Dot(self, other):
    		'''returns the dot product'''
		vec = (self.x_position * other.x_position 
			 + self.y_position * other.y_position)
		return vec

	#Prototype : def normalize(self)
	#Argument : self
	#Description : normalize the vector
	#Precondition : an instance of the vector2 class
	#Postcondition : normalize the vector
	#Protection Level : Public
	def normalize(self):
    		'''normalizes the vector'''
		vec = Vector2(self.x_position /  self.magnitude(),
					  self.y_position /  self.magnitude())
		return vec

	#Prototype : def output(self)
	#Argument : self
	#Description : outputs the vectors into the console
	#Precondition : an instance of the vector2 class
	#Postcondition : outputs the vectors into the console
	#Protection Level : Public
	def output(self):
    		'''outputs the vectors into the console'''
		print str(self.x_position) + "," +  str(self.y_position)

	