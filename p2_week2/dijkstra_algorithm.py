#ALGO -->
#Consider all vertices in increasing order of distance from source_vertex S
#    (non-tree vertex wtih lowest distTo[] value)
#Add vertex to tree and relax all edges pointing from that vertex


#import DirectedEdge, EdgeWeightedDigraph, SPT_apis
from directed_edge_weighted_graph_api import *
from indexed_PQ import IndexPQ

MAX = 99999

G = EdgeWeightedDigraph(V)

class Dijkstra_SP:

    def __init__(self,G,source_vertex):
        self.G = G
        self.S = source_vertex
        self.distTo = [MAX]*self.G.V
        self.edgeTo = []*self.G.V
        self.indexed_PQ = IndexPQ(self.G.V)

        self.distTo[self.S] = 0

        self.indexed_PQ.insert(self.S,0)

        while(self.indexed_PQ.isEmpty() is False ):
            vertex = self.indexed_PQ.delMin()
            for e in self.G.adjacent_edges(vertex):
                self.relax(e)


    def relax(self,e):
        v1 = e.edge_from()
        v2 = e.edge_to()

        if(self.distTo[v2] > self.distTo[v1] + e.weight()):
            self.distTo[v2] = self.distTo[v1] + e.weight()
            self.edgeTo[v2] = e
            self.insert_in_pq_after_relax(self.indexed_PQ,v2)
        else:
            pass

        return


    def insert_in_pq_after_relax(self, indexed_pq, v):
            if(self.indexed_PQ.contains(v)):
                self.indexed_PQ.decreaseKey(v,self.distTo[v])
            else:
                self.indexed_PQ.insert(v,self.distTo[v])
