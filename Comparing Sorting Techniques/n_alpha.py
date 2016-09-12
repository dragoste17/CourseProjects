#2013CSB1032
#Shinde Lav Chandrakant





import random
import pdb
from matplotlib import pyplot





def retArray(k):
	'''This function wil return an array of length "k", which is given as an argument.'''
	array = [random.choice(range(1000)) for _ in range(k)]
	return array









def checkSort(array):
	'''This will check if the array is sorted and repeats two check sort with incremented alpha.'''
	c=1
	for i in range(len(array)-1):
		if array[i]>array[i+1]:
			c=0
	return c









def twocheck(array):
	'''This method will attempt to sort the array by picking up randomly two numbers
	and trying to swap them alpha times, ultimately leading to all numbers by incrementing alpha till sorted.'''
	te = 1
	alp=0
	while te==1:	
		a = random.randrange(len(array))
		b = random.randrange(len(array))
		alp+=1		
		if a>b:
			a,b=b,a
		if array[a]>array[b]:
			array[a],array[b]=array[b],array[a]
		m = checkSort(array)
		if m==1:
			break
	return alp





alphaArray = []
def avgAlpha(array):
	'''This function will run 2 check alpha for 100 times and then calculate the average value
	of alpha that is obtained.''' 
	tot = 0
	for i in range(0,100):
		tot = tot + twocheck(array)
	alphaArray.append(tot/100)






def graph(x,y):
	'''This function will plot a graph of the two given inputs x and y'''
	pyplot.ylabel('Alpha')
	pyplot.xlabel('n')
	pyplot.plot(x,y)
	pyplot.show()







kArray=[]
for i in range(1,20):
	kArray.append(i)
	array = retArray(i)
	avgAlpha(array)
print kArray
print alphaArray
graph(kArray,alphaArray)
