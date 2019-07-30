class quick_find:
    def __init__(self, array=None):
        if(array == None):
            pass
        else:
            rows = len(array)
            #self.element_id = [[0]* 2] * rows
            self.element_id = [[0] * 2 for i in range(rows)]
            for i in range(0,len(array)):
                self.element_id[i][0] = i
                self.element_id[i][1] = array[i]
                #print(self.element_id[i][1])
            #print(self.element_id)

    def isconnected(self, a, b):
        if (a == b):
            return "same elements are connected by default"
        count = 0
        for i in range(0,len(self.element_id)):
            if (self.element_id[i][1] == a):
                id_1 = self.element_id[i][0]
                count = count + 1
            elif(self.element_id[i][1] == b):
                id_2 = self.element_id[i][0]
                count = count + 1
            else:
                pass
            if (count == 2):
                if (id_1 == id_2):
                    return True
                else:
                    return False

        if (count < 2):
            return "elements not in the list error"

    def union(self, a, b):
        if (a == b):
            return "same elements are connected by default"
        count = 0
        for i in range(0,len(self.element_id)):
            if (self.element_id[i][1] == a):
                a_index = i
                count = count + 1
            elif(self.element_id[i][1] == b):
                b_id = self.element_id[i][0]
                count = count + 1
        if (count == 2):
            self.element_id[a_index][0] = b_id
        else:
            return "elements not in the list error"



array_1 = [0,5,2,4,8,9,10]
array_1_qf = quick_find(array_1)
#print(array_1_qf.isconnected(0,11))
array_1_qf.union(5,2)
print(array_1_qf.isconnected(5,2))
