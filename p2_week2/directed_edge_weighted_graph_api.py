class DirectedEdge:

    def __init__(self,v1,v2,weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def edge_from(self):
        return self.v1

    def edge_to(self):
        return self.v2

    def weight(self):
        return self.weight


#Allow self loop and parallel edges
class EdgeWeightedDigraph:
# e --> represents an Edge
    def __init__(self, V):
        self.V = V
        self.adj = []*V    #contains edges instead of vertices
        self.edges = []

        for i in range(V):
            self.adj[i] = []


    #add an edge between v-w
    def add_edge(self,e):
        # e --> represents an Edge
        #parallel edges allowed
        v = e.edge_from()
        self.adj[v].append(e)
        self.edges.append(e)

    #returns the adjacent edges
    def adjacent_edges(self,v):
        return self.adj[v]

    #returns all the edges
    def edges(self):
        return self.edges


#Refer https://www.coursera.org/learn/algorithms-part2/lecture/igCiL/shortest-path-properties
#Part2 week2 shortest path properties
#Shortest path tree APIS
class SPT_apis:
    def __init__(self, G, source_vertex):
        self.V = G.V
        self.s = source_vertex
        self.distTo = []*self.V
        self.edgeTo = []*self.V #REFER README


    def distTo(self,v):
        return self.distTo[v]

    def pathTo(self,v):
        path = []

        while(e != NULL):
            k = edgeTo[v]
            e = edgeTo[k.edge_from()]
            path.append(e)

        return path

    def relax(self,e):
        v1 = e.edge_from()
        v2 = e.edge_to()

        if(self.distTo[w] > self.distTo[v] + e.weight()):
            self.distTo[w] = self.distTo[v] + e.weight()
            self.edgeTo[w] = e

        return
