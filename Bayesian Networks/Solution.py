import sys
#import networkx as nx
import copy
import itertools
import VE
import RS

def file_handeling():

	if len(sys.argv) == 3:

		file = open(sys.argv[1],"r")
		lines = file.readlines()
		for i in range(len(lines)):
			lines[i] = lines[i].split()

			'''n = int(lines[0][0])
			arrayObj = [None] * 10
			for i in range(1,n+1):
				arrayObj[i] = elem(i)'''
	

		i = 1
		count = 0
		while i < len(lines):
			i += 2**(len(lines[i]) - 1) + 1
			count += 1

		probabilities = [[] for x in range(count)]


		i = 1
		count = 0
		relations = []  #This will store all the relationships mentioned as parents of elements
		while i < len(lines):
				
			relations.append(lines[i])
			k = 2**(len(lines[i]) - 1)
			j = k
			temp = 0
			while j > 0:
				j -= 1
				temp += 1
				probabilities[count].append(lines[i+temp])
			i += 2**(len(lines[i]) - 1) + 1
			count += 1

		fi = open(sys.argv[2],"r")
		lines2= fi.readlines()
		for i in range(len(lines2)):
			lines2[i] = lines2[i].split()
			#print "R",relations
			#print "P",probabilities
		query = []
		observed = []
		for i in range(len(lines2)):
			query.append([])
			observed.append([])
			for j in range(len(lines2[i])): 
				if(lines2[i][j]!="e"):
					if(j>1):	
						query[i].append(lines2[i][j])
					continue
					
				else:
					j=j+1
					while(j<len(lines2[i])):
						observed[i].append(lines2[i][j])
						j=j+1
					break
			#print "q",query
			#print "o",observed
		
		return relations,probabilities,lines2,observed,query

	


	else:
		print "Invalid Arguments!"


relations,probabilites,lines2,observed,query= file_handeling()

for i in range(len(lines2)):
	if(lines2[i][0]=="ve"):
		VE.VE(i,sys.argv[1],sys.argv[2])
	elif(lines2[i][0]=="rs"):
		RS.RS(i,sys.argv[1],sys.argv[2])
	else :
		print "Invalid Query"
		break

#print "R",relations
#Variables = set_variables(relations)
#Variables.sort()
#print "V",Variables


