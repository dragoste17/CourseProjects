import time
import rubik
import random

class queue:
	''' This will create a queue and while removing maintain track of seen elements'''
	def __init__(self,val):
		'''Creates an empty queue'''
		self.item = [val]
		
	def push(self,a):
		'''Adds a list to the queue'''
		for i in a:
			self.item.append(i)
		
	def pop(self):
		'''Removes the element first entered in the queue and adds to seen list'''
		if len(self.item) != 0: #If the list is not empty
			x = self.item[0]
			del(self.item[0])  # Deques the element from the queue
			return x
			

class prev:
	def __init__(self,val):
		self.val = val
		self.prev = None
		self.myOrigin = None

import pdb



def shortest_path(start,end):
	#pdb.set_trace()
	p1 = prev(start)
	p2 = prev(end)
	q1 = queue(p1)
	q2 = queue(p2)
	visited1 = [[] for _ in range(11197)]
	visited2 = [[] for _ in range(11197)]
	z = []
	term = 0
	
		
	def children1(a):
		new = []
		for i in rubik.quarter_twists:
			x = rubik.perm_apply(i,a.val)
			p = prev(x)
			l,m,n = search1(p)            # visited is the hash table storing visited elements
			if l == 1:	
				continue
			else:
				p.prev = a
				p.myOrigin = i
				insert1(p)      # this is inserting element in hash table
				new.append(p)
		return new
	
	def children2(a):
		new = []
		for i in rubik.quarter_twists:
			x = rubik.perm_apply(i,a.val)
			p = prev(x)
			l,m,n = search2(p)            # visited is the hash table storing visited elements
			if l == 1:	
				continue
			else:
				p.prev = a
				p.myOrigin = rubik.perm_inverse(i)
				insert2(p)      # this is inserting element in hash table
				new.append(p)
		return new


	def insert1(p):
		''' This will insert in the hash table'''
		a = 0
		for i in range(len(p.val)):
			a += (2**i)*p.val[i]
		d = a % 11197
		visited1[d].append(p)
		
	def insert2(p):
		''' This will insert in the hash table'''
		a = 0
		for i in range(len(p.val)):
			a += (2**i)*p.val[i]
		d = a % 11197
		visited2[d].append(p)
	

	def search1(p):
		''' This will search from the hash table a particular element'''
		a = 0
		for i in range(len(p.val)):
			a += (2**i)*p.val[i]
		d = a % 11197
	        for i in range(len(visited1[d])):
	        	if visited1[d][i].val == p.val:
	        		return 1,d,i
		return -1,d,i
	
	def search2(p):
		''' This will search from the hash table a particular element'''
		a = 0
		for i in range(len(p.val)):
			a += (2**i)*p.val[i]
		d = a % 11197
	        for i in range(len(visited2[d])):
	        	if visited2[d][i].val == p.val:
	        		return 1,d,i
		return -1,d,i
	
	
	
	if start == end:                     # Base case when start and end is the same
		return []
	
	lav = prev(end)
	insert2(lav)
		
	while q1.item != None and q2.item != None:
		
		if term > 12000:
			return None
		
		x = children1(q1.pop())
		q1.push(x)
		for i in x:
			a1,b1,c1 = search2(i) # Search the element in 2nd table
			if a1 == 1:
				temp = i
				while temp.prev != None:
					z.append(temp.myOrigin)
					temp = temp.prev
				z.reverse()
				temp = visited2[b1][c1]
				while temp.prev != None:
					z.append(temp.myOrigin)
					temp = temp.prev
				return z
				
				
		x = children2(q2.pop())
		q2.push(x)
		for i in x:
			a2,b2,c2 = search1(i) # Search the element in 2nd table
			if a2 == 1:
				temp = i
				while temp.prev != None:
					z.append(temp.myOrigin)
					temp = temp.prev
				temp = visited1[b2][c2]
				y = []
				while temp.prev != None:
					y.append(temp.myOrigin)
					temp = temp.prev
				y.reverse()
				y.extend(z)
				return y
		
		term += 1
