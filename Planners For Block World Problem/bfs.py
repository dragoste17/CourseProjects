import pdb

class Block_State:
	
	def __init__(self,number):
		self.number = number
		self.Parent_state = None
		self.ontable=0
		self.clear=0
		self.on=0
	def set_clear(self,clear):
		self.clear=clear
	def set_ontable(self,ontable):
		self.ontable=ontable
	def set_on(self,on):
		self.on=on
	

class Arm_State:

	def __init__(self,empty,hold):
		self.empty = empty
		self.hold = hold
		self.Parent_State = None

def Get_Actions(total_number,Block_List,arm,current):

	Block_List2 = []
	for i in range(total_number):
		block = Block_State(i+1)
		Block_List2.append(block)
	for i in current:
		if(i[0:5] == "clear"):
			cant = i.split(" ")
			Block_List2[int(cant[1])-1].set_clear(1)
		if(i[0:3] == "ont"):
			cant = i.split(" ")
			Block_List2[int(cant[1])-1].set_ontable(1)
		if(i[0:3] == "on "):
			cant = i.split(" ")
			Block_List2[int(cant[1])-1].set_on(int(cant[2]))
		if(i[0]=="e"):
			arm = Arm_State(1,0)
		if(i[0]=="h"):
			cant = i.split(" ")
			arm = Arm_State(0,int(cant[1]))
	
	Applicable=[]
	for i in range(total_number):
		if(Block_List2[i].ontable == 1 and Block_List2[i].clear == 1 and arm.empty == 1):
			Applicable.append("pick " + str(Block_List2[i].number))
		if(Block_List2[i].clear == 1 and Block_List2[i].on != 0 and arm.empty == 1):
			Applicable.append("unstack " + str(Block_List2[i].number) + " " + str(Block_List2[i].on))
		if(Block_List[i].number == arm.hold):
			Applicable.append("release " + str(Block_List2[i].number))
		for j in range(i+1,total_number):
			if(Block_List2[j].clear ==1 and Block_List2[i].number == arm.hold):
				Applicable.append("stack " + str(Block_List2[i].number) + " " + str(Block_List2[j].number))
			if(Block_List2[j].number == arm.hold and Block_List2[i].clear == 1):
				Applicable.append("stack " + str(Block_List2[j].number) + " " + str(Block_List2[i].number))

	return Applicable



def Apply(current,action,Block_List,arm):
	
	
	current2 = current[:]
	
	if(action[0] == "p"):
		cant = action.split(" ")
		current2.append("hold " +(cant[1]))
		ind = current2.index("clear "+(cant[1]))
		del current2[ind]
		Block_List[int(cant[1])-1].clear = 0
		ind = current2.index("empty")
		del current2[ind]
		arm.empty = 0
		arm.hold = int(cant[1])
		ind = current2.index("ontable "+(cant[1]))
		del current2[ind]
		Block_List[int(cant[1])-1].ontable = 0
	
	if(action[0] == "u"):
		cant = action.split(" ")
		current2.append("hold " + cant[1])
		arm.hold = int(cant[1])
		ind = current2.index("clear "+(cant[1]))
		del current2[ind]
		Block_List[int(cant[1])-1].clear = 0
		current2.append("clear " + cant[2])
		Block_List[int(cant[2])-1].clear = 1
		ind = current2.index("on "+(cant[1])+ " "+ cant[2])
		del current2[ind]
		Block_List[int(cant[1])-1].on = 0
		ind = current2.index("empty")
		del current2[ind]
		arm.empty = 0
	
	if(action[0] == "r"):
		cant = action.split(" ")
		ind = current2.index("hold "+ cant[1])
		del current2[ind]
		arm.hold=0
		arm.empty=1
		current2.append("empty")
		current2.append("clear " + cant[1])
		Block_List[int(cant[1])-1].clear = 1
		current2.append("ontable " + cant[1])
		Block_List[int(cant[1])-1].ontable = 1
		
	if(action[0]=="s"):
		cant = action.split(" ")
		ind = current2.index("hold "+ cant[1])
		del current2[ind]
		arm.hold=0
		arm.empty=1
		current2.append("empty")
		ind = current2.index("clear "+(cant[2]))
		del current2[ind]
		Block_List[int(cant[2])-1].clear = 0
		current2.append("on "+cant[1]+" "+cant[2])
		Block_List[int(cant[1])-1].on = int(cant[2])
		current2.append("clear " + cant[1])
		Block_List[int(cant[1])-1].clear = 1
		
	
	return current2
		

class states:
	
	def __init__(self,state,parent,action):
		self.state=state
		self.parent=parent
		self.action=action
	def set_parent(self,parent):
		self.parent=parent
	def set_action(self,action):
		self.action=action

		
def Apply_BFS(total_number, Block_List, goal,arm,initial):
	state_set=[]
	currentState = []
	#Applicable = Get_Actions(total_number,Block_List,arm)
	state = []
	state.append(initial)
	currentState.append(initial)
	root = states(initial,None,"")
	equal=0
	present=-1
	state_set.append(root)
	if(set(initial)==set(goal)):
		return root
	
	while (state != []):
		#pdb.set_trace()
		current = state[0][:]
		del state[0]
		present +=1
		Applicable = Get_Actions(total_number,Block_List,arm,current)
		for i in Applicable:
			equal=0
			stateNext = Apply(current,i,Block_List,arm)
			for p in currentState:
				if(set(stateNext)==set(p)):
					equal=1
					break
			if(equal!=1):
				state.append(stateNext)
				currentState.append(stateNext)
				state2= states(stateNext,state_set[present],i)
				state_set.append(state2)
				if(set(stateNext)==set(goal)):
					return state2
					
	print "Failure"
	return 0
			 
			
			




def Planning(total_number,mode,initial,goal):
	Block_List = []
	for i in range(total_number):
		block = Block_State(i+1)
		Block_List.append(block)
	for i in initial:
		if(i[0:5] == "clear"):
			cant = i.split(" ")
			Block_List[int(cant[1])-1].set_clear(1)
		if(i[0:3] == "ont"):
			cant = i.split(" ")
			Block_List[int(cant[1])-1].set_ontable(1)
		if(i[0:3] == "on "):
			cant = i.split(" ")
			Block_List[int(cant[1])-1].set_on(int(cant[2]))
		if(i[0]=="e"):
			arm = Arm_State(1,0)
		if(i[0]=="h"):
			cant = i.split(" ")
			arm = Arm_State(0,int(i[1]))
			
			
			
	if(mode=="f"):
		answer = Apply_BFS(total_number,Block_List,goal,arm,initial)
		#print answer.state
		answerseries=[]
		while(answer.parent!=None):
			answerseries.append(answer.action)
			answer=answer.parent
		#answerseries.append(answer.action)
		answerseries.reverse()
		print len(answerseries)
		for i in answerseries:
			print i


def gsp(filename):
	'''This function performs a gsp'''

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
	
	Planning(total_number,mode,initial,goal)


#filename= raw_input("Enter filename : ")
#gsp("4.txt")


