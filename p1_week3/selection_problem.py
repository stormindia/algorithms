# finding the kth largest element

class selection:

	def __init__(self,data,k):
		self.data = data
		self.k = k

	def partition(self,low,high):
		i = low
		j = high

		while (True):
			while((self.data[i] < self.data[low]) and i <= high):		# i <=high check is necessary to stay in bound
	 			i = i + 1

			while((self.data[j] > self.data[low]) and j >= low):		# j >=low check keeps us in bound but is redundant unlike i<=high(?)
				j = j - 1
		
			if(i >= j):		#pointers crossed
				break
			else:		
				self.data[i],self.data[j] = self.data[j],self.data[i] 	# swap the elements	

		self.data[low],self.data[j] = self.data[j],self.data[low]		
		return j


	def select(self,low,high):

		#shuffle the array
		#
		#
		#shuffle the array

		if(high <= low):
			return
		while (high > low):
		
			j = self.partition(low,high)
			if(j > self.k):
				high = j - 1
			elif(j < self.k):
				low = j + 1
			else: 
				return self.data[self.k]

		return self.data[self.k]


	def start_find(self):

		#shuffle the array randomly
		#use knuth shuffle from p1_week2

		return self.select(0, len(self.data)-1)


arr = [1,5,2,7,6,3,9]

arr1 = selection(arr,4)

print(arr1.start_find())
