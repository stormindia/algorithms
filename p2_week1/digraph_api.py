# Directed graph apis

# implementation is almost same as that of undirected graph apis(graph_api)

# only add edge function changes

class Digraph:

    def __init__(self, V):
        self.V = V
        self.adj = []*V

        for i in range(V):
            self.adj[i] = []


    #add an edge between v-w
    def add_edge(self,v,w):
        self.adj[v].append(w)


    #returns the adjacent_vertices
    def adjacent_vertices(self,v):
        return self.adj[v]

    #return the out degree of v
    def out_degree(self,v):

        return len(self.adj[v])

    def in_degree(self,vertex):
        count = 0

        for i in range(self.V):
            for j in self.adj[i]:
                if(self.adj[i][j] == vertex):
                    count = count + 1
        return count

    #compute maximum degree
    def max_out_degree(self):

        max = 0
        for i in range(self.V):
            if(self.out_degree(i) > max):
                max = self.out_degree(i)

        return max

    #count number of self loops
    def self_loop_count(self):
        count = 0
        for i in range(self.V):
            for j in range(len(self.adj[i])):
                if(i == self.adj[i][j]):
                    count = count + 1

        return count/2
