#URL - https://coursera.cs.princeton.edu/algs4/assignments/seam/specification.php

# Input -
# A W * H  image starting from (0,0) to (W-1, H-1) -> each pixel will have a RGB value

#Since we don't have a image data type as in the assignemnt, we assume that input is W*H array with each element having RGB as its value

from acyclic_shortest_path import Acyclic_SP
from ../p2_week1/topological_sorting import TopologicalSort
from directed_edge_weighted_graph_api import *


example_input =[[255,255,255],[255,255,255],[255,255,255],
                [255,255,255],[255,255,255],[255,255,255],
                [255,255,255],[255,255,255],[255,255,255]]



# a 3 by 4 image
#(0,0) (1,0) (2,0)
#(0,1) (1,1) (2,1)
#(0,2) (1,2) (2,2)
#(0,3) (1,3) (2,3)

MAX = 99999
#################HELPER class#########################
class Seam_CarverEdge:

    def __init__(self,v1,weight1,v2,weight2):
        self.v1 = v1
        self.v2 = v2
        self.weightV1 = weight1
        self.weightV2 = weight2

    def edge_from(self):
        return self.v1

    def edge_to(self):
        return self.v2

    def weight_from(self):
        return self.weightV1

    def weight_to(self):
        return self.weightV2

########################################################################################

################################Seam_Carver############################################

class Acyclic_SP_for_SEAM:

    def __init__(self,G,source_vertex, seam_direction):
        self.G = G
        self.S = source_vertex
        self.distTo = [MAX]*self.G.V
        self.edgeTo = []*self.G.V
        self.seam_direction = seam_direction #horizontal or vertical
        if(self.seam_direction != 'horizontal' or self.seam_direction != 'vertical'):
            return 'invalid seam_direction'

        topological_graph = TopologicalSort(self.G)
        topological_ordered_verteices = topological_graph.return_sorted_graph()

        for vertex in topological_ordered_verteices:
            for edge in self.G.adjacent_edges[vertex]:
                self.relax(edge)

        # Return 3 things -
        # 1. vertex in the bottom row(or column) for which seam is min
        # 2. total seam  value
        # 3. path from source_vertex to the vertex found in step 1
        if(self.seam_direction == 'horizontal'):
            MIN = MAX
            for j in range(self.h - 1):
                if(self.distTo[(self.w -1) + j*(self.h-1)] == MAX): #vertex not touched
                    pass
                else:
                    if(self.distTo[(self.w -1) + j*(self.h-1)] < MIN):
                        MIN = self.distTo[(self.w -1) + j*(self.h-1)]
                        vertex_pos = (self.w - 1) + j*(self.h-1)
        else if(self.seam_direction == 'vertical'):
            MIN = MAX
            for i in range(self.w - 1):
                if(self.distTo[i*(self.w -1) + (self.h-1)] == MAX): #vertex not touched
                    pass
                else:
                    if(self.distTo[i*(self.w -1) + (self.h-1)] < MIN):
                        MIN = self.distTo[i*(self.w -1) + (self.h-1)]
                        vertex_pos = i*(self.w - 1) + (self.h-1)


        seam_value = MIN

        i = abs((vertex_pos - (self.h - 1))) % self.w
        j = abs((vertex_pos - (self.w -1))) % self.h

        self.vertex = self.vertices[i][j] #vertex is the vertex for which the seam is min
        curr_vertex = vertex
        self.path_arr = []
        while(curr_vertex != source_vertex):
            self.path_arr.append(curr_vertex)
            curr_vertex = self.edgeTo[vertex_pos].from()
        self.path_arr.append(source_vertex)

    def relax(self,e):
        v1 = e.edge_from()
        v2 = e.edge_to()
        v1_pos = v1[0] + v1[1]*(self.h - 1)
        v2_pos = v2[0] + v2[1]*(self.h -1)

        if(self.distTo[v2_pos] > self.distTo[v1_pos] + e.weight_from()):
            self.distTo[v2_pos] = self.distTo[v1_pos] + e.weight_from()
            self.edgeTo[v2_pos] = e
        else:
            pass

        return

    def return_min_seam(self):
        return [seam_value, vertex, path_arr]


class Seam_Carver:

    def __init__(self,W,H,arr_pixel):

        self.w = W
        self.h = H
        self.vertices = []*self.G.V
        self.G_horizontal = EdgeWeightedDigraph(self.w * self.h)        #assume Edges are represented using Seam_CarverEdge and not DirectedEdge
        self.G_vertical = EdgeWeightedDigraph(self.w * self.h)

        k = 0
        for i in range(self.w):
            col = []
            for j in range(self.h):
                col.append([j,i,arr_pixel[k]])
                k += 1
            self.vertices.append(col)

