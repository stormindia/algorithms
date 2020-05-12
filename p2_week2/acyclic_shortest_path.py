from ../p2_week1/topological_sorting import TopologicalSort

from directed_edge_weighted_graph_api import *


MAX = 99999

G = EdgeWeightedDigraph(V)

class Acyclic_SP:

    def __init__(self,G,source_vertex):
        self.G = G
        self.S = source_vertex
        self.distTo = [MAX]*self.G.V
        self.edgeTo = []*self.G.V

        topological_graph = TopologicalSort(self.G)
        topological_ordered_verteices = topological_graph.return_sorted_graph()

        for vertex in topological_ordered_verteices:
            for edge in self.G.adjacent_edges[vertex]:
                self.relax(edge)


    def relax(self,e):
        v1 = e.edge_from()
        v2 = e.edge_to()

        if(self.distTo[v2] > self.distTo[v1] + e.weight()):
            self.distTo[v2] = self.distTo[v1] + e.weight()
            self.edgeTo[v2] = e
        else:
            pass

        return
