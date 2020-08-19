class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    print(root.info, end=" ")
    higherLeaf(root, root.info)

def higherLeaf(node, value):
    leaf = None
    if node.left != None:
        if node.left.info > value:
            leaf = node.left
            value = node.left.info
            print(node.left.info, end=" ")
            
    if node.right != None:
        if node.right.info > value:
            leaf = node.right
            value = node.right.info
            print(node.right.info, end=" ")
    
    if leaf != None:
        higherLeaf(leaf, value)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)