##################### HELPER FUNCTIONS ###########################
    def isBorderElement(self,x,y):
        if(x == 0 or x == self.w - 1 or y == 0 or y == self.h -1):
            return True
        return False

    def isValidIndex(self,x,y):
        if(x < 0 or y < 0 or x > self.w - 1 or y > self.h-1):
            return False

        return True
#################################################################

    def width(self):
        return self.w

    def height(self):
        return self.h

    def calculate_energy(self,x,y):

        if(self.isBorderElement(x,y)):
            energy_value = 1000

        else:
            R_X = self.vertices[x+1][y][2][0] - self.vertices[x-1][y][2][0]
            G_X = self.vertices[x+1][y][2][1] - self.vertices[x-1][y][2][1]
            B_X = self.vertices[x+1][y][2][2] - self.vertices[x-1][y][2][2]

            delta_x_square = R_X**2 + G_X**2 + B_X**2

            R_Y = self.vertices[x][y+1][2][0] - self.vertices[x][y-1][2][0]
            G_Y = self.vertices[x][y+1][2][1] - self.vertices[x][y-1][2][1]
            B_Y = self.vertices[x][y+1][2][2] - self.vertices[x][y-1][2][2]

            delta_y_square = R_Y**2 + G_Y**2 + B_Y**2

            energy_value = (delta_x_square + delta_y_square)**0.5

        return energy_value


    def create_vertical_graph(self, G_vertical):
#there is a downward edge from pixel (x, y) to pixels (x − 1, y + 1), (x, y + 1), and (x + 1, y + 1)
        for i in range(self.w):
            for j in range(self.h):
                weight1 = self.calculate_energy(i,j)
                if(self.isValidIndex(i-1,j+1)):
                    weight2 = self.calculate_energy(i-1,j+1)
                    edge = Seam_CarverEdge(self.vertices[i][j],weight1,self.vertices[i-1][j+1],weight2)
                    G_vertical.add_edge(edge)
                if(self.isValidIndex(i,j+1)):
                    weight2 = self.calculate_energy(i,j+1)
                    edge = Seam_CarverEdge(self.vertices[i][j],weight1,self.vertices[i][j+1],weight2)
                    G_vertical.add_edge(edge)
                if(self.isValidIndex(i+1,j+1)):
                    weight2 = self.calculate_energy(i+1,j+1)
                    edge = Seam_CarverEdge(self.vertices[i][j],weight1,self.vertices[i+1][j+1],weight2)
                    G_vertical.add_edge(edge)

            return G_vertical

    def create_horizontal_graph(self,G_horizontal):
#there is a rightward edge from pixel (x, y) to pixels (x + 1, y - 1), (x+1, y), and (x + 1, y + 1)
        for i in range(self.w):
            for j in range(self.h):
                weight1 = self.calculate_energy(i,j)
                if(self.isValidIndex(i+1,j-1)):
                    weight2 = self.calculate_energy(i+1,j-1)
                    edge = Seam_CarverEdge(self.vertices[i][j],weight1,self.vertices[i+1][j-1],weight2)
                    G_horizontal.add_edge(edge)
                if(self.isValidIndex(i+1,j)):
                    weight2 = self.calculate_energy(i+1,j)
                    edge = Seam_CarverEdge(self.vertices[i][j],weight1,self.vertices[i+1][j],weight2)
                    G_horizontal.add_edge(edge)
                if(self.isValidIndex(i+1,j+1)):
                    weight2 = self.calculate_energy(i+1,j+1)
                    edge = Seam_CarverEdge(self.vertices[i][j],weight1,self.vertices[i+1][j+1],weight2)
                    G_horizontal.add_edge(edge)

            return G_horizontal

    def findHorizontalSeam(self):

        self.G_horizontal = self.create_horizontal_graph(self.G_horizontal)
        min_seam = []
        for i in range(self.h -1):
            calculate_seam = Acyclic_SP_for_SEAM(self.G_horizontal, self.vertices[0][i], 'horizontal')
            seam = calculate_seam.return_min_seam()
            if(min_seam == []):
                min_seam = seam
            else:
                if(min_seam[0] > seam[0]):
                    min_seam = seam
                else:
                    pass

        return min_seam

    def findVerticalSeam(self):

        self.G_vertical = self.create_vertical_graph(self.G_vertical)
        min_seam = []
        for j in range(self.w -1):
            calculate_seam = Acyclic_SP_for_SEAM(self.G_vertical, self.vertices[j][0], 'vertical')
            seam = calculate_seam.return_min_seam()
            if(min_seam == []):
                min_seam = seam
            else:
                if(min_seam[0] > seam[0]):
                    min_seam = seam
                else:
                    pass

        return min_seam
