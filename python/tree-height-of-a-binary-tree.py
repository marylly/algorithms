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
def height(root):
    nodes = arr
    root = int(root.__str__())
    height = 0
    processados = []
    quant_nodes = len(nodes)

    print("tipo array", type(arr))
    for i in arr:
        print(type(i))

    if quant_nodes > 1:
        node_menor = nodes.index(root)
        index_direita = 0
        index_esquerda = 0
        # while node not in processados:
        #     node_menor = nodes.index()
        print("node menor", node_menor)






        # for node in nodes:
        #     if node == root:
        #         node_menor = node
        #         height = height + 1

        #     if node_menor > node:
        #         height = height + 1
        #         node_menor = node              
    return height

# def height(root):
#     nodes = arr
#     root = int(root.__str__())
#     height = 0
#     if len(nodes) > 1:
#         node_menor = 0
#         for node in nodes:
#             if node == root:
#                 node_menor = node
#                 height = height + 1

#             if node_menor > node:
#                 height = height + 1
#                 node_menor = node              
#     return height

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
