import math 

def add(lhs, rhs):
	vec = [0,0]
	vec[0] = lhs[0] + rhs[0]
	vec[1] = lhs[1] + rhs[1]
	return vec

def sub(lhs, rhs):
	vec = [0,0]
	vec[0] = lhs[0] - rhs[0]
	vec[1] = lhs[1] - rhs[1]
	return vec
	
def multi(lhs, rhs):
	vec = [0,0]
	vec[0] = lhs[0] * rhs[0]
	vec[1] = lhs[1] * rhs[1]
	return vec
	
def is_equal(lhs, rhs):
	if lhs[0] == rhs[0] and lhs[1] == rhs[1]:
		return True
	else:
		print "not equal\n"
	
def magnitude(lhs, rhs):
	x_sq = lhs[0] * lhs[0]
	y_sq = rhs[1] * rhs[1]
	sum = x_sq + y_sq
	mag = math.sqrt(sum) 
	return sum 
	
def normalize(lhs, rhs):
	vec = [0, 0]
	vec[0] = lhs[0] / magnitude(lhs, rhs) 		
	vec[1] = rhs[1] / magnitude(lhs, rhs) 
	return vec 
		
def dot(lhs, rhs):
	new_vec = (lhs[0]* rhs[0] + lhs[1]* rhs[1])
	return new_vec
	
vec_one = [2, 4]
vec_two = [1, 1]
print add(vec_one, vec_two)
print sub(vec_one, vec_two)
print multi(vec_one, vec_two)
print magnitude(vec_one, vec_two)
print is_equal(vec_one, vec_two)
print normalize(vec_one, vec_two)
	
	
	
	
	
	
	
	
	
