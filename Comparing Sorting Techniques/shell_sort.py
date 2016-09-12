#2013CSB1032
#Shinde Lav Chandrakant





import math




def gapGen(array):
	'''This function will create the gaps to be used while shell sorting'''
	gap=[]
	N=len(array)
	k=1
	while math.floor(N/(2**k)) != math.floor(N/(2**(k+1))) and N/(2**k) != 1:
		gap.append(N/(2**k))
		k=k+1
	gap.append(1)
	return gap







def sort(array):
	'''This will sort the given list of elements using the shell sort technique
	and returns the number of transactions involved in the process'''
	gap=gapGen(array)	
	l=0
	for k in gap:
		for j in range(k,len(array)):
			temp = array[j];
			i=j
			while temp<array[i-k] and i>=k:
				array[i] = array[i-k]
				i = i - k
				l=l+1
			array[i] = temp
	return l








array = [9,5,4,3,2,1,7,6]
l=sort(array)
print array
print l
