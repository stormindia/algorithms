#ALGO -
# Start with vertex 0 and greedily grow tree # TEMP:
# Add to T with  Minimum weight edge with exactly one endpoint in # TEMP:
# Repeat until V-1 edges


from edge_weighted_graph_api import Edge
from edge_weighted_graph_api import EdgeWeightedGraph

class LazyPrimsMST:

    def __init__(self,G):
        self.PQ = MinPq()
        self.mst = []
        self.V = self.G.V
        self.marked = [False]*self.V

        self.visit(G,0)

        while(!self.PQ.iSEmpty()):
            e = PQ.delMin()
            v1 = e.either()
            v2 = e.other(v1)
            if(self.marked[v1] and self.marked[v2]):
                continue #returns control to the WHILE statement and next iteration is processed
            self.mst.append(e)
            if(self.marked[v1] is False):
                self.visit(G,v1)
            if(self.marked[v2] is False):
                self.visit(G,v2)


    def visit(self,G,v):
        self.marked[v] = True

        #refer edge_weighted_graph_api
        for e in EdgeWeightedGraph.edges_from_that_vertex(v):
            k = e[0]    #gives the other vertex of the edge
            if(self.marked[k] is False):
                self.PQ.insert(e)

    def returnMST(self):
        return self.mst
