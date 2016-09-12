#2013CSB1032
#Shinde Lav Chandrakant





import random



insSort_time=[]
modInsSort_time=[]


list_size = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]

avg_alpha = [58, 139, 113, 154, 228, 314, 340, 500, 546, 598, 645, 682, 668, 696, 1372, 1837, 1080, 1987, 1494, 1788, 1920, 1485, 1760, 3453, 2911, 3266, 3056, 3383, 2822, 4231, 5664, 4750, 5612, 4615, 7969, 6025, 8468, 6408, 6556, 6053, 11314, 8540, 7691, 7965, 7754, 9568, 8192, 9353, 10129, 14875, 9295, 9653, 10499, 11335, 11753, 11578, 12829, 14753, 15628, 12547, 14953, 14095, 13964, 17409, 18171, 17303, 16433, 22634, 16923, 22129, 17261, 21437, 27726, 27250, 22747, 20654, 25266, 19992, 19537, 26304, 21595, 24687, 36578, 29552, 26830, 37585, 28759, 26501, 29378, 37976, 30084, 30098, 36581, 36748, 34287]





def twocheck(arr,alpha):
	'''This function will attempt to sort the array by picking up randomly two numbers
	and trying to swap them alpha times ultimately leading to all numbers being picked up and sorted if lucky'''
	for elem in range(alpha):
		a=random.randrange(len(array))
		b=random.randrange(len(array))
		if a>b:
			a,b=b,a
		if a<b:
			if arr[a]>arr[b]:
				arr[a],arr[b]=arr[b],arr[a]









def insSort(array):
	'''This will sort the array in ascending order by using the insertion sort method
	and returns the number of transactions required in the process'''
	k=0
	for i in range(1,len(array)):
		temp=array[i]
		j=i-1
		while temp<array[j] and j>-1:
			array[j+1]=array[j]
			j=j-1
			k=k+1
		array[j+1]=temp
	return k








def compare(array,alpha):
	'''This function will call both the types of sorting individually and return the number of
	transactions required in both cases'''
	arr = array[:]
	t1 = insSort(arr)
	twocheck(array,alpha)
	t2 = insSort(array)
	insSort_time.append(t1)
	modInsSort_time.append(t2)
	return [t1,t2]







for i in range(len(list_size)):
	array = random.sample(range(1000), list_size[i])
	T = compare(array,avg_alpha[i])
print list_size
print insSort_time
print modInsSort_time
