#max logn depth of the tree (easy proof) ==> no tall trees
#union - constant time (lgN)
#find - proportional to depth of the two element

class weighted_quick_union:
    def __init__(self, array=None):
        if(array == None):
            pass
        else:
            rows = len(array)
            #self.element_id = [[0]* 2] * rows
            self.element_id = [[0] * 3 for i in range(rows)]
            #self.element_id = numpy.zeros(len(array),3)
            for i in range(0,len(array)):
                self.element_id[i][0] = array[i] #element's root
                self.element_id[i][1] = array[i] #element's value
                self.element_id[i][2] = 1 #size of the tree for current element
                #print(self.element_id[i][2])
            #print(self.element_id)

    def root(self, a):

        i = 0
        while(a != self.element_id[a][0]):
            a = self.element_id[a][0]

        return a

    def isconnected(self, a, b):
        if(self.root(a) == self.root(b)):
            return "connected"
        else:
            return "not connected"

    def union(self, a, b):

        id_a = self.root(a)
        id_b = self.root(b)
        if (id_a == id_b):
            print("already connected")
            return
        elif(self.element_id[id_a][2] < self.element_id[id_b][2]):
            self.element_id[id_a][0] = id_b
            #increment the tree size
            self.element_id[id_a][2] = self.element_id[id_a][2] + self.element_id[id_b][2]
        else:
            self.element_id[id_b][0] = id_a
            #increment the tree size
            self.element_id[id_b][2] = self.element_id[id_b][2] + self.element_id[id_a][2]
        ##major bug #####
        #self.element_id[a][0] = self.root(b)



array_1 = [0,1,2,3,4,5,6,7]
quick_union_1 = weighted_quick_union(array_1)
print(quick_union_1.root(2))
# print(quick_union_1.isconnected(0,0))
#
quick_union_1.union(6,1)
# #print(quick_union_1.root(1))
print(quick_union_1.isconnected(6,1))
#
quick_union_1.union(6,0)
# #print(quick_union_1.root(1))
print(quick_union_1.isconnected(1,0))
