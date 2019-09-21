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


    #RANK -> number of keys < given keys
    def rank(self, key):
        return self.__rank(key, self.root)

    def __rank(self, key, node):

        curr_count = 1
        if node == None:
            return 0
        if key < node.key:
            return self.__rank(key, node.left)
        elif key > node.key:
            #return 1 + self.size(node.left) + self.__rank(key, node.right)
            if(self.size(node.left) is not None):
                curr_count = curr_count + self.size(node.left)
            if(self.size(node.right) is not None):
                curr_count = curr_count + self.__rank(key,node.right)

            return curr_count
        else:
            return self.size(node.left)


    def size(self,node):
        if(node == None):
            return 0
        return node.count


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

        #node.count = 1 + self.size(node.left) + self.size(node.right)

        if(node.left is not None):
            node.count = node.count + self.size(node.left)
        if(node.right is not None):
            node.count = node.count + self.size(node.right)

        node.count = node.count + 1

        return node

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

    #find number of keys between two given keys
    def number_of_keys_in_range(self,low,high):
        if(self.contains(high)):
            return self.rank(high) - self.rank(low) + 1
        else:
            return self.rank(high) - self.rank(low)

    #find all keys between two given keys
    def one_d_search(self,low,high):

        result = []
        self.__one_d_search(self.root,low,high,result)
        print(result)
        return


    def __one_d_search(self,node,low,high,data=None):

        if(node is None):
            return

        if(node.key < low):
            self.__one_d_search(node.right,low,high,data)
        elif(node.key > high):
            self.__one_d_search(node.left,low,high,data)

        self.__one_d_search(node.left, low, high, data)
        self.__one_d_search(node.right, low, high, data)
        if node.key >= low and node.key <= high:
            data.append(node.key)
        #self.__one_d_search(node.right, low, high, data)
        return



root = BST.Node(1,1)
bst = BST(root)

bst.put(2,2)
bst.put(3,3)
bst.put(5,5)

#print(bst.rank(10))
#print(bst.number_of_keys_in_range(6,7))

print(bst.one_d_search(5,6))
