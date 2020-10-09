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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  arrV1 = []
  arrV2 = []
  searchNode(root, v1, arrV1)
  searchNode(root, v2, arrV2)
  print(arrV1[0])
  print(arrV1[1])
  print("-------")
  print(arrV2[0])
  print(arrV2[1])
  nodes_list_1 = set(node.info for node in arrV1)
  intersection = [node for node in arrV2 if node.info in nodes_list_1]
  intersection = max(intersection, key=lambda x: x.info)
  return intersection

def searchNode(node, search, ancestor):
    if node:
        ancestor.append(node)

    if node.left:
        if node.left.info < search:
            searchNode(node.left, search, ancestor)

    if node.right:
        if node.right.info > search:
            searchNode(node.right, search, ancestor)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
