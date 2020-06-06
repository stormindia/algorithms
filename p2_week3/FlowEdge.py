# For reference -> https://algs4.cs.princeton.edu/64maxflow/FlowEdge.java.html

class FlowEdge:
    FLOATING_POINT_EPSILON = 1e-10
    def __init__(self,*args):
        # Allow user to initalize edge in 2 ways
        # with v1, v2, capacity
        # or with v1, v2, capacity and flow
        if(len(args) > 4):
            raise ValueError("invalid number of attributes passed")

        if(args[0] < 0):
            raise ValueError("vertex can't be negative")
        else:
            self.v1 = args[0]

        if(args[1] < 0):
            raise ValueError("vertex can't be negative")
        else:
            self.v2 = args[1]

        if(args[2] < 0):
            raise ValueError("capacity can't be negative")
        else:
            self.capacity = args[2]

        if(len(args) == 4):
            if(args[3] > self.capacity):
                raise ValueError("flow can't be greater than capacity")
            elif(args[3] < 0):
                raise ValueError("flow can't be negative")
            else:
                self.flow = args[3]
        else:
            self.flow = 0


    def edge_from(self):
        return self.v1

    def edge_to(self):
        return self.v2


    def capacity(self):
        return self.capacity

    def flow_of_edge(self):
        return self.flow


    def other(self,vertex):
        if(vertex == self.v1):
            return self.v2
        elif(vertex == self.v2):
            return self.v1
        else:
            raise ValueError("invalid endpoint")

    #Returns the residual capacity of the edge in the direction
    def residualCapacityTo(self,vertex):
        if(vertex == self.v1): #backword edge
            return self.flow
        elif(vertex == self.v2):    #forward edge
            return self.capacity - self.flow
        else:
            raise ValueError("invalid endpoint")


     # * Increases the flow on the edge in the direction to the given vertex.
     # *   If {@code vertex} is the tail vertex, this increases the flow on the edge by {@code delta};
     # *   if {@code vertex} is the head vertex, this decreases the flow on the edge by {@code delta}.
    def addResidualFlowTo(self,vertex,delta):
        if(delta < 0):
            raise ValueError("delta can't be negative")

        if(vertex == self.v1):
            self.flow = self.flow - delta
        elif(vertex == self.v2):
            self.flow = self.flow + delta
        else:
            raise ValueError("invalid endpoint")

        #round flow to 0 or capacity if within floating-point precision
        if(abs(self.flow) < FLOATING_POINT_EPSILON):
            self.flow = 0
        if(abs(self.flow - self.capacity) <= FLOATING_POINT_EPSILON):
            self.flow = self.capacity

        if(self.flow < 0):
            raise ValueError("flow is negative")
        if(self.flow > self.capacity):
            raise ValueError("flow is greater than capacity")

    def toString(self):
        #print("edge from {} -> {} has flow/capacity as {} / {}".format(self.v1, self.v2, self.flow, self.capacity))
        return "{} -> {} {} / {} ".format(self.v1,self.v2,self.flow,self.capacity)


# To test
# edge1 = FlowEdge(1,2,2.3,2.1)
# edge1.toString()
# print(edge1.residualCapacityTo(2))
# print(edge1.addResidualFlowTo(2,0.1))
# edge1.toString()
