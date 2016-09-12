def insSort(array):
	p=1
	for i in range(1,len(array)):
		temp=array[i]
		for j in range(i-1,-1,-1):
			if temp<array[j]:
				p=0
				array[j+1]=array[j]
		if p==0:
			array[j]=temp	
arr=[4,5,3,2,1]
insSort(arr)
print arr
