# Works only on directed acyclic graph (dag)
# Algorithm
# Run DFS
# Return vertices in reverse post-order

#added finding directed cycle

# to print vertices in reverse post order - use stack - Using just an array and prinitng it in reverse for simiplicity

from digraph_api import Digraph

class TopologicalSort:

    def __init__(self,graph):
        self.G = graph
        self.marked = []*self.G.V
        self.reversePost = []*self.G.V
        self.dfs_done = [0]*self.G.V
        self.edgeTo = []*self.G.V

        for i in self.G.V:
            if(self.marked[i] is not True):

                self.dfs_for_topological_sort(self.G,i)
        self.return_sorted_graph()

    def dfs_for_topological_sort(self,graph,vertex):

        self.marked[vertex] = True

        for i in self.adj[vertex]:
            if(self.marked[i] is not True):
                self.dfs_for_topological_sort(self.G,i)
        self.reversePost.append(vertex)

    def return_sorted_graph(self):

        reverse_post_order =  []
        # print the array in reverse order
        for i in range(len(self.reversePost),0, -1):
            reverse_post_order.append(self.reversePost[i])
            print(self.reversePost[i])

        return reverse_post_order

    def dfs_for_directed_cycle(self,graph,vertex):
        self.marked[vertex] = True

        for i in self.adj[vertex]:
            if(self.marked[i] is not True):
                self.dfs_for_directed_cycle(self.G,i)
                self.edgeTo[i] = vertex
            else:
                if(self.dfs_done[i] == True):
                    #cycle exsist
                    cycle_arr = []
                    for(j in self.edgeTo[i]):
                        if(j != i):
                            cycle_arr.append(j)
                    cycle_arr.append(i)
                    cycle_arr.append(vertex)

            self.dfs_done[i] = True
