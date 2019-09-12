#use MaxPQ method

class binary_heap:

    def __init__(self, data=None):

        self.data = data
        self.N = len(self.data) -1


    def print_heap(self):
        print(self.data)

    def less(self, x , y):

        #print(x,y)
        if(self.data[x] < self.data[y]):
            return True
        else:
            return False


    def sink(self,k,N):

        while(2*k <= N ):

            i = 2*k
            #print(i)
            if(i < N and self.less(i, i + 1)):  #right child (2k + 1) is bigger
                i = i + 1

            if( self.less(k, i) is not True): #parent is not less than children
                return #return   #exit out of loop
            else:
                self.data[k],self.data[i] = self.data[i],self.data[k]
                k = i

    #priority queue using binary_heap
    def sort(self):

        k = self.N // 2

        while(k > 0):
            self.sink(k,self.N)
            k = k -1

        while(self.N > 1):
            self.data[1],self.data[self.N] = self.data[self.N],self.data[1]
            self.N = self.N - 1
            self.sink(1,self.N)



# assume numbers start from 1 index for simplicity
arr = [None,90,80,70,60,50,40,30,20]
arr1 = binary_heap(arr)
arr1.sort()
print(arr)
