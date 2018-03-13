#pylint: disable = W0312
import math
class Vector2:
	'''math library for a 2D vector'''
	def __init__(self, xpos, ypos):
    		'''constructor'''
		self.x_position = xpos
		self.y_position = ypos

	def __add__(self, other):
    		'''returns the sum of 2 vectors'''
		vec = Vector2(self.x_position + other.x_position,
					  self.y_position + other.y_position)
		return vec

	def __sub__(self, other):
    		'''returns the difference of 2 vectors '''
		vec = Vector2(self.x_position - other.x_position,
					  self.y_position - other.y_position)
		return vec

	def __mul__(self, other):
    		'''returns the product of 2 vectors'''
		vec = Vector2(self.x_position * other,
					  self.y_position * other)
		return vec

	def __eq__(self, other):
    		'''compares two vectors to each other'''
		if self.x_position == other.x_position and self.y_position == other.y_position:
    			return True
		return False

	def magnitude(self):
    		'''returns the magnitude'''
		xsq = self.x_position * self.x_position
		ysq = self.x_position * self.x_position
		sum = xsq + ysq
		mag = math.sqrt(sum)
		return mag 

	def Dot(self, other):
    		'''returns the dot product'''
		vec = (self.x_position * other.x_position 
			 + self.y_position * other.y_position)
		return vec 

	def normalize(self):
    		'''normalizes the vector'''
		vec = Vector2(self.x_position /  self.magnitude(),
					  self.y_position /  self.magnitude())
		return vec

	def output(self):
    		'''outputs the vectors into the console'''
		print str(self.x_position) + "," +  str(self.y_position)

	