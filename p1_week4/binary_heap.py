# for any confusion refer the video p1_week4/binary heaps
# minor corner cases fixing left

class binary_heap:

    def __init__(self, data=None):

        self.data = data
        self.heap = [None]
        for i in range(len(self.data)):
            self.heap.append(self.data[i])

        # 0 1 2 3 4 5 6 7 8 9 ==> indexes
        # - A B C D E F G H I ==> Value at these indexes ==> nothing at 0th index for simplicity
        # Properties of binary heap
        # root value is at 1         -------------------------------------------------->|
        # root value is largest value                                                   |
        # parent of node k is at k/2 and children are at 2k and 2k+1                    |
        # parent value > children value ----------------------------------------------->|

    def print_heap(self):
        print(self.heap)

    def less(self, x , y):

        #print(x,y)
        if(self.heap[x] < self.heap[y]):
            return True
        else:
            return False

    #in case a child becomes bigger than parent
    def swim(self, k):

        while(k > 1 and self.less(k, int(k/2))):
            self.heap[k],self.heap[k//2] = self.heap[k//2],self.heap[k]
            k = k//2

        return

    #In case, a parent is less than one (or both) of its child   ==> different from above ==> That parent can be a child of another node.
    #It can have value less than its parent. But its children can have value larger than their parent
    def sink(self,k):

        while(2*k <= len(self.heap) - 1):

            i = 2*k
            #print(i)
            if(i < len(self.heap)-1 and self.less(i, i + 1)):  #right child (2k + 1) is bigger
                i = i + 1

            if( self.less(k, i) is not True): #parent is not less than children
                return #return   #exit out of loop
            else:
                self.heap[k],self.heap[i] = self.heap[i],self.heap[k]
                k = i

    def insert(self,k):
        self.heap.append(k)
        self.swim(len(self.heap)-1)



    #priority queue using binary_heap
    def delMax(self):

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



arr = [100,90,80,70,60,50,40,30,20]
arr1 = binary_heap(arr)
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
