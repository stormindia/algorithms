# URL - https://coursera.cs.princeton.edu/algs4/assignments/wordnet/specification.php
import csv
from graph_api import Graph
from digraph_api import Digraph

#synsets basically contain value of the nodes (which we don't even require to implement graph and to calculate SAP)
#hypernym contains the entire graph
#each value of each line represents a vertex in hypernym.txt
#In each line, values other than first value in hypernym.txt represents an edge to the first value
#That is all we need to create the graph

noun_list = []
with open('synsets.txt') as synset_file:
    synset_iterator = csv.reader(synset_file,delimiter = ',')
    for row in synset_iterator:
        noun_list.append(row[0])


adjacency_matrix = []
with open('hypernyms.txt') as hypernym_file:
    hypernym_iterator = csv.reader(hypernym_file, delimiter = ',')
    for row in hypernym_iterator:
        adjacency_matrix.append(int(row[0]))
        adjacency_matrix[int(row[0])] = []
        for j in range(1,len(row)):
            adjacency_matrix[int(row[0])].append(int(row[j]))

#adjacency_matrix received from above can be used as a graph where each index represents a vertex and the values stored in the index represents a directed edge from the index to the values



#following code is written assuming we have a graph as per our apis

class WordNet:

    def __init__(self,graph):
        self.G = graph
        self.V = V #represents all the vertices
        self.marked = []*V

# returns all WordNet nouns
    def iterable_noun(self):
        return noun_list

# is the word a WordNet noun?
    def isNoun(self, word):
        # method 1 - a simple search in the array to check if the word is present => binary search => logarthmic time
        # method 2 - use dfs => implemented below

        for i in self.V:
            if ( noun_list[i] == word):
                return True
            else:
                if (self.marked[i] is not True):
                    self.dfs_to_check_is_noun(i,word)


    def dfs_to_check_is_noun(self,vertex,word):

        self.marked[vertex] = True
        for i in self.adj[vertex]:
            if(noun_list[i] != word):
                if(self.marked[i] is not True):
                    self.dfs_to_check_is_noun(i,word)
            else:
                return True

    def sap(self,word1, word2):
        pass
        #implemented below


class SAP:
    def __init__(self,graph,vertex1,vertex2):
        self.G = graph
        self.V = V
        self.v1 = vertex1
        self.v2 = vertex2
        self.marked_for_v1 = []*V
        self.marked_for_v2 = []*V
        self.edgeTo = []*self.G.V
        self.distTo_v1 = []*self.G.V        #dist of vertex from vertex1
        self.distTo_v2 = []*self.G.V        #dist of vertex from vertex2
        self.hasAncestor = NULL             #boolean value
        self.commonAncestors = []

        for i in self.distTo_v1:
            self.distTo_v1[i] = []
            self.distTo_v2[i] = []

    #Run dfs for vertex1
    #Get all adjacent vertices and stop when the in_degree of the node becomes 0
    #Update the self.marked_for_v1 array and self.distTo_v1 array

    #Run dfs for vertex2
    # update self.commonAncestors if self.marked_for_v1 for a vertex is True
    #set self.hasAncestor as True
    #Update the self.marked_for_v2 array and self.distTo_v2 array


    def dfs_for_vertex1(self,vertex1):
        self.marked_for_v1[vertex1] = True
        for i in self.adj[vertex1]:
            if(self.marked_for_v1[i] is not True):
                if(self.edgeTo[i] is self.v1):
                    self.distTo_v1[i] = 1
                else: #we will never encounter a case self.distTo[self.edgeTo[i]] is not already calculated (related to the property that bfs always finds the shortest path)
                    self.distTo_v1[i] = self.distTo_v1[self.edgeTo[i]]  + 1
                self.dfs_for_vertex1(i)


    def dfs_for_vertex2(self,vertex2):
        if(self.marked_for_v1[vertex2] is True):
            self.hasAncestor = True
            self.commonAncestors.append(vertex2)

        self.marked_for_v2[vertex2] = True

        for i in self.adj[vertex2]:
            if(self.marked_for_v2[i] is not True):
                if(self.edgeTo[i] is self.v2):
                    self.distTo_v2[i] = 1
                else: #we will never encounter a case self.distTo[self.edgeTo[i]] is not already calculated (related to the property that bfs always finds the shortest path)
                    self.distTo_v2[i] = self.distTo_v2[self.edgeTo[i]]  + 1

                self.dfs_for_vertex2(i)


    def length(self,vertex1,vertex2):

        if(vertex1 == vertex2):
            return 0

        self.dfs_for_vertex1(vertex1)
        self.dfs_for_vertex2(vertex2)

        if(self.hasAncestor  is not True):
            return -1
        else:
            sap_length = 99999999
            min_ancestor = NULL

            for i in self.commonAncestors:
                dist_from_v1 = self.distTo_v1[i]
                dist_from_v2 = self.distTo_v2[i]
                if((dist_from_v1 + dist_from_v2) < sap_length):
                    sap_length = dist_from_v1 + dist_from_v2
                    min_ancestor = i

            return sap_length , min_ancestor


#   Below 3 can be solved using above function
#  // a common ancestor of v and w that participates in a shortest ancestral path; -1 if no such path
#  public int ancestor(int v, int w)
#
# // length of shortest ancestral path between any vertex in v and any vertex in w; -1 if no such path
# public int length(Iterable<Integer> v, Iterable<Integer> w)
#
# // a common ancestor that participates in shortest ancestral path; -1 if no such path
# public int ancestor(Iterable<Integer> v, Iterable<Integer> w)
#

# Outcast detection. Given a list of wordnet nouns A1, A2, ..., An, which noun is the least related to the others? To identify an outcast, compute the sum of the distances between each noun and every other one:
# di   =   dist(Ai, A1)   +   dist(Ai, A2)   +   ...   +   dist(Ai, An)
# and return a noun At for which dt is maximum.

    def outcast_detection(self):

        outcast_value = NULL

        distances = []
        dist = 0

        for i in self.V:
            for j in self.V:
                dist = dist + self.length(i,j)

            distances.append(dist)
            dist = 0

        max_dist = 0
        for i in len(distances):
            if(distances[i] > max_dist):
                max_dist = distances[i]
                outcast_value = i

        return outcast_value
