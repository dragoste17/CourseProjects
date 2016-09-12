import time
import random
import rubik

def run(start,end):
	visited1 = {start : 0}
	visited2 = {end : 0}
	previous1 = {start : None}
	previous2 = {end : None}
	new1 = []
	new2 = []
	
	if start == end:                     # Base case when start and end is the same
		return []
		
	for i in rubik.quarter_twists:
		x,y,z = search(i)            # will search in the hastable of visited1 
		if x == 1:                   # if search is successful
			continue
		x,y,z = search(i)            # will search in the hastable of visited2
		if x == 1:
			k = i
			while previous1(k) != None:
				z.append(previous1(k))
				k = previous1(k)
			k = i
			while previous2(k) != None:
				z.append(rubik.perm_inverse(previous2(k)))
				k = previous2(k)
			return z
		else:
			new1.append(i)
			previous1[i] = previous(i) + 1
				
			
	
