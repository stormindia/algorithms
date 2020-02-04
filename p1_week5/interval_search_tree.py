# 1 D interval search
# insert an interval - lo, hi
# search for an interval lo, hi
# delete an interval lo, hi
# interval intersection query - given an interval (lo,hi), find all interval(s) in the set that intersect (lo, hi)

# A BST where  each node stores an interval (lo, hi)
# Use left endpoint as BST keys
# Also store max endpoint in subtree rooted at that node
# to update max endpoint whenver an insertion occur, we need to able to access parent element of the inserted_node


# below is a pseudo code - a full fleged implementation in python is getting too complicated to write
# grateful to anyone who wishes to contribute to a python code based on the algorithm as suggested here - https://www.coursera.org/learn/algorithms-part1/lecture/ot9vw/interval-search-trees

class intervalST:

    def __init__(self,root):
        self.root = root

    class Node:
        def __init__(self,low,high):
            self.key = low
            self.low = low      #for code simplification; using that variable again
            self.high = high
            self.left = None
            self.right = None
           #self.count = 0
            self.max_endpoint = high


    def put(self, lo, hi, val):
        return

    def get(self, lo, hi):
        return

    def delete(self, lo, hi):
        return

    def intersects(self, lo, hi):
        return


    def contains(self,key):
        node = self.root

        while(node is not None):
            if(key < node.key):
                node = node.left
            elif(key > node.key):
                node = node.right
            else:
                return True

        return False

    def intervalSearch(self, lo ,hi):
        x = self.root
        while x != None:
            if x.interval.intersects(lo, hi):
                return x.interval
            elif x.left == None:
                x = x.right
            elif x.left.max < lo:
                x = x.right
            else:
                x = x.left
        return None
