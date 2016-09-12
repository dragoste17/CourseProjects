import sys
#import networkx as nx
import copy
import itertools

def VE(varanswer,filename1,filename2):

	
	def set_variables(relations):

		Variable = []
		for i in relations:
			for j in i:
				if j not in Variable:
					Variable.append((j))

		return Variable


	def set_factors(relations,probabilites):
		yes=""
		factors={}
		facts=[]
		total=0
		for i in relations:
			yes=""
			for j in i:
				yes=yes+j
			factors[yes]=probabilites[total]
			facts.append(yes)
			total=total+1
	
		return factors,facts


	def MakeTable(factors,facts):
		#print "facts",facts
		table=[]
		for i in facts:
			n = len(i)
			table2 = list(itertools.product([True,False], repeat=n))
			tome=factors[i]
			for j in range(len(table2)):
				one=j%(len(table2)/2)
				if(j<len(table2)/2):
					two=0
				else:
					two=1
				table2[j] += (tome[one][two],)
			table.append(table2)
		return table


	def Observed(tableCopy,j,ind,istrue):
		toDelete = []
		if(istrue ==1):
			var= True
		else:
			var=False

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

	def summ(var,T,fac):

		ind=fac.index(var)
		n=len(fac)-1
		table2 = list(itertools.product([True,False], repeat=n))
		#print "TAB@",table2
		for i in range(len(table2)):
			suum=0
			for j in range(len(T[0])):
				ok=copy.deepcopy(T[0][j])
				newtup=()
				for k in range(len(ok)-1):
					if(k!=ind):
						newtup+=(ok[k],)
				if(newtup==table2[i]):
					#print "HERE"
					suum+=float(ok[-1])
		
			table2[i] += (suum,)
		new=""
		for i in range(len(fac)):
			if(i != ind):
				new+=str(fac[i])
		fac=new
	
		return table2, fac





	def Products(Rs,Rs2,tableCopy):

		#print Rs
		#print Rs2
		tableRs=[]
		fac=Rs2[0]
		fac2=0
		if(len(Rs2)==1):
			n=len(fac)
			table2 = []
			table2.append(Rs[0])
			return table2,fac
		
		for j in range(1,len(Rs2)):
			#print "present",j,len(Rs2)
			if((set(fac) & set(Rs2[j]))==set([])):
				fac=fac+Rs2[j]
				n=len(fac)
				table2 = list(itertools.product([True,False], repeat=n))
				#print fac
				if(tableRs==[]):
					for i in range(len(table2)):
						table2[i] += (float(Rs[fac2][i/2**(len(fac)-1)][-1])*float(Rs[j][i%len(Rs2[j])][-1]),)
						#print i,table2[i][-1]
					tableRs.append(table2)
				else:
					for i in range(len(table2)):
						#print "please",i
						#print i/len(Rs2[j])
						table2[i] += (float(tableRs[0][i/len(fac)][-1])*float(Rs[j][i%len(Rs2[j])][-1]),)
					tableRs[0]=table2
	
			else :
				common=[]
				inone=[]
				intwo=[]
				for i in range(len(Rs2[j])):
					if (Rs2[j][i] not in fac):
						fac+=Rs2[j][i]
					else:
						common.append(Rs2[j][i])
						inone.append(fac.index(Rs2[j][i]))
						intwo.append(i)
					
				n=len(fac)
				#print "fac",fac
				#print "tb",tableRs
				table2 = list(itertools.product([True,False], repeat=n))
				if(tableRs !=[]):
					total=0
					#print "Ca",common
					#print inone,intwo
					for p in range(len(tableRs[0])):
					
						for q in range(len(Rs[j])):
							totalloop=0
							for r in range(len(common)):
								if(tableRs[0][p][inone[r]]!=Rs[j][q][intwo[r]]):
									break
								totalloop +=1
						
							if(totalloop!=len(common)):
								continue
							else:
								table2[total]+=(float(tableRs[0][p][-1])*float(Rs[j][q][-1]),)
								total +=1
					tableRs[0]=table2
					#print "C",common
					#print tableRs
						
				else:
					#print "C",common
					#print inone,intwo
					total=0
					for p in range(len(Rs[fac2])):
					
						for q in range(len(Rs[j])):
							totalloop=0
							for r in range(len(common)):
								#print "rin",r
								if(Rs[fac2][p][inone[r]]!=Rs[j][q][intwo[r]]):
									#print "IT BROKE"
									break
								totalloop+=1
					
							#print "r",totalloop
							if(totalloop != len(common)):
								continue
							else:
								#print "total",total
								table2[total]+=(float(Rs[fac2][p][-1])*float(Rs[j][q][-1]),)
								#print table2[total]
								total +=1
					tableRs.append(table2)
			
	
		
		return tableRs, fac
		
		
						
		











	def Variable_Elimination(Variables,factors,facts,o,q,table):

		final_Variables=[]
		query_Variables=[]
		observed_Variables=[]
		present_Factors=[]
		factors2=copy.deepcopy(factors)
		tableCopy=copy.deepcopy(table)
		for i in q:
			if(i[0]!="~"):
				var=i[:]
				if(int(var)>9):
					var=chr(ord('a') + int(var)-10)	
				query_Variables.append((str(var)))
			else:
				j=i
				var=int(j[1:])
				if(int(var)>9):
					var=chr(ord('a') + int(var)-10)	
				query_Variables.append(str(var))
		
		for i in o:
			if(i[0]!="~"):
				observed_Variables.append((i))
			else:
				j=i
				observed_Variables.append((j[1:]))
		for i in Variables:
			if((i) not in query_Variables):
				final_Variables.append(i)
		
		#print "Q",query_Variables
		#print "F",final_Variables
		#print "O",observed_Variables
		for i in final_Variables:
			#print "i",i
			if((i) in observed_Variables):
				#print facts
				inob=observed_Variables.index((i))
				yes=o[inob]
				if(yes[0]=="~"):
					istrue=0
				else:
					istrue=1
				for j in range(len(facts)):
					if(str(i) in str(facts[j])):
						ind=facts[j].index(str(i))
						if(ind==0):
							if(istrue==1):
								tableCopy=Observed(tableCopy,j,ind,istrue)
								toapp=""
								#print tableCopy
								for l in range(len(facts[j])):
									if(l!=ind):
										toapp += (facts[j][l])
								facts[j]=toapp
							elif (istrue==0):
								tableCopy=Observed(tableCopy,j,ind,istrue)
								toapp=""
								for l in range(len(facts[j])):
									if(l!=ind):
										toapp += (facts[j][l])
								facts[j]=toapp
						elif(ind>0):
							tableCopy=Observed(tableCopy,j,ind,istrue)
							toapp=""
							for l in range(len(facts[j])):
								if(l!=ind):
									toapp += (facts[j][l])
							facts[j]=toapp
			else:
	
				#print "HERE",facts
				#print "HERE2",tableCopy
				twototal=0
				Rs={}
				Rs2=[]
				places=[]
				for j in range(len(facts)):
					#print "ssup",j,facts
					if(str(i) in facts[j]):
						places.append(j)
						Rs[twototal]=copy.deepcopy(tableCopy[j])
						Rs2.append(copy.deepcopy(facts[j]))
						twototal=twototal+1
		
				total=0
				for t in places:
					del tableCopy[t-total]
					del facts[t-total]
					total=total+1
		
				#print tableCopy
				#print "B5",Rs,Rs2
				T,fac = Products(Rs,Rs2,tableCopy)
				#print "B4",i,T,fac
				T,fac= summ(str(i),T,fac)
				#print "B6",T,fac
				tableCopy.append(T)
				facts.append(fac)
				#print "af",facts

		todel=[]
		for i in range(len(facts)):
			if(facts[i]==""):
				todel.append(i)
		total=0
		for i in range(len(todel)):
			del facts[todel[i]-total]
			del tableCopy[todel[i]-total]
			total+=1
		#print tableCopy
		T,fac = Products(tableCopy,facts,tableCopy)
		#print "PreAnswer",T,fac
		return T,fac
		
		
	




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
		
				for l in range(len(lines[i])):
					if(int(lines[i][l])>9):
						lines[i][l]=chr(ord('a') + int(lines[i][l])-10)		
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
	Variables = set_variables(relations)
	#print "V",Variables

	#print Variables
	#print query

	factors,facts = set_factors(relations,probabilites)

	table = MakeTable(factors,facts)


	AnswerTable,fac=Variable_Elimination(Variables,factors,facts,observed[varanswer],query[varanswer],table)
	aww=[]
	aww2=[]
	for i in fac:
		aww2.append(i)
	for i in fac:
		if(i>="1" and i<="9"):
			aww.append(i)
		else:
			aww.append(str(ord("a")-ord(i)+10))
	
	#print aww
			
			
	Qu=[]
	for i in range(len(query)):
		Qu.append({})

	for i in range(len(query)):
		for j in query[i]:
			if(j[0]=="~"):
				Qu[i][j[1:]]=False
			else:
				Qu[i][j]=True
	
	for i in range(len(AnswerTable[0])):
		totallen=0
		var=0
		for j in Qu[varanswer]:
			if(int(j)>9):
				var=chr(ord('a') + int(j)-10)
			else:
				var=j
			india=aww2.index(var)
			if(AnswerTable[0][i][india]!= Qu[varanswer][j]):
				break
			totallen+=1
		if(totallen==len(Qu[varanswer])):
			Answer=AnswerTable[0][i][-1]
			fo=open("answer.txt","a")
			fo.write(str(Answer)+"\n")
			fo.close()
			
			
