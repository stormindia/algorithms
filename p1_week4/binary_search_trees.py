class BST:

    def __init__(self,root):
        self.root = root

    class Node:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.count = 0


    def size(self,node):
        if(node == None):
            return None
        return node.count

    def complete_size(self):
        if(self.root != None):
            return self.root.count
        else:
            return None

    def get(self,key):

        curr_node = self.root

        while(curr_node != None):
            if (key < curr_node.key):
                curr_node = curr_node.left
            elif(key > curr_node.key):
                curr_node = curr_node.right
            else:
                print("node found!")
                return curr_node.value

        print("node not found")
        return False

    #finds min in a subtree
    def find_min(self,node):

        while(node.left is not None):
            node = node.left

        return node

    def put(self,key,value):
        self.root = self.__put(self.root,key,value)

    def __put(self,node,key,value): #for recursion

        if(node == None):
            #create a new Node
            return BST.Node(key,value)

        if(key < node.key):
            node.left = self.__put(node.left,key,value)

        elif(key > node.key):
            node.right = self.__put(node.right,key,value)
        else:
            node.value = value

        node.count = 1 + self.size(node.left) + self.size(node.right)
        return node


    # FLOOR -> Largest key <= given key
    def floor(self, key):
        node = self.__floor(self.root, key)

        if(node == None):
            return None

        return node.key

    def __floor(self,node,key):

# WRONG IMPLEMENTATION
#         if(node == None):
#             return None
#         elif(key > node.key):
#             node = self.__floor(node.right,key)
#         elif(key < node.key):
#             node = self.__floor(node.left,key)
#         else:
#             return node

        if(node == None):
            return None

        if(key == node.key):
            return node

        if(key < node.key):
            node = self.__floor(node.left,key)

        new_node = self.__floor(node.right,key)
        if(new_node != None):
            return new_node
        else:
            return node


    #CEILING -> Smallest key >= given key
    def ceiling(self,key):
        node = self.__ceiling(self.root,key)

        if(node == None):
            return None

        return node.key

    def __ceiling(self,node,key):

        if(node == None):
            return None

        if(key == node.key):
            return node

        if(key > node.key):
            node = self.__ceiling(node.right,key)

        new_node = self.__ceiling(node.left,key)
        if(new_node != None):
            return new_node
        else:
            return node


    #RANK -> number of keys < given keys
    def rank(self,key):
        return self.__rank(self.root,rank)

    def __rank(self,node,key):
        if(node == none):
            return 0

        if(key < node.key):
            return self.__rank(node.left,key)
        elif(key > node.key):
            return 1 + size(node.left) + self.__rank(node.right,key)

        else:
            return size(node.left)

#Depth first search - {IN, PRE, POST}ORDER
    #INORDER TRAVERSAL
    def inorder(self):
        # q = Queue() #Assume a Queue object
        q = []
        self.__inorder(self.root, q)
        return q

    def __inorder(self, node, q):
        if node == None:
            return
        self.__inorder(node.left, q)
        q.append(node.key)
        self.__inorder(node.right, q)


#Breadth first search - level order traversal
    def bfs(self):

        if(self.root is None):
            return None

        q = []
        q.append(self.root)
        while(len(q) > 0):
            curr_node = q.pop(0)

            print(curr_node.key)

            if(curr_node.left != None):
                q.append(curr_node.left)

            if(curr_node.right != None):
                q.append(curr_node.right)

        return


#delete operations

    def delMin(self):
        self.root = self.__delMin(self.root)

    def __delMin(self,node):
        if(node.left is None):
            return node.right

        node.left = self.__delMin(node.left)
        node.count = 1 + self.size(node.left) + self.size(node.right)
        return node


    def delMax(self):
        self.root = self.__delMax(self.root)

    def __delMax(self,node):
        if(node.right is None):
            return node.left

        node.right = self.__delMax(node.right)
        node.count = 1 + self.size(node.left) + self.size(node.right)
        return node


    #Hibbard deletion - delete a particular key k
    # 3 cases - no child | 1 child | 2 child*
    def delete_key(self,key):
        self.root = self.__delete_key(self.root,key)

    def __delete_key(self,node,key):

        if(node is None):
            return None

        if(node.key < key): #move to right
            node.right = self.__delete_key(node.right,key)

        elif(node.key > key): #move to left
            node.left = self.__delete_key(node.left,key)
        else:
            if(node.left is None):
                return node.right
            if(node.right is None):
                return node.left

            tmp_node = node
            node = self.find_min(tmp_node.right) #no particular reason for going right
            node.right = self.delMin(tmp_node.right)
            node.left = tmp_node.left

        node.count = 1 + self.size(node.left) + self.size(node.right)
        return node
