import sys
import pdb
import time

S = [[],[],[],[],[],[],[],[],[]] #Sudoku puzzle
possDomains = [[],[],[],[],[],[],[],[],[]] #This will store all the possible domains allowed for the field initially
copyS = S[:]
copyPossDomains = possDomains[:]
m = 9
n = 9
totalTime = 0		#For Performance Analysis
counter = 0
bts = 0
totalbts = 0


def subSquareCheck(i,j,n):
	'''This function checks for a 3x3 square constraints'''
	global S
	global possDomains
	if n == 1:
		starti = 0
		startj = 0
	elif n == 2:
		starti = 0
		startj = 3
	elif n == 3:
		starti = 0
		startj = 6
	elif n == 4:
		starti = 3
		startj = 0
	elif n == 5:
		starti = 3
		startj = 3
	elif n == 6:
		starti = 3
		startj = 6
	elif n == 7:
		starti = 6
		startj = 0
	elif n == 8:
		starti = 6
		startj = 3
	elif n == 9:	
		starti = 6
		startj = 6
	for p in range(starti,starti+3):
		for q in range(startj,startj+3):
			if S[p][q] != ".":
				try:
					possDomains[i][j].remove(S[p][q])
				except ValueError:
					pass


def setDomain(i,j):
	'''This function checks the entire Domain contraints in a particular empty element'''
	global S
	global possDomains
	if S[i][j] == ".":
		for k in range(n):  #Loop over that row for constraints
			if S[i][k] != ".":
				try:
					possDomains[i][j].remove(S[i][k])
				except ValueError:
					pass
		for k in range(m):  #Loop over that column for constraints
			if S[k][j] != ".":
				try:
					possDomains[i][j].remove(S[k][j])
				except ValueError:
					pass
		if i < 3 and j < 3: #Checking constraints within a particular Sub-Square
			subSquareCheck(i,j,1)
		elif i < 3 and j > 2 and j < 6: #Checking constraints within a particular Sub-Square
			subSquareCheck(i,j,2)
		elif i < 3 and j > 5 and j < 9: #Checking constraints within a particular Sub-Square
			subSquareCheck(i,j,3)
		elif i > 2 and i < 6 and j < 3: #Checking constraints within a particular Sub-Square
			subSquareCheck(i,j,4)
		elif i > 2 and i < 6 and j > 2 and j < 6: #Checking constraints within a particular Sub-Square
			subSquareCheck(i,j,5)
		elif i > 2 and i < 6 and j > 5 and j < 9: #Checking constraints within a particular Sub-Square
			subSquareCheck(i,j,6)
		elif i > 5 and i < 9 and j < 3: #Checking constraints within a particular Sub-Square
			subSquareCheck(i,j,7)
		elif i > 5 and i < 9 and j > 2 and j < 6: #Checking constraints within a particular Sub-Square
			subSquareCheck(i,j,8)
		elif i > 5 and i < 9 and j > 5 and j < 9: #Checking constraints within a particular Sub-Square
			subSquareCheck(i,j,9)
		return 1
	return 0


def isEnd():
	'''This fuction decides whether all the sudoku empty spaces have been filled and the assignment is valid or not'''
	for i in range(m):
		for j in range(n):
			if S[i][j] == ".":
				return False
	return True

def subSquareValidCheck(i,j,n):
	global copyS
	global copyPossDomains
	if n == 1:
		starti = 0
		startj = 0
	elif n == 2:
		starti = 0
		startj = 3
	elif n == 3:
		starti = 0
		startj = 6
	elif n == 4:
		starti = 3
		startj = 0
	elif n == 5:
		starti = 3
		startj = 3
	elif n == 6:
		starti = 3
		startj = 6
	elif n == 7:
		starti = 6
		startj = 0
	elif n == 8:
		starti = 6
		startj = 3
	elif n == 9:	
		starti = 6
		startj = 6
	for p in range(starti,starti+3):
		for q in range(startj,startj+3):
			if not (p == i and q == j):
				if S[p][q] == S[i][j]:
					return False
	return True



