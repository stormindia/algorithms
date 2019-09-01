#quick sort for duplicate keys ==> 3-way partationing


def quick_sort(data, low, high):
	if(high <= low):
		return

	lt = low 	  	#less than index
	gt = high 		#greater than index
	i = low
	pivot_value = data[low]
	
	while (i <= gt):
		if(data[i] < pivot_value):
			data[i], data[lt] =  data[lt],  data[i]
			lt = lt + 1
			i = i + 1
		elif( data[i] >  pivot_value):
			#print(i , gt)
			data[i], data[gt] =  data[gt],  data[i]
			gt = gt - 1
		else:
			i = i + 1

	quick_sort(data, low,lt-1)
	quick_sort(data, gt + 1 , high)


arr = [1,5,2,7,6,3,9]

quick_sort(arr,0,len(arr)-1)

print(arr)