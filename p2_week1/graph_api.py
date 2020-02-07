# graph implementation using adjacency list graph representation
#implementation in python
#Since python does not have any implicit BAG data structure as used in the course. we can write it in following manner by taking advantage of dynamic arrays in python
#We can take an array where each element of an array is an array itself
#We can also make each element of the array a queue but insertion in array(apend) and queue(ennqueue) is same

# V represents total number of vertices - starts from 0 to # NOTE: vertices are continuous

class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = []*V

        for i in range(V):
            self.adj[i] = []


    #add an edge between v-w
    def add_edge(self,v,w):
        #parallel edges allowed
        self.adj[v].append(w)
        self.adj[w].append(v)


    #returns the adjacent_vertices
    def adjacent_vertices(self,v):
        return self.adj[v]

    #return the degree of v
    def degree(self,v):

        return len(self.adj[v])

    #compute maximum degree
    def max_degree(self):

        max = 0
        for i in range(self.V):
            if(self.degree(i) > max):
                max = self.degree(i)

        return max

    #count number of self loops
    def self_loop_count(self):
        count = 0
        for i in range(self.V):
            for j in range(len(self.adj[i])):
                if(i == self.adj[i][j]):
                    count = count + 1

        return count/2
