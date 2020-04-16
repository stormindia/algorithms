# check if a graph is acyclic and bipartite
# refer https://github.com/stormindia/algorithms/blob/master/Robert%20Sedgewick_%20Kevin%20Daniel%20Wayne-Algorithms-Addison-Wesley%20%20(2011).pdf   page 547

#import previously written dfs algo
from graph_api import Graph

class Check_Cycle:

    def __init__(self,Graph):
        self.G = Graph
        self.marked = []*self.G.V   # TRUE or False
        self.hasCycle = NULL # TRUE or False
        self.edgeTo = []*self.G.V


    def Cycle(self):

        for i in range(self.G.V):
            if (self.marked[i] is not True):
                self.dfs_for_cycle(self.G, i,i)

    def dfs_for_cycle(self,graph,vertex,source_vertex):

        self.marked[vertex] = True

        for i in self.Graph.adj[vertex]:
            if (self.marked[i] is not True):
                self.dfs_for_cycle(self.G,i,source_vertex)
            else:
                if(i != source_vertex):
                    self.hasCycle = True
                else:
                    pass

class check_Bipartite:

    def __init__(self,Graph):
        self.G = Graph
        self.marked = []*self.G.V   # TRUE or False
        self.color = []*self.G.V # Two possible colors (true/False)
        self.isTwoColorable = NULL #  boolean value
        self.edgeTo = []*self.G.V

    def TwoColor(self):
        for i in range(self.G.V):
            if(self.marked[i] is not True):
                self.dfs_for_color(self.G, i)

    def dfs_for_color(self, graph, vertex):
        self.marked[vertex] = True
        for i in self.Graph.adj[vertex]:
            if (self.marked[i] is not True):
                self.color[i] = !self.color[vertex]
                self.dfs_for_color(self.G,i)
            else:
                if(self.color[i] == self.color[vertex] ):
                    self.isTwoColorable = False

    def isBipartite(self):
        return self.isTwoColorable
