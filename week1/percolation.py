class percolation:
    def __init__(self, N):
        self.N = N
        self.grid_size = N**2
        #create grid
        #grid structure -
        # N*N grid
        # each element contains 4 values in respective order
        # root value{0} , element's value(index value){1}, open or closed{2}, tree size of that element{3}
        # initially all elements values are equal to root value
        # initially all elements are closed execept v_top and v_bottom
        # initially tree size of all elements is 1 execept v_top and v_bottom so that root always points towards them
        self.grid = [[i,i, False, 1] for i in range(self.grid_size)]
        #print(self.grid[0][3])
        self.v_top = [-1,-1, True, 1000]
        self.v_bottom = [-2,-2,True,1000]


    def root_value(self, k):
        if(k < -2 or k > self.grid_size -1):
            print("{} --> element index out of bound root".format(k))
            return
        # -1 and -2 for v_top and v_bottom

        if (k == -1):
            return self.v_top[0]
        if (k == -2):
            return self.v_bottom[0]

        while(k != self.grid[k][0]):
            k = self.grid[k][0]

        return k

    def get_adjacent_open_elements(self,a):

        list = []
        if(a < 0 or a > self.grid_size -1):
            print("{} --> element index out of bound get_adjacent_open_elements".format(a))
            return

        border_condition = False
        #topmost row
        if (a >=0 and a < self.N):
            list.append(self.v_top)
            border_condition = True

        #bottom most row
        if (a >= (self.N -1)*self.N and a < self.grid_size):
            list.append(self.v_bottom)
            border_condition = True

        #leftmost column
        if (a % self.N == 0):
            if(self.grid[a+1][2] is True):
                list.append(self.grid[a+1])
                border_condition = True

        #rightmost column
        if((a+1) % self.N == 0):
            if(self.grid[a-1][2] is True):
                list.append(self.grid[a-1])
                border_condition = True

        #for in between elements
        if (border_condition is True):
            return list
        else:
            if(self.grid[a+1][2] is True):
                list.append(self.grid[a+1])

            if(self.grid[a-1][2] is True):
                list.append(self.grid[a-1])

            if(self.grid[a-self.N][2] is True):
                list.append(self.append[a-self.N])

            if(self.grid[a+self.N][2] is True):
                list.append(self.append[a+self.N])

            return list


#implement weighted_quick_union
    def union(self, a, b):

        if(a < 0 or a > self.grid_size -1):
            print("{} -> this element index out of bound union a".format(a))
            return
        if(b < -2 or b > self.grid_size -1):
            print("{} -> this element index out of bound union b".format(b))
            return

        # element a is always given by us so it can't be v_top and v_bottom
        # -1 and -2 because of v_top and v_bottom
        #union function will only be called for open element due to code design
        #hence no need to put an edge case checking if both a and b elements are open

        root_a = self.root_value(a)
        root_b = self.root_value(b)

        if(root_a == root_b):
            return

        elif(b == -1):
            self.grid[a][0] = root_b
            self.v_top[3] = self.v_top[3] + self.grid[a][3]
        elif(b == -2):
            self.grid[a][0] = root_b
            self.v_bottom[3] = self.v_bottom[3] + self.grid[a][3]

        elif(self.grid[a][3] >= self.grid[b][3]):
            self.grid[b][0] = root_a
            #increment the weight
            self.grid[a][3] = self.grid[a][3] + self.grid[b][3]
            return
        else:
            self.grid[a][0] = root_b
            self.grid[b][3] = self.grid[b][3] + self.grid[a][3]
            return

        return


    def open(self, a):

        if(a < 0 or a > self.grid_size -1):
            print("{} -> this element index out of bound open function".format(a))
            return

        open_elements = self.get_adjacent_open_elements(a)
        print(open_elements)
        for i in range(len(open_elements)):
            self.union(a, open_elements[i][1])


    def isPercolating(self):
        if(self.v_top[0] == self.v_bottom[0]):
            print("yes")
            return True
        else:
            print("no")
            return False




system_1 = percolation(2)


system_1.open(0)
system_1.open(2)
system_1.isPercolating()
