class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.result = []
    
    def insert(self, data):
        self.root = self.insert_value(self.root, data)
        return self.root is not None
    
    def insert_value(self, node, data):
        if node == None:
            node = Node(data)
        else:
            if data < node.data:
                node.left = self.insert_value(node.left, data)
            else:
                node.right = self.insert_value(node.right, data)
        return node
    
    def find(self, data):
        return self.find_value(self.root, data)
    
    def find_value(self, node, data):
        if node is None or node.data == data:
            return node is not None
        else:
    
            if data < node.data:
                return self.find_value(node.left, data)
            else:
                return self.find_value(node.right, data)

    def preOrder(self):
        self.result = []
        return self.re_preOrder(self.root)
    
    def re_preOrder(self, node):
        if node is not None:
            self.result.append(node.data) #추가
        if node.left is not None:
            self.re_preOrder(node.left)
        if node.right is not None:
            self.re_preOrder(node.right)
        return self.result
    
    def postOrder(self):
        self.result = []
        return self.re_postOrder(self.root)
    
    def re_postOrder(self, node):
        if node is None:
            return None
        if node.left is not None:
            self.re_postOrder(node.left)
        if node.right is not None:
            self.re_postOrder(node.right)
        self.result.append(node.data) #추가
    
        return self.result

    def inOrder(self):
        self.result = []
        return self.re_inOrder(self.root)

    def re_inOrder(self, node):
        if node is None:
            return None
        if node.left is not None:
            self.re_inOrder(node.left)

        self.result.append(node.data) #추가

        if node.right is not None:
            self.re_inOrder(node.right)

        return self.result

        
bst = BinarySearchTree()
data = [21, 14, 11, 18, 5, 12, 15, 19, 28, 25, 32, 23, 27, 30, 37]

for i in data:
    bst.insert(i)
for i in data:
    print(bst.find(i))
    
bst.preOrder()
bst.postOrder()
bst.inOrder()