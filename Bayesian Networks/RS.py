import sys
#import networkx as nx
import copy
import itertools
import trial
import random

def RS(rejectanswer,filename1,filename2):

	def Observed(tableCopy,j,ind,var):
		toDelete = []
		l=[]
		tablel=copy.deepcopy(tableCopy[j])
		jlist=j.split(",")
		for i in range(len(jlist)):
			if(i!=ind):
				l.append(jlist[i])
		l=",".join(l)
		del tableCopy[j]
		tableCopy[l]=tablel
		j=l
		#print tableCopy, ind, var
		for i in range(len(tableCopy[j])):
			if(tableCopy[j][i][ind]!=var):
				toDelete.append(i)
				#print "TODEL",i
			else:
				new_tuple = ()
				for k in range(len(tableCopy[j][i])):
					if (k!=ind):
						new_tuple += (tableCopy[j][i][k],)
				#print "NEWTUP",new_tuple
				tableCopy[j][i]=new_tuple
	
		total=0
		for i in range(len(toDelete)):
			del tableCopy[j][toDelete[i]-total]
			total=total+1
			
		return tableCopy



	def probabilityassign(t):
		t=float(t)
		#print "t",t
		r= random.random()
		#print "r",r
		return r < t

	def rejectionSampling(order,table,O,Q):
		#print "HERE"
	
		assignmentdict={}
		assignment=[]
		tablecopy=copy.deepcopy(table)
		#print order
		for i in order:
			#print i
			for j in tablecopy:
				tum = j.split(",")
				#print j,tum
				if(str(i) in tum):
					#print tum
					if(len(tablecopy[j])==2):
						#print len(tablecopy[j])
						assign=probabilityassign(tablecopy[j][0][-1])
						#print "Ass",assign
						if(i in O):
							if(O[i]!=assign):
								#print O[i]
								return None
							else:	
								assignmentdict[i]=assign
								#print "MINELSE"
								del tablecopy[j]
								for k in tablecopy:
									tum = k.split(",")
									if(str(i) in tum):
										tablecopy=Observed(tablecopy,k,tum.index(i),assign)
								#print i,tablecopy
								break
						else:
							assignmentdict[i]=assign
							#print "MINELSE"
							del tablecopy[j]
							for k in tablecopy:
								tum = k.split(",")
								if(str(i) in tum):
									tablecopy=Observed(tablecopy,k,tum.index(i),assign)
							#print i,tablecopy
							break
		#print assignmentdict
		#print Q
		for i in assignmentdict:
			#print i
			if(i in Q):
				#print i,Q[i],assignmentdict[i]
				if(Q[i]!=assignmentdict[i]):
					return False
		return True
								


	def set_variables(relations):
	
		Variable = []
		for i in relations:
			for j in i:
				if j not in Variable:
					Variable.append((j))
	
		return Variable


	def MakeTable(relations,probabilites):
		table={}
		for i in range(len(relations)):
			n = len(relations[i])
			table2 = list(itertools.product([True,False], repeat=n))
			tome=probabilites[i]
			for j in range(len(table2)):
				one=j%(len(table2)/2)
				if(j<len(table2)/2):
					two=0
				else:
					two=1
				table2[j] += (tome[one][two],)
			joined=",".join(relations[i])
			table[joined]=table2
		
		return table
	


	def file_handeling():

		if len(sys.argv) == 3:

			file = open(filename1,"r")
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

			fi = open(filename2,"r")
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
	#print "R",relations
	Variables = set_variables(relations)
	Variables.sort()
	#print "V",Variables
	graph=[]
	for i in relations:
		if(len(i)>1):
			for j in range(1,len(i)):
				toapp=[]
				toapp.append(i[j])
				toapp.append(i[0])
				graph.append(toapp)

	alltable=MakeTable(relations,probabilites)
	order=trial.sort_direct_acyclic_graph(graph)
	Ob=[]
	Co=[]
	Qu=[]
	for i in range(len(observed)):
		Ob.append({})
		Co.append({})

	for i in range(len(query)):
		Qu.append({})

	for i in range(len(query)):
		for j in query[i]:
			if(j[0]=="~"):
				Qu[i][j[1:]]=False
			else:
				Qu[i][j]=True
	
	for i in range(len(observed)):
		for j in observed[i]:
			if(j[0]=="~"):
				Ob[i][j[1:]]=False
			else:
				Ob[i][j]=True
	#print Ob,Qu
	final=[]
	for i in range(1000):
		kyu=rejectionSampling(order,alltable,Ob[rejectanswer],Qu[rejectanswer])
		if(kyu!= None):
			final.append(kyu)

	notrue= final.count(True)
	if(final != []):
		Answer=float(float(notrue)/float(len(final)))
	else:
		Answer=0
	fo=open("answer.txt","a")
	fo.write(str(Answer)+"\n")
	fo.close()
	
	
	

