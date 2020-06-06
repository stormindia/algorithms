# reference -> https://algs4.cs.princeton.edu/64maxflow/FordFulkerson.java.html

# /**
#      * Compute a maximum flow and minimum cut in the network {@code G}
#      * from vertex {@code s} to vertex {@code t}.
#      *  The {@code FordFulkerson} class represents a data type for computing a
#      *  <em>maximum st-flow</em> and <em>minimum st-cut</em> in a flow
#      *  network.
#      *  <p>
#      *  This implementation uses the <em>Ford-Fulkerson</em> algorithm with
#      *  the <em>shortest augmenting path</em> heuristic.
# */


from FlowEdge import FlowEdge
from FlowNetwork import FlowNetwork
from queue import Queue

FLOATING_POINT_EPSILON = 1e-11


class FordFulkerson:

    def __init__(self, flowNetwork, s,t):
        self.V = flowNetwork.NumberOfVertices() #number of vertices
        self.s = s # source vertex
        self.t = t # sink vertex

        self.validate(self.s)
        self.validate(self.t)
        if(self.s == self.t):
            raise ValueError("source equals sink")

        self.marked = [False]
        for i in range(1,self.V):
            self.marked.append(False) #marked[v] = true iff s->v path in residual graph
        self.edgeTo = [None]
        for i in range(1,self.V):
            self.edgeTo.append(None)  #edgeTo[v] = last edge on shortest residual s->v path

        self.value = 0 #current value of max flow

        if(self.isFeasible(flowNetwork, self.s, self.t) == False):
            raise ValueError("initial flow is infeasible")


        value = self.excess(flowNetwork, self.t)
        while(self.hasAugmentingPath(flowNetwork, self.s, self.t) is True):

            #Compute bottleneck capacity
            bottle = 999999
            vertex = t
            while(vertex != s):
                bottle = min(bottle, self.edgeTo[vertex].residualCapacityTo(vertex))
                vertex = self.edgeTo[vertex].other(vertex)

            # augment flow
            while(vertex != s):
                self.edgeTo[vertex].addResidualFlowTo(vertex,bottle)
                vertex = self.edgeTo[vertex].other(vertex)

            value += bottle;

        # check optimality conditions
        assert self.check(flowNetwork, s, t);


    def return_max_flow(self):
        return self.value

    # Returns true if the specified vertex is on the {@code s} side of the mincut.
    def inCut(self,vertex):
        self.validate(vertex)
        return self.marked[vertex]


    def validate(self,vertex):
        if(vertex < 0 or vertex > self.V - 1):
            raise ValueError("vertex {} is not between 0 and {}".format(vertex, self.V -1))


    #is there an augmenting path?
    #if so, upon termination edgeTo[] will contain a parent-link representation of such a path
    #this implementation finds a shortest augmenting path (fewest number of edges),
    #which performs well both in theory and in practice

    def hasAugmentingPath(self, flowNetwork, s, t):
        #edgeTo = []*flowNetwork.NumberOfVertices()
        #marked = [False]*flowNetwork.NumberOfVertices()

        #BFS
        temp_q = Queue()
        temp_q.put(s)
        self.marked[s] = True

        while(temp_q.empty() is False and self.marked[t] is False):
            vertex = temp_q.get()

            for edge in flowNetwork.adj[vertex]:
                vertex2 = edge.other(vertex)

                # if residual capacity from v to w
                if(edge.residualCapacityTo(vertex2) > 0):
                    if(self.marked[vertex2] is False):
                        self.edgeTo[vertex2] = edge
                        self.marked[vertex2] = True
                        temp_q.put(vertex2)

        # is there an augmenting path?
        return self.marked[t]

    # return excess flow at vertex
    def excess(self, flowNetwork, vertex):
        excess_flow = 0.0
        for edge in flowNetwork.adj[vertex]:
            if(vertex == edge.edge_from()):
                excess_flow = excess_flow - edge.flow_of_edge()
            else:
                excess_flow = excess_flow + edge.flow_of_edge()

        return excess_flow

    def isFeasible(self,flowNetwork, s, t):

        #check that capacity constraints are satisfied
        for v in range(flowNetwork.NumberOfVertices()):
            for edge in flowNetwork.adj[v]:

                if(edge.flow_of_edge() < - FLOATING_POINT_EPSILON or edge.flow_of_edge() > edge.capacity + FLOATING_POINT_EPSILON):
                    print("Edge does not satisfy capacity constraints: {}".format(edge.toString()))
                    return False

        #check that net flow into a vertex equals zero, except at source and sink
        if((abs(self.value + self.excess(flowNetwork, s))) > FLOATING_POINT_EPSILON):
            print("excess at source: {}".format(self.excess(flowNetwork, s)))
            print("max flow: {}".format(self.value))
            return False

        if((abs(self.value + self.excess(flowNetwork, t))) > FLOATING_POINT_EPSILON):
            print("excess at sink: {}".format(self.excess(flowNetwork, t)))
            print("max flow: {}".format(self.value))
            return False

        for v in range(flowNetwork.NumberOfVertices()):
            if(v == s or v == t):
                pass
            else:
                if(abs(self.excess(flowNetwork, v)) > FLOATING_POINT_EPSILON):
                    print("net flow out of vertex {} is not zero".format(v))
                    return False
                else:
                    pass

        return True


    #check optimality conditions
    def check(self, flowNetwork, s, t):

        #check that flow is feasible
        if(self.isFeasible(flowNetwork, s, t) is False):
            print("Flow is infeasible")
            return False

        #check that s is on the source side of min cut and that t is not on source side
        if(self.inCut(s) is False):
            print("source {} is not on the source side of the min-cut".format(s))
            return False

        if(self.inCut(t) is True):
            print("sink {} is on the source side of the min-cut".format(t))
            return False


        #check that value of min cut = value of max flow
        mincutValue = 0.0
        for v in range(flowNetwork.NumberOfVertices()):
            for edge in flowNetwork.adj[v]:
                if( (v == edge.edge_from()) and self.inCut(edge.edge_from()) is True and self.inCut(edge.edge_to()) is False):
                    mincutValue += edge.capacity

        if(abs(mincutValue - self.value) > FLOATING_POINT_EPSILON):
            print("Max flow value is {} and min-cut value is {}".format(self.value, mincutValue))
            return False

        return True




'''
Unit testing
'''
# flowNetwork = FlowNetwork(100,100)
# s = 0
# t = 99
# abc = FordFulkerson(flowNetwork, s, t)
# print(abc.return_max_flow())
# print(abc.isFeasible(flowNetwork,0,4))
# print(abc.excess(flowNetwork,3))
# print(abc.inCut(1))
