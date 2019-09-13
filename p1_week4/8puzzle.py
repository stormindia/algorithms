#Conditions for unsolvability -->
#https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/

#used same heuristic function as given in assignment

class Puzzle:

    goal_state =  [[0,1,2],[3,4,5],[6,7,8]]
    #correct postions
    #               1 2 3   4 5 6   7 8 0
    #    X          0 0 0   1 1 1   2 2 2
    #    Y          0 1 2   0 1 2   0 1 2
    #to make calculation of manhattan_value easy, save the goal_state values with their coordinates as well
    #goal_state = [[[1,0,0],[2,0,1],[3,0,2]],[[4,1,0],[5,1,1],[6,1,2]],[[7,2,0],[8,2,1],[0,2,2]]]

    def __init__(self, board=None):
        self.board = board


    #check if it is solvable
    #for simplicity using an extra array to store all the values in 1D
    #requires improvement
    def isSolvable(self):
        self.one_d_array = []

        for i in range(0,len(self.board)):
            for j in range(0,len(self.board)):
                self.one_d_array.append(self.board[i][j])

        inv_count = 0
        for i in range(0,len(self.one_d_array)-1):
            for j in range(i+1, len(self.one_d_array)):
                if (self.one_d_array[i] != 0 and self.one_d_array[j] != 0 and self.one_d_array[i] > self.one_d_array[j]):
                    inv_count = inv_count + 1

        if(inv_count % 2 == 0):
            print("board is solvable")
            return True
        else:
            print("board is not solvable")
            return False



    def manhattan_value(self):
        manhattan_distance = 0
        for i in range(0,len(self.board)):
            for j in range(0,len(self.board)):
                if(self.board[i][j] != self.goal_state[i][j]):

                    #correct position of the element
                    x_goal , y_goal = divmod(self.board[i][j],3)
                    manhattan_distance = manhattan_distance + abs(i-x_goal) + abs(j-y_goal)

        return manhattan_distance


    def hamming_value(self):
        hamming_value = 0
        for i in range(0,len(self.board)):
            for j in range(0,len(self.board)):
                if(self.board[i][j] != self.goal_state[i][j]):
                    hamming_value = hamming_value + 1

        return hamming_value


    def get_neighbours(self,data=None):

        tmp_state = data
        get_neighbours_list = []
        border_condition = False

        #find the position of blank space
        x_blank = 0
        y_blank = 0
        for i in range(0,len(data)):
            for j in range(0,len(data)):
                if(data[i][j] != 0):
                    pass
                else:
                    x_blank = i
                    y_blank = j
                    break

        #topmost row
        if(x_blank == 0):
            tmp_state[x_blank][y_blank] , tmp_state[x_blank + 1][y_blank] = tmp_state[x_blank + 1][y_blank] , tmp_state[x_blank][y_blank]
            get_neighbours_list.append(tmp_state)
            border_condition = True

        #bottom most row
        tmp_state = data
        if(x_blank == 2):
            tmp_state[x_blank][y_blank] , tmp_state[x_blank - 1][y_blank] = tmp_state[x_blank - 1][y_blank] , tmp_state[x_blank][y_blank]
            get_neighbours_list.append(tmp_state)
            border_condition = True

        #left most row
        tmp_state = data
        if(y_blank == 0):
            tmp_state[x_blank][y_blank] , tmp_state[x_blank][y_blank + 1] = tmp_state[x_blank][y_blank + 1] , tmp_state[x_blank][y_blank]
            get_neighbours_list.append(tmp_state)
            border_condition = True

        #right most row
        tmp_state = data
        if(y_blank == 2):
            tmp_state[x_blank][y_blank] , tmp_state[x_blank][y_blank - 1] = tmp_state[x_blank][y_blank - 1] , tmp_state[x_blank][y_blank]
            get_neighbours_list.append(tmp_state)
            border_condition = True

        #in between element
        if(border_condition == True):
            return get_neighbours_list
        else:
            border_condition = False
            tmp_state = data
            # 4 possible neighbours in this case

            # first - upper element
            tmp_state[x_blank][y_blank] , tmp_state[x_blank - 1][y_blank] = tmp_state[x_blank - 1][y_blank] , tmp_state[x_blank][y_blank]
            get_neighbours_list.append(tmp_state)

            #second - lower element
            tmp_state = data      #we can simply revert the above change again by reswapping the values
            tmp_state[x_blank][y_blank] , tmp_state[x_blank + 1][y_blank] = tmp_state[x_blank + 1][y_blank] , tmp_state[x_blank][y_blank]
            get_neighbours_list.append(tmp_state)

            #third - element to right
            tmp_state = data      #we can simply revert the above change again by reswapping the values
            tmp_state[x_blank][y_blank], tmp_state[x_blank][y_blank + 1] = tmp_state[x_blank][y_blank + 1], tmp_state[x_blank][y_blank]
            get_neighbours_list.append(tmp_state)

            #fourth - element to left
            tmp_state = data      #we can simply revert the above change again by reswapping the values
            tmp_state[x_blank][y_blank], tmp_state[x_blank][y_blank - 1] = tmp_state[x_blank][y_blank - 1], tmp_state[x_blank][y_blank]
            get_neighbours_list.append(tmp_state)
            return get_neighbours_list


    #implement A* algorithm
    def solver(self):
        moves = 0

        curr_state = self.board

        if(curr_state == self.goal_state):
            print("goal state reached!")
            print(curr_state)
            print("number of moves required to reach goal state --> {}".format(moves))

        else:
            print(self.get_neighbours(curr_state))
            #print()
            return






#board1 = [[1,2,3],[4,5,6],[8,7,0]]
#board1 = [[8,1,2],[0,4,3],[7,6,5]]
#b1 = Puzzle(board1)
#b1.isSolvable()

board2 = [[1,0,2],[3,4,5],[6,7,8]]
b2 = Puzzle(board2)
#b2.isSolvable()
b2.solver()
