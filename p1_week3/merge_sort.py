class merge_sort:

    def __init__(self, data):
        self.data = data                            # reference to data
        self.aux_array = [0] * len(data)            # allocate aux_array

    def merge(self, low, mid, high):

        for k in range(low, high+1):                # fix (high+1)
            self.aux_array[k] = self.data[k]
        
        i = low
        j = mid + 1
        
        for k in range(low, high+1):                # fix (high+1)
            if(i > mid):
                self.data[k] = self.aux_array[j]
                j = j + 1
            elif(j > high):
                self.data[k] = self.aux_array[i]
                i = i + 1
            elif(self.aux_array[i] < self.aux_array[j]):
                self.data[k] = self.aux_array[i]
                i = i + 1
            else:
                self.data[k] = self.aux_array[j]
                j = j + 1


    def mergesort(self, low, high):                 # top down approach
        if(low >= high):
            return

        mid = low + (high - low)//2                 
       
        self.mergesort(low, mid)
        self.mergesort(mid+1, high)
        self.merge(low, mid, high)


    def bottom_up_mergesort(self):

        size = 1
        #low = 0

        while(size < len(self.data)):
            low = 0
            while (low < len(self.data)):
                mid = low + size - 1
                high = min(low + size + size -1, len(self.data) -1)         #*********
                self.merge(low, mid, high)
                low = low + 2*size

            size = size + size

        
    def start_sort(self):
        high = len(self.data) - 1
        self.mergesort(0, high)


arr = [10, 2, 30, 0, 4]
arr1 = merge_sort(arr)
#arr1.start_sort()
#print(arr)                          
arr1.bottom_up_mergesort()
print(arr)   