#EVERY undirected graph is a directed graph with edges in both direction
#Hence previously written both DFS and BFS are digraph Algorithms

#REFER - https://www.coursera.org/learn/algorithms-part2/lecture/Vag6E/digraph-search

from digraph_api import Digraph

class DirectedDFS:

    def __init__(self,graph, source_vertex):

        self.G = graph
        self.s = source_vertex
        self.marked = []*self.G.V
        self.edgeTo = []*self.G.V

    def directed_dfs(self):
        self.dfs(self.G, self.s)


    def dfs(self,graph,vertex):
        self.marked[vertex] = True

        for i in self.graph.adj[vertex]:
            if self.marked[i] is not True:
                self.dfs(graph,i)
                self.edgeTo[i] = vertex

    def hasPathTo(self,vertex): #returns true if there is a path from source_vertex to vertex
        if(self.marked[vertex] is not NULL):
            return True

        return False


class DirectedBFS:

    def __init__(self, graph, source_vertex):

        self.G = graph
        self.s = source_vertex
        self.marked = []*self.G.V
        self.edgeTo = []*self.G.V
        self.distTo = []*self.G.V

    def directed_bfs(self):
        self.bfs(self.G, self.s)

    def bfs(self,graph,vertex):

        queue = []

        queue.append(vertex)

        while (queue != []):

            vertex = queue.pop(0)

            self.marked[vertex] = True

            for i in self.graph.adj[vertex]:
                if(self.marked[i] is not True):
                    queue.append(i)
                    self.marked[i] = True
                    self.edgeTo[i] = vertex

                    # fill the distTo array
                    if(self.edgeTo[i] is self.s):       #self.s is source_vertex
                        self.distTo[i] = 1
                    else: #we will never encounter a case self.distTo[self.edgeTo[i]] is not already calculated (related to the property that bfs always finds the shortest path)
                        self.distTo[i] = self.distTo[self.edgeTo[i]]  + 1


# Above BFS Algorithm also solves multiple source shortest path problem
