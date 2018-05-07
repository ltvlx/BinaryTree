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

    def MakeFromList(self, t_list):
        assert len(t_list) > 0
        size = 0
        i = 0
        while size < len(t_list):
            size += 2**i
            i += 1
        t_list += [None] * (size - len(t_list))
        
        self.root = TreeNode(t_list[0])
        self._MakeFromList(self.root, t_list, 0)

        return

    def _MakeFromList(self, node, t_list, i):
        node.val = t_list[i]
        # print(i, t_list)
        if (2*i + 1) < len(t_list):
            if t_list[2*i + 1] != None:
                node.l = TreeNode(t_list[2*i + 1])
                self._MakeFromList(node.l, t_list, 2*i + 1)
            if t_list[2*i + 2] != None:
                node.r = TreeNode(t_list[2*i + 2])
                self._MakeFromList(node.r, t_list, 2*i + 2)
        return


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans

            


# tree = Tree()
# a = [3, 0, 5, None, 1, 4]
# tree.MakeFromList(a)
# print(tree.getTreeAsList())
# tree.printTreeLevel()
t1 = Tree()
t1.MakeFromList([1,3,2,5])
print(t1.getTreeAsList())
t1.printTreeLevel()

print()
t2 = Tree()
t2.MakeFromList([2,1,3,None,4,None,7])
print(t2.getTreeAsList())
t2.printTreeLevel()
# t2 = Tree().MakeFromList([2,1,3,None,4,None,7])

