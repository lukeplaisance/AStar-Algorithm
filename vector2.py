#pylint: disable = W0312
import math
class Vector2:
	'''math library for a 2D vector'''
	def __init__(self, xpos, ypos):
    		'''constructor'''
		self.x_pos = xpos
		self.y_pos = ypos

	def __add__(self, other):
    		'''returns the sum of 2 vectors'''
		vec = Vector2(self.x_pos + other.x_pos,
					  self.y_pos + other.y_pos)
		return vec

	def __sub__(self, other):
    		'''returns the difference of 2 vectors '''
		vec = Vector2(self.x_pos - other.x_pos,
					  self.y_pos - other.y_pos)
		return vec

	def __mul__(self, other):
    		'''returns the product of 2 vectors'''
		vec = Vector2(self.x_pos * other,
					  self.y_pos * other)
		return vec

	def __eq__(self, other):
    		'''compares two vectors to each other'''
		if self.x_pos == other.x_pos and self.y_pos == other.y_pos:
    			return True
		return False

	def magnitude(self):
    		'''returns the magnitude'''
		xsq = self.x_pos * self.x_pos
		ysq = self.y_pos * self.y_pos
		sum = xsq + ysq
		mag = math.sqrt(sum)
		return mag 

	def Dot(self, other):
    		'''returns the dot product'''
		vec = (self.x_pos * other.x_pos 
			 + self.y_pos * other.y_pos)
		return vec 

	def normalize(self):
    		'''normalizes the vector'''
		vec = Vector2(self.x_pos /  self.magnitude(),
					  self.y_pos /  self.magnitude())
		return vec;

	def output(self):
    		'''outputs the vectors into the console'''
		print str(self.x_pos) + "," +  str(self.y_pos)

	