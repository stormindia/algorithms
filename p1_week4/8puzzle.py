#Conditions for unsolvability -->
#https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/

#used same heuristic function as given in assignment
#only get_neighbours function requires minor modification for N-puzzle solutions

import copy

class Puzzle:

    goal_state =  [[0,1,2],[3,4,5],[6,7,8]]
    #correct postions
    #               1 2 3   4 5 6   7 8 0
    #    X          0 0 0   1 1 1   2 2 2
    #    Y          0 1 2   0 1 2   0 1 2


    def __init__(self, board=None):
        self.board = board


    #currently has bugs -- require fixing
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



    def manhattan_value(self,data=None):
        manhattan_distance = 0
        for i in range(0,len(data)):
            for j in range(0,len(data)):
                if(data[i][j] != self.goal_state[i][j] and data[i][j] != 0):
                    #correct position of the element
                    x_goal , y_goal = divmod(data[i][j],3)
                    manhattan_distance = manhattan_distance + abs(i-x_goal) + abs(j-y_goal)

        return manhattan_distance


    def hamming_value(self,data=None):
        hamming_value = 0
        for i in range(0,len(data)):
            for j in range(0,len(data)):
                if(data[i][j] != self.goal_state[i][j]):
                    hamming_value = hamming_value + 1

        return hamming_value


    #swaps values then save the resultant state in an array and then reswaps them to return to original position for further swapping
    def append_in_list(self,a,b,c,d,data=None):

        result_state = []

        #swap the values
        data[a][b] , data[c][d] = data[c][d] , data[a][b]

        for i in range(0,len(data)):
            result_state.append(data[i][:])

        #reswap them to their original position
        data[a][b] , data[c][d] = data[c][d] , data[a][b]

        #print(result_state)
        return result_state

    def get_neighbours(self,data=None):

        #tmp_state = data
        result = []
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

        #print(x_blank, y_blank)

        #topmost row
        if(x_blank == 0):
            result = self.append_in_list(x_blank,y_blank,x_blank+1,y_blank,data)
            get_neighbours_list.append(result)

            if(y_blank != 0):
                result = self.append_in_list(x_blank,y_blank,x_blank,y_blank-1,data)
                get_neighbours_list.append(result)
            if(y_blank != 2):
                result = self.append_in_list(x_blank,y_blank,x_blank,y_blank+1,data)
                get_neighbours_list.append(result)
            border_condition = True


        #bottom most row
        if(x_blank == 2):
            result = self.append_in_list(x_blank,y_blank,x_blank-1,y_blank,data)
            get_neighbours_list.append(result)

            if(y_blank != 0):
                result = self.append_in_list(x_blank,y_blank,x_blank,y_blank-1,data)
                get_neighbours_list.append(result)

            if(y_blank != 2):
                result = self.append_in_list(x_blank,y_blank,x_blank,y_blank+1,data)
                get_neighbours_list.append(result)

            border_condition = True

        #left most row
        if(y_blank == 0):

            if(x_blank == 1):
                result = self.append_in_list(x_blank,y_blank,x_blank-1,y_blank,data)
                get_neighbours_list.append(result)

                result = self.append_in_list(x_blank,y_blank,x_blank+1,y_blank,data)
                get_neighbours_list.append(result)

                result = self.append_in_list(x_blank,y_blank,x_blank,y_blank+1,data)
                get_neighbours_list.append(result)

            border_condition = True

        #right most row
        if(y_blank == 2):

            if(x_blank == 1):
                result =  self.append_in_list(x_blank,y_blank,x_blank-1,y_blank,data)
                get_neighbours_list.append(result)

                result = self.append_in_list(x_blank,y_blank,x_blank+1,y_blank,data)
                get_neighbours_list.append(result)

                result = self.append_in_list(x_blank,y_blank,x_blank,y_blank-1,data)
                get_neighbours_list.append(result)

            border_condition = True

        #in between element
        if(border_condition == True):
            return get_neighbours_list
        else:
            border_condition = False
            # 4 possible neighbours in this case

            # first - upper element
            result = self.append_in_list(x_blank,y_blank,x_blank-1,y_blank,data)
            get_neighbours_list.append(result)

            #second - lower element
            result = self.append_in_list(x_blank,y_blank,x_blank+1,y_blank,data)
            get_neighbours_list.append(result)

            #third - element to right
            result = self.append_in_list(x_blank,y_blank,x_blank,y_blank+1,data)
            get_neighbours_list.append(result)

            #fourth - element to left
            result = self.append_in_list(x_blank,y_blank,x_blank,y_blank-1,data)
            get_neighbours_list.append(result)
            return get_neighbours_list


    #implement A* algorithm
    def solver(self):
        moves = 0
        heuristic_value = []
        prev_state = []
        curr_state = self.board
        output = []


        if(curr_state == self.goal_state):
            print("goal state reached!")
            print(curr_state)
            print("number of moves required to reach goal state --> {}".format(moves))

        else:
            while(True):
                min_heuristic_value = 99999999999
                min_pos = None
                moves = moves + 1
                output = self.get_neighbours(curr_state)
                #print(output)
                for i in range(len(output)):
                    if(output[i] != prev_state):
                        h = self.manhattan_value(output[i])
                        if(h < min_heuristic_value):
                            min_heuristic_value = h
                            min_pos = i
                        elif(h == min_heuristic_value):
                            #calculate hamming_value for i and min_pos to break tie
                            hamming_value_i = self.hamming_value(output[i])
                            hamming_value_min_pos = self.hamming_value(output[min_pos])
                            if(hamming_value_i < hamming_value_min_pos):
                                min_heuristic_value = h
                                min_pos = i
                            else:
                                pass
                        else:
                            pass

                if(min_heuristic_value == 0):
                    print("goal state reached!")
                    print(output[min_heuristic_value])
                    print("minimum number of moves required to reach goal state --> {}".format(moves))
                    break
                else:
                    prev_state = copy.deepcopy(curr_state)
                    curr_state = copy.deepcopy(output[min_pos])
                    #print(curr_state)
                    #if(moves > 2):
                    #    break

            return





#board1 = [[1,2,3],[4,5,6],[8,7,0]]
#board1 = [[8,1,2],[0,4,3],[7,6,5]]
#b1 = Puzzle(board1)
#b1.isSolvable()

# board2 = [[1,0,2],[3,4,5],[6,7,8]]
# b2 = Puzzle(board2)
# if(b2.isSolvable()):
#     b2.solver()

# board3 = [[3,1,2],[0,4,5],[6,7,8]]
# b3 = Puzzle(board3)
# if(b3.isSolvable()):
#     b3.solver()

board4 = [[3,1,2],[6,4,5],[7,0,8]]
b4 = Puzzle(board4)
if(b4.isSolvable()):
    b4.solver()
