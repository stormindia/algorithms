#BFS computes shortest path from source_vertex to all other vertices in time proportional to E + V

#BFS is implemented using queue

#DFS is implemented using stacks

# we can simply use python array features to implement queue and use queue.pop and queue.append features (https://www.geeksforgeeks.org/queue-in-python/)

# Algorithm
# Put source_vertex on FIFO queue and mark source_vertex as visited
# While queue is not empty:
#   remove the last added vertex v from the queue
#   add each of v's unmarked neighbours to the queue and mark them as visited


from graph_api import Graph

def BreadthFirstPath:

    def __init__(self, graph, source_vertex):

        self.G = graph
        self.s = source_vertex
        self.marked = []*self.G.V
        self.edgeTo = []*self.G.V
        self.distTo = []*self.G.V

    def dfs(self,graph,source_vertex):

        queue = []

        queue.append(source_vertex)

        while (queue != []):

            vertex = queue.pop(0)

            self.marked[vertex] = True

            for i in self.graph.adj[vertex]:
                if(self.marked[i] is not True):
                    queue.append(i)
                    self.marked[i] = True

                # fill the distTo array
                if(self.edgeTo[i] is source_vertex):
                    self.distTo[i] = 1
                else: #we will never encounter a case self.distTo[self.edgeTo[i]] is not already calculated (related to the property that bfs always finds the shortest path)
                    self.distTo[i] = self.distTo[self.edgeTo[i]]  + 1
