class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self,val):
        if(self.root==None):
            self.node = Node(val)
        else:
            self._add(val,self.root)

    def _add(self,val,node):
# add node to left if the new node value is smaller then current value
        if(val < node.v):
# if the left node is not empty, we can add a new node as current node's left node
            if(node.l != None):
                self._add(val,node.l)
# if the left node is empty, then the new node is current node's left node
            else:
                node.l = Node(val)
# add node to rightif the new node value is bigger then current value
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
# found the node!
        if(val == node.v):
            return node
# the search val is smaller then current node so check the left node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
# the search val is bigger then current node so check the right node
        elif(val > node.v and node.r !=None):
            self._find(val, node.r)
    def deleteTree(self):
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)

if __name__ == "__main__":
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    tree.printTree()
    #print((tree.find(8)).v)
