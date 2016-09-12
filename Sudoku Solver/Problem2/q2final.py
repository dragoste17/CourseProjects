import sys


clauses = []

def Cell_Clauses(PropVar):
	cell_clause=[]
	for i in range(9):
		for j in range(9):
			string1 = str(i+1)+str(j+1)
			for k in range(9):
				string2= string1+str(k+1)
				cell_clause.append(PropVar[string2])
			cell_clause.append(0)
			clauses.append(cell_clause)
			cell_clause=[]
	cell_clause=[]
	for i in range(9):
		for j in range(9):
			string1=str(i+1)+str(j+1)
			for k in range(8):
				for l in range(k+1,9):
					string2=string1 + str(k+1)
					string3= string1 + str(l+1)
					cell_clause.append(-1*PropVar[string2])
					cell_clause.append(-1*PropVar[string3])
					cell_clause.append(0)
					clauses.append(cell_clause)
					cell_clause=[]



def Row_Clauses(PropVar):
	row_clauses=[]
	for i in range(9):
		for j in range(9):
			for k in range(9):
				string1=str(i+1)+str(k+1)+str(j+1)
				row_clauses.append(PropVar[string1])
			row_clauses.append(0)
			clauses.append(row_clauses)
			row_clauses=[]
	row_clauses=[]
	for i in range(9):
		for j in range(9):
			string1=str(i+1)
			for k in range(8):
				for l in range(k+1,9):
					string2=string1+str(k+1)+str(j+1)
					string3=string1+str(l+1)+str(j+1)
					row_clauses.append(-1*PropVar[string2])
					row_clauses.append(-1*PropVar[string3])
					row_clauses.append(0)
					clauses.append(row_clauses)
					row_clauses=[]

def Column_Clauses(PropVar):
	column_clauses=[]
	for i in range(9):
		for j in range(9):
			for k in range(9):
				string1=str(k+1)+str(i+1)+str(j+1)
				column_clauses.append(PropVar[string1])
			column_clauses.append(0)
			clauses.append(column_clauses)
			column_clauses=[]
	column_clauses=[]
	for i in range(9):
		for j in range(9):
			string1=str(i+1)
			for k in range(8):
				for l in range(k+1,9):
					string2=str(k+1)+string1+str(j+1)
					string3=str(l+1)+string1+str(j+1)
					column_clauses.append(-1*PropVar[string2])
					column_clauses.append(-1*PropVar[string3])
					column_clauses.append(0)
					clauses.append(column_clauses)
					column_clauses=[]
				

def Block_Clauses(PropVar):
	block_clauses=[]
	block=[]
	blocks=[]
	starti=0
	startj=0
	for starti in range(0,7,3):
		for startj in range(0,7,3):
			for k in range(9):
				for i in range(starti,starti+3):
					for j in range(startj,startj+3):
						string1=str(i+1)+str(j+1)+str(k+1)
						block_clauses.append(PropVar[string1])
						block.append(string1)
				blocks.append(block)
				block_clauses.append(0)
				clauses.append(block_clauses)
				block_clauses=[]
				block=[]
	block_clauses=[]
	for i in range(len(blocks)):
		for j in range(9):
			for k in range(j+1,9):
				block_clauses.append(-1*PropVar[blocks[i][j]])
				block_clauses.append(-1*PropVar[blocks[i][k]])
				block_clauses.append(0)
				clauses.append(block_clauses)
				block_clauses=[]
	


PropVar = {}

total=1
for i in range(9):
	for j in range(9):
		for k in range(9):
			variable =str(i+1)
			variable=variable + str(j+1) + str(k+1)
			PropVar[variable]=total
			total=total+1

Cell_Clauses(PropVar)
Row_Clauses(PropVar)
Column_Clauses(PropVar)
Block_Clauses(PropVar)
fo=open("p.txt","r")
lines=fo.read().split("\r")
del lines[-1]
line_number = int(sys.argv[1])
for i in range(len(lines)):
	lines[i]=list(lines[i])

for i in range(len(lines[line_number])):
	if lines[line_number][i] != '.' :
		row= i/9 + 1
		column = i%9 +1
		FilledClause=[PropVar[str(row)+str(column)+lines[line_number][i]],0]
		clauses.append(FilledClause)

answer = open("answer.txt","w")
answer.write("p cnf "+ "729 " + str(len(clauses))+"\n")
for i in range(len(clauses)):
	for j in range(len(clauses[i])):
		answer.write(str(clauses[i][j])+" ")
	answer.write("\n")
		
