class Edge:

    def __init__(self,v1,v2,weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    #given an edge, return any endpoint(vertex)
    def either(self):
        return self.v1

    #given one vertex of the edge, return the other endpoint
    def other(self,vertex):
        if(vertex == self.v1):
            return self.v2
        else:
            return self.v1

    #compares the edge of this constructor with other edge passed in the function
    def compareTo(self,edge):
        if(self.weight > edge.weight):
            return 1
        elif(self.weight < edge.weight):
            return -1
        else:
            return 0


#Allow self loop and parallel edges
class EdgeWeightedGraph:
# e --> represents an Edge
    def __init__(self, V):
        self.V = V
        self.adj = []*V    #contains edges instead of vertices
        self.edges = []

        for i in range(V):
            self.adj[i] = []


    #add an edge between v-w
    def add_edge(self,e):
        # e --> represents an Edge
        #parallel edges allowed
        v = e.either()
        w = e.other(v)
        self.adj[v].append(e)
        self.adj[w].append(e)
        self.edges.append(e)

    #returns the adjacent edges
    def adjacent_edges(self,v):
        return self.adj[v]

    #returns all the edges
    def edges(self):
        return self.edges

    #detect cycle using Union Find algorithm (updated for path compression using rank)
    def isCycle(self):
        self.makeSet = [-1]*self.V
        self.rank = [0]*self.V


        for i in self.V:
            self.makeSet[i] = i

        def findSet(v):
            if(self.makeSet[v] == v):
                return v
            else:
                return findSet(self.makeSet[v])

        def union(v1,v2):
            a = findSet(v1)
            b = findSet(v2)
            if(self.rank[a] > self.rank[b]):
                self.makeSet[b] = a
                self.rank[a] += self.rank[b]
            else:
                self.makeSet[a] = b
                self.rank[b] += self.rank[a]



        for i in self.edges:
            v1 = i.either()
            v2 = i.other(v1)

            a = findSet(v1)
            b = findSet(v2)

            if(a == b):
                return True
            else:
                union(a,b)

        return False
