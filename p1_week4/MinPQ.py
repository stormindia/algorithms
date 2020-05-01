#Minimum priority queue based on binary heap

#For MaxPQ based on binary_heap, refer heap_sort.py

#For MaxPQ based on linked list, refer priority_queue.py


class MinPQ:

    def __init__(self, data=None):

        self.data = data
        self.heap = []*(len(self.data)+1)
        self.heap.append(None)
        for i in self.data:
            self.heap.append(i)
        self.n = len(self.data) // 2
        for i in range(self.n,1,-1):
            self.sink(i)


    def print_heap(self):
        print(self.heap)

    def greater(self, x , y):

        #print(x,y)
        if(self.heap[x] < self.heap[y]):
            return False
        else:
            return True

    #in case a child becomes bigger than parent
    def swim(self, k):

        while(k > 1 and self.greater(k, int(k/2))):
            self.heap[k],self.heap[k//2] = self.heap[k//2],self.heap[k]
            k = k//2

        return

    #In case, a parent is less than one (or both) of its child   ==> different from above ==> That parent can be a child of another node.
    #It can have value less than its parent. But its children can have value larger than their parent
    def sink(self,k):

        while(2*k <= len(self.heap) - 1):

            i = 2*k
            #print(i)
            if(i < len(self.heap)-1 and self.greater(i, i + 1)):  #right child (2k + 1) is bigger
                i = i + 1

            if( self.greater(k, i) is not True): #parent is not less than children
                return #return   #exit out of loop
            else:
                self.heap[k],self.heap[i] = self.heap[i],self.heap[k]
                k = i

    def insert(self,k):
        self.heap.append(k)
        self.swim(len(self.heap)-1)


    #priority queue using binary_heap
    def delMin(self):

        if(len(self.heap) == 1):
            print("no element present in heap")
            return False

        print("deleted max element is {}".format(self.heap[1]))

        tmp = self.heap[1]
        self.heap[1] = self.heap[len(self.heap)-1]
        self.heap[len(self.heap)-1] = tmp

        #print(self.heap , len(self.heap))

        del[self.heap[len(self.heap)-1]]    #prevent loitering
        self.sink(1)



#arr = [100,90,80,70,60,50,40,30,20]
arr = [30,20,40,50,60,70,80,90,100]
arr1 = MinPQ(arr)
arr1.delMax()
arr1.delMax()
arr1.delMax()
arr1.delMax()
arr1.print_heap()
arr1.delMax()
arr1.print_heap()
arr1.delMax()
arr1.delMax()
arr1.delMax()
arr1.delMax()
arr1.delMax()
arr1.insert(10)
arr1.print_heap()
