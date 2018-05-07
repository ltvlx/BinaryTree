class TreeNode:
    def __init__(self, x):
        self.v = x
        self.l = None
        self.r = None

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = TreeNode(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = TreeNode(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = TreeNode(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)


    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None


    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)


    def _printTree(self, node):
        if node != None:
            self._printTree(node.l)
            print(str(node.v), end='-')
            self._printTree(node.r)


    def printTreeLevel(self):
        tree_list = self.getTreeAsList()
        current = 0
        for i in range(self.getLen()):
            for j in range(current, current + 2**i):
                val = '_' if tree_list[j] == None else tree_list[j]
                print(val, end=' ')
            current += 2**i
            print()


    def getTreeAsList(self):
        size = 0
        for i in range(self.getLen()):
            size += 2**i
        res = [None] * size
        return self._getTreeAsList(self.root, 0, res)


    def _getTreeAsList(self, node, i, res):
        if node == None:
            return res
        else:
            res[i] = node.v
            self._getTreeAsList(node.l, 2*i+1, res)
            self._getTreeAsList(node.r, 2*i+2, res)
            return res


    def getLen(self):
        return self._getLen(self.root, 0)


    def _getLen(self, node, length):
        if node == None:
            return length
        else:
            length += 1
            return max(self._getLen(node.l, length), self._getLen(node.r, length))


#     3
#   0    5
#    1  4 8
#     2
tree = Tree()
tree.add(3)
tree.add(5)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(1)
tree.add(2)
print(tree.getTreeAsList())
tree.printTreeLevel()

