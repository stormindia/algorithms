#RED link representation -
#         |
#         A
#        / \
#       /   \
#      B     \
#             C
#
# A-B link is RED if color of B is red (and not color of A) ==> child defines the color of link
# keep above point in mind while rotating the node

#No node has two red links connected to it (both its child can't be red; one child red and itself being red is also not possible)
#Every path from root to null link has the same number of BLACK links(perfect BLACK balance)
#Red links lean left

#FLOOR, CEILING, RANK, SEARCH(GET) functions remain same as of simple binary search trees

RED = True
BLACK = False

class red_black:

    def __init__(self,root):
        self.root = root

    class Node:
        def __init__(self,key,value,color):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.count = 0
            self.color = color


    def isRed(self,node):

        if(node is None): #null links are BLACK
            return False

        return node.color == RED

    def Rotate_Left(self,node):

        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RED

        return x

    def Rotate_Right(self,node):

        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = RED

        return x


    def Flip_Color(self,node): #to split a temporary 4 node

        node.color = RED
        h.left.color = BLACK
        h.right.color = BLACK


    def put(self,key,value):

        self.root = self.__put(self.root,key,value)

    def __put(self,h,key,value): #h is the node to be inserted

        if(h is None):
            return red_black.Node(key,value,color)

        if(key < h.key):
            h.left = self.__put(h.left,key,value)
        elif(key > h.key):
            h.right = self.__put(h.right,key,value)
        else:  #duplicate key
            h.value = value

        if self.isRed(h.right) and not self.isRed(h.left):  #lean left
            h = self.rotateLeft(h)
        if self.isRed(h.left) and self.isRed(h.left.left):  #balance 4 node
            h = self.rotateRight(h)
        if self.isRed(h.left) and self.isRed(h.right):      #split 4 node
            self.flipColors(h)
            
        h.count = 1 + self.size(h.left) + self.size(h.right)
        return h
