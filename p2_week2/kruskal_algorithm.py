#An undirected graph is connected when it has at least one vertex and there is a path between every pair of vertices. Equivalently, a graph is connected when it has exactly one connected component.
#In a connected graph, there are no unreachable vertices.

#A spanning tree T of an undirected graph G(with +ve edge weights) is a subgraph that is a tree which includes all of the vertices of G, with minimum possible number of edges and is connected and acyclic.
#Minimum spanning tree -> spanning tree with minimum weight


#KRUSKAL's Algo ->
# Take the edges and sort them by weights (using min priority queue or use sort function)
# If the edge does not create a cycle:
#    add it to the tree
# else: pass



from edge_weighted_graph_api import Edge
from edge_weighted_graph_api import EdgeWeightedGraph

class KruskalMst:

    def __init__(self,G):
        self.G = G
        self.V = self.G.V
        self.makeSet = [-1]*self.V
        self.rank = [0]*self.V
        self.mst = []

        sorted_edges = sorted(self.edges, key=itemgetter(1)) #refer - https://docs.python.org/3/howto/sorting.html
        #can use a min priority queue as well

        for i in self.V:
            self.makeSet[i] = i

        for i in sorted_edges:
            v1 = i.either()
            v2 = i.other(v1)

            if(EdgeWeightedGraph.findSet(v1) != EdgeWeightedGraph.findSet(v1)):
                EdgeWeightedGraph.union(v1,v2)
                self.mst.append(i)

        return self.mst
