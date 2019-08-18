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
        # initially tree size of all elements is 1
        self.grid = [[i,i, False, 1] for i in range(self.grid_size)]
        #print(self.grid[0][3])
        self.v_top = [-1,-1, True, 1]
        self.v_bottom = [-2,-2,True,1]


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
            if (k == -1):
                return self.v_top[0]
            if (k == -2):
                return self.v_bottom[0]


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
            if(self.grid[a+self.N][2] is True):
                list.append(self.grid[a+self.N])
            if(a != self.N and self.grid[a+1][2] is True):
                list.append(self.grid[a+1])
            if(a != 0 and self.grid[a-1][2] is True):
                list.append(self.grid[a-1])
            border_condition = True

        #bottom most row
        if (a >= (self.N -1)*self.N and a < self.grid_size):
            list.append(self.v_bottom)
            if(self.grid[a-self.N][2] is True):
                list.append(self.grid[a-self.N])
            if(a != self.grid_size -1 and self.grid[a+1][2] is True):
                list.append(self.grid[a+1])
            if(a != (self.N -1)*self.N and self.grid[a-1][2] is True):
                list.append(self.grid[a-1])
            border_condition = True

        #leftmost column
        if (a % self.N == 0 and a != 0 and a != (self.N -1)*self.N):
            #print(a)
            if(self.grid[a+1][2] is True):
                list.append(self.grid[a+1])
            if(self.grid[a+self.N][2] is True):
                list.append(self.grid[a+self.N])
            if(self.grid[a-self.N][2] is True):
                list.append(self.grid[a-self.N])
            #print(list)
            border_condition = True

        #rightmost column
        if((a+1) % self.N == 0 and a != self.N and a != self.grid_size -1):
            if(self.grid[a-1][2] is True):
                list.append(self.grid[a-1])
            if(self.grid[a+self.N][2] is True):
                list.append(self.grid[a+self.N])
            if(self.grid[a-self.N][2] is True):
                list.append(self.grid[a-self.N])
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
        elif(root_a < 0 and root_b < 0):
            #one of the element points to v_top and other points to v_bottom
            print("system percolates now")
            if(root_a == -2):
                #connect a and v_bottom to v_top
                self.v_bottom[0] = self.v_top[0]
                self.grid[a][0] = self.v_top[0]
                self.v_top[3] = self.v_top[3] + self.grid[a][3]
            else:
                self.v_top[0] = self.v_bottom[0]
                self.grid[a][0] = self.v_bottom[0]
                self.v_bottom[3] = self.v_bottom[3] + self.grid[a][3]
        elif(root_b == -1):
            if(self.v_top[3] >= self.grid[a][3]):
                self.grid[a][0] = root_b
                #increment the weight
                self.v_top[3] = self.v_top[3] + self.grid[a][3]
            else:
                self.v_top[0] = root_a
                self.grid[a][3] = self.grid[a][3] + self.v_top[3]

        elif(root_b == -2):
            if(self.v_bottom[3] >= self.grid[a][3]):
                self.grid[a][0] = root_b
                #increment the weight
                self.v_bottom[3] = self.v_bottom[3] + self.grid[a][3]
            else:
                self.v_bottom[0] = root_a
                self.grid[a][3] = self.grid[a][3] + self.v_bottom[3]

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

        self.grid[a][2] = True
        open_elements = self.get_adjacent_open_elements(a)
        for i in range(len(open_elements)):
            self.union(a, open_elements[i][1])

        #print(self.grid)
        #print(self.v_top)
        #print(self.v_bottom)


    def isPercolating(self):
        # print(self.grid)
        # print(self.v_top)
        # print(self.v_bottom)
        if(self.v_top[0] == self.v_bottom[0]):
            print("yes")
            return True
        else:
            print("no")
            return False




system_1 = percolation(3)


system_1.open(0)
system_1.open(3)
system_1.open(6)
system_1.isPercolating()
