import rubik
seen = []

class queue:
	''' This will create a queue and while removing maintain track of seen elements'''
	def __init__(self):
		'''Creates an empty queue'''
		self.item = []
		
	def push(self,a):
		'''Adds an element to the queue'''
		self.item.append(a)
		
	def pop(self):
		'''Removes the element first entered in the queue and adds to seen list'''
		global seen
		if len(self.item) != 0: #If the list is not empty
			seen.append(self.item[0])  # Adds element removed from the queue
						   # To a new array
			del(self.item[0])
		else:
			print('The queue is empty')

import pdb
def shortest_path(start,end):
	''' This is the main required thing, finding shortest path between initial
	and final conditions'''
	q1 = queue()
	q2 = queue()
	maxPath = None
	level1 = {start : 0}
	previous1 = {start : None}
	level2 = {end : 0}
	previous2 = {end : None}
	x = {}
	y= {}
	z = []
	term = 0
	q1.push(start)
	q2.push(end)
	#pdb.set_trace()
	while len(q1.item) != 0 and len(q2.item) != 0:	
	####################################################################################	
	###### First we will check for repeated elements till now
	####################################################################################
		for i in q1.item:
			if i in y:
				#level2[i] = level1[i]
				temp = i
				while previous1[temp]!= None:
					z.append(x[temp])
					temp = previous1[temp]
				z.reverse()
				while previous2[i] != None:
					#l = level2[i]
					z.append(y[i])
					i = previous2[i]
					#level2[i] = l + 1 
				#maxPath = level2[i]
				return z  # This is wrong thing to return, just for sake of understanding
						# that the program should terminate here, returning list of applied operations.
						# can be done without inc level and storing previous values in a list
						# as they are being encountered on the shortest path, given by previous
						# Also remember to append list from start to point of similarity in level1
						# then move to level2 and go previous upto previous != None
		
		if term > ((6**6)-1)/5:   # This is the terminating condition after checking at each level and reaching halfway
					  # It is summation 1 + 6 + 6**2 + ... + 6**6 (which are max number of children in each level)
			return None
				
	#####################################################################################
	###### Here we move ahead in our BFS making a new level from both ends
	###### And checking again in the while				
	#####################################################################################
		for i in rubik.quarter_twists:
			if rubik.perm_apply(i,q1.item[0]) not in x:
				x[rubik.perm_apply(i,q1.item[0])] = i
		BFS(x,q1,level1,previous1)
		
		
		for i in q1.item:
			if i in y:
				#level2[i] = level1[i]
				temp = i
				while previous1[temp]!= None:
					z.append(x[temp])
					temp = previous1[temp]
				z.reverse()
				while previous2[i] != None:
					#l = level2[i]
					z.append(y[i])
					i = previous2[i]
					#level2[i] = l + 1 
				#maxPath = level2[i]
				return z
		
		
		for i in rubik.quarter_twists:
			if rubik.perm_apply(i,q2.item[0]) not in y:
				y[rubik.perm_apply(i,q2.item[0])] = rubik.perm_inverse(i)
		BFS(y,q2,level2,previous2)
				
		term += 1		
				
	

def BFS(x,q,level,previous):      # x is array of possible new levels from start
	     	                  # q specifies which queue to check q1 or q2 depending on value of start
		        	  # level is the dictionary containing the level of each nodes/elements
		        	  # previous is the previous entry to track the best path from a point
	'''Take care of the things we have seen till now
	Check if there is any repetition till now
	Keep a track of the path we have followed till now'''	        
	for i in x:
		if i not in level:
			q.push(i)
			level[i] = level[q.item[0]] + 1
			previous[i] = q.item[0]
	q.pop()
