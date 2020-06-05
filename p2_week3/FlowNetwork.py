#For reference -> https://algs4.cs.princeton.edu/64maxflow/FlowNetwork.java.html

from FlowEdge import FlowEdge
import random

# Implemented 3 types of constructors -> use as per requirement

class FlowNetwork:

    def __init__(self,*args):
        if(len(args) == 1 and isinstance(args[0], int)):
            # /** Case 1
            #  * Initializes an empty flow network with {@code V} vertices and 0 edges.
            #  * @param V the number of vertices
            #  * @throws ValueError if {@code V < 0}
            #  */
            if(args[0] < 0):
                raise ValueError("Number of vertices must be non-negative")

            self.V = args[0]  #total number of vertices (network starts from 0th vertex to (V-1)th vertex)
            self.E = 0  #total number of edges
            self.adj = [] #adjacent edges

            for v in range(self.V):
                self.adj.append([])

        elif(len(args) == 2):
            # /** Case 2
            #  * Initializes a random flow network with {@code V} vertices and <em>E</em> edges.
            #  * The capacities are integers between 0 and 99 and the flow values are zero.
            #  * @param V the number of vertices
            #  * @param E the number of edges
            #  * @throws ValueError if {@code V < 0}
            #  * @throws ValueError if {@code E < 0}
            #  */
            if(args[0] < 0):
                raise ValueError("Number of vertices must be non-negative")
            if(args[1] < 0):
                raise ValueError("Number of edges must be non-negative")

            self.V = args[0]  #total number of vertices (network starts from 0th vertex to (V-1)th vertex)
            self.E = args[1] #total number of edges
            self.adj = [] #adjacent edges

            for v in range(self.V):
                self.adj.append([])

            for i in range(self.E):
                v1 = random.randint(0,self.V-1)
                v2 = random.randint(0,self.V-1)
                capacity = random.uniform(0,100)
                self.addEdge(FlowEdge(v1,v2,capacity))

        elif(len(args) == 1 and isinstance(args[0], list)):
            # /** Case 3
            #  * Initializes a flow network from an input stream. Input stream is passed as list
            #  * The format is the number of vertices <em>V</em>,
            #  * followed by the number of edges <em>E</em>,
            #  * followed by <em>E</em> pairs of vertices and edge capacities,
            #  * with each entry separated by whitespace.
            #  * @param in the input stream
            #  * @throws ValueError if the endpoints of any edge are not in prescribed range
            #  * @throws ValueError if the number of vertices or edges is negative
            #  */
            if(args[0][0] < 0):
                raise ValueError("Number of vertices must be non-negative")
            if(args[0][1] < 0):
                raise ValueError("Number of edges must be non-negative")

            self.V = args[0][0]  #total number of vertices (network starts from 0th vertex to (V-1)th vertex)
            self.E = args[0][1] #total number of edges
            self.adj = [] #adjacent edges
            for v in range(self.V):
                self.adj.append([])

            for i in range(2,self.E + 2):
                v1 = args[0][i][0]
                v2 = args[0][i][1]
                capacity = args[0][i][2]
                self.addEdge(FlowEdge(v1,v2,capacity))

        else:
            raise AttributeError("invalid attributes passed")


    def validateVertex(self,vertex):
        if(vertex < 0 or vertex >= self.V):
            raise ValueError("vertex {} is not between 0 and {}".format(vertex, self.V-1))

    def addEdge(self, edge):
        v1 = edge.edge_from()
        v2 = edge.edge_to()

        self.validateVertex(v1)
        self.validateVertex(v2)

        self.adj[v1].append(edge)
        self.adj[v2].append(edge)
        self.E += 1

    def NumberOfVertices(self):
        return self.V

    def NumberOfEdges(self):
        return self.E


    #Return edges to and from vertex V
    def edges_from_vertex(self,vertex):
        self.validateVertex(vertex)
        return self.adj[vertex]

    #Return list of all edges excluding self loops
    def all_edges(self):
        edge_list = []
        for v in range(self.V):
            for edge in self.adj[v]:
                if(edge.edge_to() != v):
                    edge_list.append(edge)

        return edge_list


    def toString(self):
        arr = []
        arr.append("{}  {}".format(self.V, self.E))
        for v in range(self.V):
            temp_str = str(v) + ": "
            for edge in self.adj[v]:
                if(edge.edge_to() != v):
                    temp_str += str(edge.toString()) + " "
            arr.append(temp_str)

        return arr


'''
Unit testing code below
'''

# abc = FlowNetwork(5,5)
# #abc.validateVertex(4)
# #
# # print(abc.NumberOfVertices())
# # print(abc.edges_from_vertex(0)[1].toString())
#
# #print(abc.all_edges()[1].toString())
#
# for i in abc.toString():
#     print(i)

# abc = FlowNetwork(5)
# edge = FlowEdge(1,2,3.4)
# abc.addEdge(edge)
#print(abc.edges_from_vertex(1)[0].toString())
#print(abc.all_edges()[0].toString())
# edge1= FlowEdge(0,3,2.1)
# abc.addEdge(edge1)
#print(abc.edges_from_vertex(0)[0].toString())
# for i in abc.toString():
#     print(i)
#abc.validateVertex(4)
#
#print(abc.NumberOfVertices())
#print(abc.edges_from_vertex(0)[1].toString())

#print(abc.all_edges()[1].toString())

#for i in abc.toString():
#    print(i)

# abc = FlowNetwork([5,2,[0,1,2.1],[2,3,2.1]])
# abc.validateVertex(4)
# print(abc.edges_from_vertex(0)[0].toString())
# print(abc.all_edges()[1].toString())
# for i in abc.toString():
#     print(i)
