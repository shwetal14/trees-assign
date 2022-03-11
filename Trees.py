#!/usr/bin/env python
# coding: utf-8

# In[ ]:




   #  1.Implement Binary tree
    
    
class BinaryTree:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):

        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = BinaryTree(value)
                else:
                    self.left.insert(value)
            elif data > self.value:
                if self.right is None:
                    self.right = BinaryTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

root = BinaryTree(100)
root.insert(50)
root.insert(55)
root.insert(60)
root.insert(20)
root.insert(52)


root.PrintTree() 
    
    
    
    
    
   #   2.Find height of a given tree


class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Recursive function to calculate  height of a given binary tree
def height(root):
 
    
    if root is None:
        return 0
 
    return 1 + max(height(root.left), height(root.right))
 
 
  if __name__ == '__main__':
 
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
 
    print('The height of the binary tree is', height(root)


          

   #  3.Perform Pre-order, Post-order, In-order traversal
          
          


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def inorder(root):

    if root:
        
        inorder(root.left)
        print(str(root.val) + "->", end='')
        inorder(root.right)


def postorder(root):

    if root:
       
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->", end='')


def preorder(root):

    if root:
        
        print(str(root.val) + "->", end='')
        preorder(root.left)
        preorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)        
          
          
    
   # 4.Function to print all the leaves in a given binary tree
          
          
  
    from collections import deque
 
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
def isLeaf(node):
    return node.left is None and node.right is None
 
def printRootToLeafPaths(node, path):
 
    
    if node is None:
        return
 
    path.append(node.data)
 

    if isLeaf(node):
        print(list(path))
 
    printRootToLeafPaths(node.left, path)
    printRootToLeafPaths(node.right, path)
 
    path.pop()
 
def printRootToLeafPath(root):
 
    path = deque()
    printRootToLeafPaths(root, path)
 
 
if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)
    root.right.right.right = Node(9)
 
    printRootToLeafPath(root)
       
          

   # 5. Implement BFS (Breath First Search) and DFS (Depth First Search)
          
 
 # BFS (Breath First Search)  
          
          
     graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
          
bfs(visited, graph, 'A')     
          
  
   # DFS (Depth First Search) 
          
          
    graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() 

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search")
dfs(visited, graph, '5')      
          
          
          
          
    
   #  6.Find sum of all left leaves in a given Binary Tree
          
          
     class Node: 

    def __init__(self, key): 
        self.key = key 
        self.left = None
        self.right = None
   
def isLeaf(node): 
    if node is None: 
        return False
    if node.left is None and node.right is None: 
        return True
    return False
    
def leftLeavesSum(root): 
  
    # Initialize result 
    res = 0
       
    if root is not None:  
          
      if isLeaf(root.left): 
            res += root.left.key 
        else: 
             
            res += leftLeavesSum(root.left)  
            res += leftLeavesSum(root.right) 
    return res 
  
root = Node(20) 
root.left = Node(9) 
root.right = Node(49) 
root.right.left = Node(23)         
root.right.right = Node(52) 
root.right.right.left = Node(50) 
root.left.left = Node(5) 
root.left.right = Node(12) 
root.left.right.right = Node(12) 
print "Sum of left leaves is", leftLeavesSum(root)     
          
          
          
          
          
   #  7. Find sum of all nodes of the given perfect binary tree.
          
          
       class Node:  
    def __init__(self,data):  
        
        self.data = data;  
        self.left = None;  
        self.right = None;  
   
class SumOfNodes:  
    def __init__(self):  
         
        self.root = None;  
        
    def calculateSum(self, temp):  
        sum = sumRight = sumLeft = 0;  
           
        if(self.root == None):  
            print("Tree is empty");  
            return 0;  
        else:    
            if(temp.left != None):  
                sumLeft = self.calculateSum(temp.left);  
          
            if(temp.right != None):  
                sumRight = self.calculateSum(temp.right);  
              
            sum = temp.data + sumLeft + sumRight;   
        return sum;  
   
bt = SumOfNodes();    
bt.root = Node(5);  
bt.root.left = Node(2);  
bt.root.right = Node(9);  
bt.root.left.left = Node(1);  
bt.root.right.left = Node(8);  
bt.root.right.right = Node(6);  
    
print("Sum of all nodes of perfect binary tree: " + str(bt.calculateSum(bt.root)));  
          
          
          
          
    
   #  8.Count subtress that sum up to a given value x in a binary tree
          
          
      class Node:
    def __init__(self, data):
        self.node = data
        self.left = self.right = None

class defineCountSumSubtree:
    def countSubtreesSum(self,root, count, key):
            
        if ( root== None):
            return 0

        lsub =self.countSubtreesSum(root.left,count, key)
        rsub =self.countSubtreesSum(root.right,count, key)
        Sum = lsub + rsub + root.node
         if (Sum == key):
           count[0] += 1
        return Sum

# Recursive function to count subtrees that Sum up to a given key
    def countSubtreesSumRec(self,root, key):

     
        if ( root== None):
            return 0
        count = [0]


        lsub =self.countSubtreesSum(root.left,count, key)
        rsub =self.countSubtreesSum(root.right,count, key)
        if ((lsub + rsub + root.node) == key):
            count[0] += 1


        return count[0]

        
def main():

    dcs=defineCountSumSubtree()
    root = Node(10)
    root.left =Node(-4)
    root.right = Node(5)
    root.left.left =Node(6)
    root.left.right = Node(8)
    root.right.left = Node(-4)
    root.right.right =Node(10)
    print('Enter key value tofind sum of subtree:')
    x=int(input())
    count =dcs.countSubtreesSumRec(root, x)
    print("Count:",count)

if __name__ == "__main__":
    main()    
          
          
          

   #  9.Find maximum level sum in Binary Tree
          
          
       
from collections import deque


class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def maxLevelSum(root):

    if (root == None):
        return 0


     result = root.data


    q = deque()
    q.append(root)

    while (len(q) > 0):

        count = len(q)
        sum = 0
        while (count > 0):

           temp = q.popleft()

           sum = sum + temp.data

               if (temp.left != None):
                  q.append(temp.left)
               if (temp.right != None):
                  q.append(temp.right)
            count -= 1
         result = max(sum, result)
       return result
          
if __name__ == '__main__':

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)

print("Maximum level sum is", maxLevelSum(root))


   
    
   #  10.Print the nodes at odd levels of a tree



class newNode: 
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None
  
def printOddNodes(root, isOdd = True): 
      
      if (root == None):  
        return
   
    if (isOdd):  
        print(root.data, end = " ") 
   
    printOddNodes(root.left, not isOdd)  
    printOddNodes(root.right, not isOdd) 
    
if __name__ == '__main__': 
    root = newNode(1)  
    root.left = newNode(2)  
    root.right = newNode(3)  
    root.left.left = newNode(4)  
    root.left.right = newNode(5)  
    printOddNodes(root)

