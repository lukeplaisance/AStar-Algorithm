print "Hello World"
import os

def add(lhs, rhs):
	return lhs + rhs

def sub(lhs, rhs):
	return lhs - rhs
	
def multi(lhs, rhs):
	return lhs * rhs
	
def div(lhs, rhs):
	return lhs / rhs 
	
question = 0
while question != 5:
	print " 1.add  2.subtract  3.multiply	4.divide  5.exit  6.restart "
	lhs = input("enter any number \n")
	rhs = input("enter another number \n")
	question = input("What operation do you want to use?: \n")
	if question is 1:
		print add(lhs, rhs)
	elif question is 2:
		print sub(lhs, rhs)
	elif question is 3:
		print multi(lhs, rhs)
	elif question is 4:
		print div(lhs, rhs)
	elif question is 5:
		break
	else:
		continue
	question = input("Would you like to quit?: ")
os.system('cls')
		