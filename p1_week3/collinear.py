with open('input6.txt') as f:
    next(f)
    cord = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            cord.append(line)

#print(cord[0])
#print(cord[1])
#print(cord)


def slope(list, a, b):

    slope = 0
    #vertical line
    if((list[a][0] == list[b][0]) and (list[a][1] != list[b][1])):
        slope = float("inf")
        
    elif((list[a][0] == list[b][0]) and (list[a][1] == list[b][1])):
        slope = float("-inf")
    else:
        slope = (list[b][1] - list[a][1])/(list[b][0] - list[a][0])

    return slope

def compareTo(list, a, b):
    #return less if a < b
    #compare points by their y-coordinates, breaking ties by their x-coordinates

    if(list[a][1] < list[b][1]):
        return -1   #less
    elif(list[a][1] == list[b][1]):
        if(list[a][0] < list[b][0]):
            return -1  #less
    else:
        return None


def slopeOrder(list, a, b, c):
    #return less if slope of b is less than c taking a as refernce point

    if(slope(list, a, b) < slopeTo(list, a, c)):
        return 'less'
    if(slope(list, a, b) == slopeTo(list, a, c)):
        return 'equal'



def BruteCollinearPoint(list):
    #examines 4 points at a time and checks whether they all lie on the same line segment, returning all such line segments
    #check whether the three slopes between p and q, between p and r, and between p and s are all equal. --> O(n^4)
    for i in range(0,len(list)):
        for j in range(i+1, len(list)):
            for k in range(j+1, len(list)):
                for l in range(k+1, len(list)):
                    if ((slope(list , i ,j) == slope(list, i, k)) and (slope(list , i ,j) == slope(list, i, l))):
                        print("collinear points are ")
                        print(list[i] , list[j] ,list[k] , list[l])
    return

#BruteCollinearPoint(cord)

def FastCollinearPoint(list):
    row = len(list)
    #print(row)
    slope_array = [[0 for x in range(2)] for y in range(row)]
    #print(len(slope_array))
    for k in range(len(list)):
    
        for i in range(len(list)):
            
            slope_array[i][0] = slope(list, k ,i)
            
            slope_array[i][1] = i
        
        #use any STABLE sort; python's sort function , by default , is stable
        slope_array.sort()
        # print(slope_array)
        # print(slope_array[0][0])
        for i in range(0, (len(slope_array)-2) ):
        
            if( (slope_array[i][0] == slope_array[i+1][0]) and (slope_array[i][0] == slope_array[i+2][0])):
                
                print(cord[k],cord[slope_array[i][1]],cord[slope_array[i+1][1]],cord[slope_array[i+2][1]])

    
FastCollinearPoint(cord)