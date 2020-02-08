# Works only on directed acyclic graph (dag)
# Algorithm
# Run DFS
# Return vertices in reverse post-order

# to print vertices in reverse post order - use stack - Using just an array and prinitng it in reverse for simiplicity

from digraph_api import Digraph

class TopologicalSort:

    def __init__(self,graph):
        self.G = graph
        self.marked = []*self.G.V
        self.reversePost = []*self.G.V

        for i in self.G.V:
            if(self.marked[i] is not True):

                self.dfs_for_topological_sort(self.G,i)


    def dfs_for_topological_sort(self,graph,vertex):

        self.marked[vertex] = True

        for i in self.adj[vertex]:
            if(self.marked[i] is not True):
                self.dfs_for_topological_sort(self.G,i)
        self.reversePost.append(vertex)

    def return_sorted_graph(self):

        # print the array in reverse order
        for i in range(len(self.reversePost),0, -1):
            print(self.reversePost[i])
