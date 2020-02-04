# Problem statement - https://coursera.cs.princeton.edu/algs4/assignments/kdtree/specification.php
# 2d-tree implementation. Write a mutable data type KdTree.java that uses a 2d-tree to implement the same API (but replace PointSET with KdTree).
# A 2d-tree is a generalization of a BST to two-dimensional keys. The idea is to build a BST with points in the nodes, using the x- and y-coordinates of the points
# as keys in strictly alternating sequence.
# lecture reference - https://www.coursera.org/learn/algorithms-part1/lecture/Yionu/kd-trees

#assumption - no duplicate node is being added for simplicity - less corner cases implementation

class 2d_bst:
    def __init__(self,root):
        self.root = root

    class Node:
        def __init__(self, x_cord, y_cord):
            self.left = None
            self.right = None

            #div_line indicates if the points divide the plane horizontally or vertically
            self.div_line = None  # possibe values - horizontal or vertical


    # search implementation writtent to find parent - can be used for normal search as well
    def find_parent(self,node):
        if(node is self.root):
            return -1
        else:
            curr_node = self.root
            while(curr_node.right is not None and curr_node.left is not None):
                tmp_node = curr_node

                if( curr_node.div_line is horizontal):
                    if(curr_node.y_cord < node.y_cord):
                        curr_node = curr_node.left
                    else:
                        curr_node = curr_node.right
                else: # div_line is vertical
                    if(curr_node.x_cord < node.x_cord):
                        curr_node = curr_node.left
                    else:
                        curr_node = curr_node.right

                if(curr_node is node):
                    return tmp_node

            return False

    #if the div_line is horizontal - insert on the basis of y coordinates
    #if the div_line is vertical - insert on the basis of x coordinates
    def put(self,x_cord,y_cord):
        self.root = self.__put(self.root,x_cord,y_cord,vertical)


    def __put(self,node,x_cord,y_cord,div_line): #for recursion

        if(node == None):
            #create a new Node
            new_node = 2d_bst.Node(x_cord,y_cord)
            new_node.div_line = div_line
            return new_node

        if(node.div_line is horizontal):
            if(y_cord < node.y_cord):
                node.left = self.__put(node.left,x_cord,y_cord,vertical)
            elif(y_cord > node.y_cord):
                node.right = self.__put(node.right,x_cord,y_cord,vertical)
            else:
                node.value = value
        else:
            if(x_cord < node.x_cord):
                node.left = self.__put(node.left,x_cord,y_cord,horizontal)
            elif(y_cord > node.y_cord):
                node.right = self.__put(node.right,x_cord,y_cord,horizontal)
            else:
                node.value = value


        #node.count = 1 + self.size(node.left) + self.size(node.right)
        return node
