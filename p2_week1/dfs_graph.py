# DFS for graph - algo
# DFS(to visit a vertex v)
# Mark v as visited
# recursively visit al vertices w adjacent to v


#use previously written graph_api

from graph_api import Graph

class DepthFirstPaths:

    def __init__(self,graph,source_vertex):
        self.G = graph
        self.s = source_vertex
        self.marked = []*self.G.V
        self.edgeTo = []*self.G.V


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


    def pathTo(self,vertex): #returns the path from source_vertex to vertex

        if(self.hasPathTo(vertex) is not True):
            return NULL

        path_array = []

        path_array.append(vertex)
        while(vertex != source_vertex):
            vertex = self.edgeTo(vertex)
            path_array.append(vertex)

        path_array.append(source_vertex)

        return path_array


# PROPERTIES
# DFS marks all vertices connected to source_vertex in time proportional to the sum of their degrees
# After DFS, all the connected vertices can be found in constant time. The path can be found in time proportional to its length
