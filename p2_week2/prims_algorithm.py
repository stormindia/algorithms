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

        self.visit(self.G,0)

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
        for e in EdgeWeightedGraph.adjacent_edges(v):
            i = e.either()
            k = e.other(i)    #gives the other vertex of the edge
            if(self.marked[k] is False):
                self.PQ.insert(e)

    def returnMST(self):
        return self.mst




# EAGER implementation
from indexed_PQ import IndexPQ

class EagerPrimMst:

    def __init__(self,G):
        self.G = G
        self.V = self.G.V
        self.indexed_PQ = IndexPQ(self.V)
        self.EagerMst = []
        self.marked = [False]*self.V
        self.distTo = [999]*self.V
        self.edgeTo = []*self.V

        self.visit(self.G,0)

        while(!self.indexed_PQ.iSEmpty()):
            e = self.indexed_PQ.delMin()
            v1 = e.either()
            v2 = e.other(v1)
            if(self.marked[v1] and self.marked[v2]):
                continue #returns control to the WHILE statement and next iteration is processed
            self.EagerMst.append(e)
            if(self.marked[v1] is False):
                self.visit(G,v1)
            if(self.marked[v2] is False):
                self.visit(G,v2)


    def visit(self,G,v):
        self.marked[v] = True

        #refer edge_weighted_graph_api
        for e in EdgeWeightedGraph.adjacent_edges(v):
            i = e.either()
            k = e.other(i)    #gives the other vertex of the edge
            if(self.marked[k] is False):
                if(self.e.weight() < self.distTo[k]):
                    self.distTo[k] = self.e.weight()
                    self.edgeTo[k] = e
                    if(self.indexed_PQ.contains(e)):
                        self.indexed_PQ.decreaseKey(e,self.distTo[k])
                    else:
                        self.indexed_PQ.insert(e,self.distTo[k])

    def returnEagerMST(self):
        return self.EagerMst