def isValid(i,j):
	'''This function will check whether the existing configuration in the Sudoku puzzle is valid or not'''
	global S
	global possDomains
	global copyS
	global copyPossDomains
	for k in range(n):  #Loop over that row for constraints
		if j != k and copyS[i][k] == copyS[i][j]:
			return False
	for k in range(m):  #Loop over that column for constraints
		if i != k and copyS[k][j] == copyS[i][j]:
			return False
	if i < 3 and j < 3: #Checking constraints within a particular Sub-Square
		val = subSquareValidCheck(i,j,1)
	elif i < 3 and j > 2 and j < 6: #Checking constraints within a particular Sub-Square
		val = subSquareValidCheck(i,j,2)
	elif i < 3 and j > 5 and j < 9: #Checking constraints within a particular Sub-Square
		val = subSquareValidCheck(i,j,3)
	elif i > 2 and i < 6 and j < 3: #Checking constraints within a particular Sub-Square
		val = subSquareValidCheck(i,j,4)
	elif i > 2 and i < 6 and j > 2 and j < 6: #Checking constraints within a particular Sub-Square
		val = subSquareValidCheck(i,j,5)
	elif i > 2 and i < 6 and j > 5 and j < 9: #Checking constraints within a particular Sub-Square
		val = subSquareValidCheck(i,j,6)
	elif i > 5 and i < 9 and j < 3: #Checking constraints within a particular Sub-Square
		val = subSquareValidCheck(i,j,7)
	elif i > 5 and i < 9 and j > 2 and j < 6: #Checking constraints within a particular Sub-Square
		val = subSquareValidCheck(i,j,8)
	elif i > 5 and i < 9 and j > 5 and j < 9: #Checking constraints within a particular Sub-Square
		val = subSquareValidCheck(i,j,9)
	if val == False:
		return False
	return True


def findMRV():
	'''This function will find the minimum remaining value heuristic and return the i,j corresponding to it'''
	global copyPossDomains
	global copyS
	global m
	global n
	mini = float("inf")
	#pdb.set_trace()
	for i in range(m):
		for j in range(n):
			if S[i][j] == ".":
				if len(copyPossDomains[i][j]) < mini:
					mini = len(copyPossDomains[i][j])
					p = i
					q = j
	return p,q


def backtrack(i,j):
	'''This function will perform the basic backtracking search and has the parameters as the location of the next cell which'''
	global copyPossDomains
	global copyS
	global bts
	bts += 1
	if isEnd() == True:
		return True
	if copyS[i][j] == ".":
		for element in copyPossDomains[i][j]:
			copyS[i][j] = element
			#print copyPossDomains
			#print copyS
			#pdb.set_trace()
			temp = isValid(i,j)
			if temp == True and isEnd() == True:
				return True
			if temp == True:  #Check if sudoku remains valid after the addition of new element
				m,l = findMRV()

				if backtrack(m,l) == True:
					return True
		copyS[i][j] = "."
		return False
	return False



def rasterize(A):
	string = ""
	for i in range(m):
		for j in range(n):
			string += A[i][j]
	string += "\n"
	return string



if len(sys.argv) != 2:
	print 'Illegal Arguments passed!!'
	sys.exit()

else:
	m = 9 #Number of rows in sudoku puzzle
	n = 9 #Number of columns in sudoku puzzle
	
	ans = ""
	file = open(sys.argv[1])
	line = file.readline(9)
	while line != "":
		bts = 0
		startTime = time.time()
		possDomains = [[],[],[],[],[],[],[],[],[]]
		for i in range(m):
			for j in range(n):
					possDomains[i].append(["1","2","3","4","5","6","7","8","9"])  #Create a list of all the possible domains initially
		S = [[],[],[],[],[],[],[],[],[]]
		for i in range(m-1):
			S[i][:] = line
			line = file.readline(9)
		S[i+1][:] = line
		empty = file.readline(1)        #Read the endofline character
		line = file.readline(9)			#Read the 1st row of next puzzle else read EOF
		for i in range(m):			#Loop over the entire 9 rows and columns
			for j in range(n):
				val = setDomain(i,j)
				if val == 0:
					possDomains[i][j] = []
		
		flager = 0
		copyS = S[:]
		copyPossDomains = possDomains[:]
		for i in range(m):
			for j in range(n):
				if S[i][j] != ".":
					temp = isValid(i,j)
					if temp == True:
						continue
					elif temp == False:
						flager = 1
						break
			if flager == 1:
				break
		if temp == False:
			ans += "Sudoku is Not Solvable\n"
		#Implement Backtrack from here
		else:
			copyS = S[:]
			copyPossDomains = possDomains[:]
			flag = 0
			#for i in range(n):
			#	for j in range(m):
			#		if S[i][j] == ".":
			#			flag = 1
			#			break
			#	if flag == 1:
			#		break
			i,j = findMRV()
			val = backtrack(i,j)		#Call the backtrack search algorithm over the first element in the puzzle
			if val == True:
				ans += rasterize(copyS)
			else:
				ans += "Sudoku is Not Solvable\n"
		endTime = time.time()
		counter += 1
		totalbts += bts
		totalTime += endTime - startTime


	avgTime = totalTime / counter
	avgbts = totalbts / counter
	print avgTime
	print avgbts
	file.close()
	#print possDomains
	#print copyS
	file = open("outputBS-I.txt","w")
	file.write(ans)