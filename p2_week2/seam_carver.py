#URL - https://coursera.cs.princeton.edu/algs4/assignments/seam/specification.php

# Input -
# A W * H  image starting from (0,0) to (W-1, H-1) -> each pixel will have a RGB value

#Since we don't have a image data type as in the assignemnt, we assume that input is W*H array with each element having RGB as its value

from directed_edge_weighted_graph_api import EdgeWeightedDigraph
from acyclic_shortest_path import Acyclic_SP

example_input =[[255,255,255],[255,255,255],[255,255,255],
                [255,255,255],[255,255,255],[255,255,255],
                [255,255,255],[255,255,255],[255,255,255]]


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

    def width(self):
        return self.w

    def height(self):
        return self.h

    def isBorderElement(self,x,y):
        if(x == 0 or x == self.w - 1 or y == 0 or y == self.h -1):
            return True
        return False

    def isValidIndex(self,x,y):
        if(x < 0 or y < 0 or x > self.w - 1 or y > self.h-1):
            return False

        return True


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
