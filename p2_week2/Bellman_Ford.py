#Original Bellman Ford --> solves the single source shortest-paths problem from a given source s for any edge-weighted digraph with V vertices and no negative cycles reachable from s


# A negative cycle is a directed cycle whose sum of edge weights is negative

# This is a queue based approach for Bellman Ford algo where the only edges that could lead to a change in distTo[] are those leaving a vertex whose distTo[] value
# changed in the previous pass.


from directed_edge_weighted_graph_api import *
from edge_weighted_graph_api import EdgeWeightedGraph

MAX = 99999

G = EdgeWeightedDigraph(V)


#there could be a negative cycle, but it must be unreachble from source_vertex
class BellmanFord:

    def __init__(self,G,source_vertex):
        self.G = G
        self.S = source_vertex
        self.distTo = [MAX]*self.G.V
        self.edgeTo = []*self.G.V

        self.onQ = [False]*self.G.V      #is the vertex on queue
        self.queue = []*self.G.V    #vertices being relaxed

        self.distTo[self.S] = 0

        self.queue.append(self.S)
        self.onQ[self.S] = True

        while(len(self.queue) > 0 and self.hasNegativeWeightCycle() is False):
            v = self.queue.pop()
            self.onQ[v] = False
            self.relax(v)


    def relax(self,e):
        v1 = e.edge_from()
        v2 = e.edge_to()

        if(self.distTo[v2] > self.distTo[v1] + e.weight()):
            self.distTo[v2] = self.distTo[v1] + e.weight()
            self.edgeTo[v2] = e
            if(self.onQ[v2] is False):
                self.insert_in_pq_after_relax(self.queue,v2)
                self.onQ[v2] = True
        else:
            #if()
            pass

        return


    def insert_in_pq_after_relax(self, queue, v):
            if(self.indexed_PQ.contains(v)):
                self.indexed_PQ.decreaseKey(v,self.distTo[v])
            else:
                self.indexed_PQ.insert(v,self.distTo[v])


    def hasNegativeWeightCycle(self):
        v = len(self.edgeTo)
        spt = EdgeWeightedDigraph(v)
        for i in range(v):
            if(self.edgeTo[v] is not Null):
                spt.add_edge(self.edgeTo[v])

        cycle_finder = EdgeWeightedGraph(spt.V)
        return cycle_finder.isCycle()
