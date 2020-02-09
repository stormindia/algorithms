# two vertices are strongly connected if there is a directed path from v to w and from w to v
# for proof - read https://github.com/stormindia/algorithms/blob/master/Robert%20Sedgewick_%20Kevin%20Daniel%20Wayne-Algorithms-Addison-Wesley%20%20(2011).pdf page 588

# Algorithm -
# Given a digraph G, use DepthFirstOrder to compute the reverse postorder of
# its reverse, G.R.
#  Run standard DFS on G, but consider the unmarked vertices in the order just
# computed instead of the standard numerical order.
#  All vertices reached on a call to the recursive dfs() from the constructor are in a
# strong component (!), so identify them as in CC.


# for getting a reverse graph - refer https://www.geeksforgeeks.org/transpose-graph/

#use previously written apis
from digraph_api import Digraph

from topological_sorting import TopologicalSort


class  KosarajuSCC:

    def __init__(self,graph):
        self.G = graph
        self.marked = []*self.G.V
        self.count = 0 # number of connected componenets
        self.id = []*self.G.V

        #step 1 of algo
        dfo = TopologicalSort(G.compute_reverse_graph())

        #step 2 of algo
        for i in dfo:
            if not self.marked[i]:
                self.dfs(G, i)
                self.count += 1


    def compute_reverse_graph(self):
        #create a object graph with V vertices
        reverse_graph = Digraph(self.V)

        for i in self.G.V:
            for j in self.G.adj[i]:
                reverse_graph.add_edge(j,i)

        return reverse_graph


    def dfs_for_kosaraju(self,graph,vertex):
        self.marked[vertex] = True
        self.id[vertex] = self.count
        for w in G.adjacent(vertex):
            if not self.marked[w]:
                self.dfs(G, w)

    def is_stronglyConnected(self,v,w):
        if(self.id[v] == self.id[w]):
            return True
        else:
            return False

    def number_of_connectedComponenets(self):
        return self.count
