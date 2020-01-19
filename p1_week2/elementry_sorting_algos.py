def swap_values(a,b,data=None):
	tmp = data[a]
	data[a] = data[b]
	data[b] = tmp
	#can use swap function directly


def selection_sort(data=None):

	i = 0
	while(i < len(data)):
		min = i
		for j in range(i, len(data)):
			if(data[j] <= data[min]):
				min = j
		if(min != i):
			swap_values(min,i,data)

		i = i +1

	return data



def insertion_sort(data=None):

	for i in range(0, len(data)-1):

		if(data[i] <= data[i+1]):
			pass
		else:
			j = i+1
			while(j > 0 and data[j] < data[j-1] ):
#				if(data[j] < data[j-1]):
				swap_values(j,j-1,data)
				j = j -1

	return data


def shell_sort(data=None):

# a g-sorted array remains g-sorted even after h-sorting it
#increment factor = 3x + 1
	N = len(data)
	#print(N)
	h = 1
	while(h < int(N/3)):
		h = 3*h + 1
		#print(h)
	while(h >= 1):
		for i in range(h,N):

			tmp = data[i]
			j = i
			while j >= h and data[j -h] > tmp :
				data[j] = data[j-h]
				j = j - h

			data[j] = tmp

		h = h//3

	return data




array_1 = [5,3,1,7,9,2,100,50,62,70,89,98,11]

#print(selection_sort(array_1))
print(insertion_sort(array_1))
#print(shell_sort(array_1))
