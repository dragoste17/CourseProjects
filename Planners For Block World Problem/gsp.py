import pdb
import sys
import time
from copy import deepcopy

currentState = []

class Stack:

	def __init__(self):
		self.stack = []

	def push(self,elem):
		self.stack.append(elem)

	def pop(self):
		return self.stack.pop()

	def fullpush(self,elem):
		self.stack.append(elem)
		for i in range(len(elem)):
			self.stack.append(elem[len(elem)-i-1])

	def isnotempty(self):
		return not(self.stack == [])
			 
			
			
def findAction(elem):
	#pdb.set_trace()
	global currentState
	if(elem[0:5] == "clear"):
		#pdb.set_trace()
		cant = elem.split(" ")
		for i in currentState:
			x = i.split(" ")
			if x[0] == "on" and x[2] == cant[1]:
				act = "action unstack "+x[1]+" "+x[2]
				prec = ["clear "+x[1],"empty"]
				return act,prec
			elif x[0] == "hold" and x[1] == cant[1]:
				act = "action release "+x[1]
				prec = ["hold "+x[1]]
				return act,prec
	if(elem[0:3] == "ont"):
		cant = elem.split(" ")
		#pdb.set_trace()
		for i in currentState:
			x = i.split(" ")
			if x[0] == "on" and x[1] == cant[1]:
				act = "action unstack "+x[1]+" "+x[2]
				prec = ["clear "+x[1],"empty"]
				return act,prec
			elif x[0] == "hold" and x[1] == cant[1]:
				act = "action release "+x[1]
				prec = ["hold "+x[1]]
				return act,prec
			
	if(elem[0:3] == "on "):
		cant = elem.split(" ")
		act = "action stack "+cant[1]+" "+cant[2]
		prec = ["clear "+cant[2],"hold "+cant[1]]
		return act,prec
	if(elem[0]=="e"):
		for i in currentState:
			x = i.split(" ")
			if x[0] == "hold":
				act = "action release "+x[1]
				prec = ["hold "+x[1]]
				return act,prec
	if(elem[0]=="h"):
		cant = elem.split(" ")
		for i in currentState:
			x = i.split(" ")
			if x[0] == "on" and x[1] == cant[1]:
				act = "action unstack "+x[1]+" "+x[2]
				prec = ["clear "+x[1],"empty"]
				return act,prec
			elif x[0] == "ontable" and x[1] == cant[1]:
				act = "action pick "+cant[1]
				prec = ["empty","clear "+cant[1],"ontable "+cant[1]]
				return act,prec


def applyAction(elem):
	'''This will apply the action once it is popped'''
	global currentState
	cant = elem.split(" ")
	#pdb.set_trace()
	if cant[1] == "pick":
		for i in range(len(currentState)):
			if currentState[i] == "empty":
				currentState[i] = "hold "+cant[2]
			elif currentState[i] == "clear "+cant[2]:
				currentState[i] = 0
			elif currentState[i] == "ontable "+cant[2]:
				currentState[i] = 0

	elif cant[1] == "release":
		currentState.append("ontable "+cant[2])
		currentState.append("clear "+cant[2])
		for i in range(len(currentState)):
			if currentState[i][0:4] == "hold":
				currentState[i] = "empty"

	elif cant[1] == "unstack":
		#pdb.set_trace()
		currentState.append("clear "+cant[3])
		for i in range(len(currentState)):
			if currentState[i] == "on "+cant[2]+" "+cant[3]:
				currentState[i] = 0
			elif currentState[i] == "empty":
				currentState[i] = "hold "+cant[2]
			elif currentState[i] == "clear "+cant[2]:
				currentState[i] = 0


	elif cant[1] == "stack":
		currentState.append("on "+cant[2]+" "+cant[3])
		currentState.append("clear "+cant[2])
		for i in range(len(currentState)):
			if currentState[i] == "hold "+cant[2]:
				currentState[i] = "empty"
			elif currentState[i] == "clear "+cant[3]:
				currentState[i] = 0

	currentState[:] = [x for x in currentState if x != 0]





def Planning(total_number,mode,initial,goal):
	
	global currentState
	stack = Stack()
	#print goal
	currentState = deepcopy(initial)
	plan = []
	stack.fullpush(goal)
	#print stack.stack
	while stack.isnotempty():
		elem = stack.pop()
		#pdb.set_trace()
		#print elem
		#print currentState
		#print stack.stack
		if elem == goal:
			flag1 = 0
			for i in currentState:
				if i in goal:
					continue
				else:
					flag1 = 1
					break
			if flag1 == 0:
				#print "Done"
				return plan
			else:
				stack.fullpush(goal)
		elif isinstance(elem, list):
			flag = 0
			for i in elem:
				if i in currentState:
					pass
				else:
					flag = 1
					break
			if flag == 1:
				stack.fullpush(elem)
		elif isinstance(elem, basestring):
			if elem in currentState:
				pass
			elif elem[0:6] == "action":
				applyAction(elem)
				plan.append(elem)
			else:
				#stack.push(elem)
				#pdb.set_trace()
				action,precond = findAction(elem)
				stack.push(action)
				stack.fullpush(precond)




def gsp(filename):
	'''This function performs a gsp'''
	#time1 = time.time()
	global currentState
	fileopen = open(filename,"r")
	linesArray = fileopen.read().split("\n")
	total_number = int(linesArray[0])
	mode = linesArray[1]
	#Initial conditions
	initial = linesArray[3].split(") (")
	initial[0] = initial[0].strip("(")
	initial[-1] = initial[-1].strip(")")
	currentState = initial

	#Goal state
	goal = linesArray[5].split(") (")
	goal[0] = goal[0].strip("(")
	goal[-1] = goal[-1].strip(")")
	
	#print initial,goal
	
	plan = Planning(total_number,mode,initial,goal)
	print len(plan)
	for i in plan:
		print i
	#time2 = time.time()
	#print time2-time1


#filename= raw_input("Enter filename : ")

#gsp("3.txt")