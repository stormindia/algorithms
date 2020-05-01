#Refer Part2 week2 Prims algo
#https://algs4.cs.princeton.edu/24pq/IndexMinPQ.java.html
#Corner cases needs to be fixed

#Associate an index between 0 and N-1 with each key in a PQ
#Client can insert and delete the minimum
#Client can change the key by specifying index

#Uses same code as that of MinPQ.py from p1_week4
#keys[i] --> priority of i
#pq[i] --> index of the key in heap position i
#qp[i] --> heap position of the key with index i
#use swim(qp[k]) to implement decreaseKey(k.keys)

#i           0   1   2     3   4   5   6    7   8
#keys[i]     A   S   O    R   T   I   *N*   G   -
#pq[i]       -   0  *6*   7   2   1    5    4   3
#qp[i]       1   5   4    8   7   6   *2*   3   -

#start with qp[i] to find what is the value of the element in a heap
#For ex -
# qp[2] = 4 ==> pq[4] = 2 ==> keys[2] = O  ==> at 4th index of the heap, we will find O


class IndexPQ:

#Create indexed PQ with indices 0,1,..,N-1
    def __init__(self,N):
        self.MaxN = N #Max elements in a PQ
        self.n = 0 #Number of elements in a PQ
        keys = []*(self.N + 1)
        pq = []*(self.N + 1)
        qp = [-1]*(self.N + 1)


    def isEmpty(self):
        if(self.n == 0):
            return True
        return False

    def isValidIndex(self,i):
        if(i < 0 or i >= MaxN):
            return False
        return True

#Check if 'i' is an index on this PQ
    def contains(self,i):
        self.isValidIndex(i)
        return self.qp[i] != -1


    def greater(self, x , y):

        #print(x,y)
        a = self.keys[self.pq[x]]
        b = self.keys[self.pq[j]]

        if(a < b):
            return False
        else:
            return True

    def exchange(self,x,y):
        pq[i],pq[j] = pq[j], pq[i]
        qp[pq[i]] = i
        qp[pq[j]] = j

    def swim(self,k):
        while(k > 1 and self.greater(k/2,k)):
            self.exchange(k,k/2)
            k = k/2

    def sink(self,k):
        while(2*k <= self.n):
            i = 2*k
            if(i < self.n and self.greater(i,i+1)):
                i += 1 #do nothing
            if(self.greater(k,i) is False):
                break
            self.exchange(k,i)
            k = i

    def changeKey(self,i,key):
        self.keys[i] = key
        self.swim(self.qp[i])
        self.sink(self.qp[i])

    def decreaseKey(self,i,key):
        self.keys[i] = key
        self.swim(self.qp[i])

    def increaseKey(self,i,key):
        self.keys[i] = key
        self.sink(self.qp[i])

    def size(self):
        return self.n

    def insert(self, i , key):
        self.isValidIndex(i)
        if(self.contains(i)):
            return
        self.n += 1

        self.qp[i] = n
        self.pq[n] = i
        self.keys[i] = key

        self.swim(self.n)

    def minIndex(self):
        if(n == 0):
            return False
        return self.pq[1]

    def minKey(self):
        if(n == 0):
            return False
        return self.keys[self.pq[1]]

    
    def delMin(self):
        min = self.pq[1]
        self.exchange(1,self.n-1)

        self.n = self.n - 1
        return min
