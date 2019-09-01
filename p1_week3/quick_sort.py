#randomly shuffling the array is an important step
#preserving randomness gurantees performance in worst cases
#shuffling ensures the pivot element to be random


#for duplicate keys ==> refer duplicate_keys.py
# this implementation can take qudaratic time in case of duplicate keys
# merge sort does not has this problem 

class quick_sort:

	def __init__(self,data=None):
		self.data = data

	def partition(self,low,high):
		i = low
		j = high

		while (True):
			while((self.data[i] <= self.data[low]) and i <= high):		# i <=high check is necessary to stay in bound
	 			i = i + 1

			while((self.data[j] > self.data[low]) and j >= low):		# j >=low check keeps us in bound but is redundant unlike i<=high(?)
				j = j - 1
		
			if(i >= j):		#pointers crossed
				break
			else:		
				self.data[i],self.data[j] = self.data[j],self.data[i] 	# swap the elements	

		self.data[low],self.data[j] = self.data[j],self.data[low]		
		return j


	def quick_sort(self,low,high):

		if(high <= low):
			return

		j = self.partition(low,high)
		self.quick_sort(low, j-1)
		self.quick_sort(j+1, high)

	def start_sort(self):

		#shuffle the array randomly
		#use knuth shuffle from p1_week2

		self.quick_sort(0, len(self.data)-1)



arr = [1,5,2,7,6,3,9]


arr1 = quick_sort(arr)
arr1.start_sort()

print(arr)