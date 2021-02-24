# Find if v is  connected to w in constant time without using adjacency sparse matrix
# Algorithm
# To visit a vertex V:
# Mark it as true
# recursively visit all unmarked vertices adjacent to v
# refer - https://www.coursera.org/learn/algorithms-part2/lecture/Dzl65/connected-components


from graph_api import Graph

class connected_components:

    def __init__(self,graph):

        self.G = graph
        self.marked = [False]*self.G.V  #from graph_api V represents total number of vertices
        self.cc = []*self.G.V #id of connected component
        self.count = 0

        for i in range(self.G.V):
            if(self.marked[i] is not True):
                self.dfs(self.G , i)
                self.count += 1




    def dfs(self,G,vertex):

        self.marked[vertex] = True
        self.cc[vertex] = self.count

        for i in self.G.adj[vertex]:
            if(self.marked[i] is not True):
                self.marked[i] = True

                self.dfs(self.G,i):
                self.edgeTo[i] = vertex



    def connected_components_number(self):
        return self.count

    def is_connected(self,v1,v2):
        if(self.cc[v1] == self.cc[v2]):
            return True

        return False
