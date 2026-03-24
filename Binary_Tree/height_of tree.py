# DAY-54  HEIGHT OF A BINARY TREE 
# METHOD -1 USING DFS (DEPTH SEARCH )
class Node:

# create nodes 
  def __init__(self,val):
    self.val=val
    self.left=None
    self.right=None
      

def dfs(node):
     if node ==None :
        return 0
   # left height and right height 
     left_height=dfs(node.left)
     right_height=dfs(node.right)
#  (dono me se max le ke current node ko +1 kro )
     return 1+max(left_height,right_height)    

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
print(dfs(node))

# --- Tree Structure ---
#      1      <- Height 3
#     / \
#    2   3
#   /
#  4




# Method - 2 Using BFS (Breath search )

from collections import deque

def bfs(node):
    queue=deque() # o(1) operations perform ke liye ek hi jgh se  
    height=0
    queue.append(node)

    while len(queue)!=0: # queue empty nhi hai to 
        level_size=len(queue) # level size bnao jitni height queue ki hai utne 
        height+=1 # and height ko increase kro +1

        for _ in range (level_size): # level size pe (no. element in a queue pe loop chlo )
            e=queue.popleft() 
            if e.left is not None:
                queue.append(e.left)

            if e.right is not None:
                queue.append(e.right)

    return height 



node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.right.right = Node(9)

print(bfs(node))        

# --- Tree Structure ---
#      1      <- Level 1
#     / \
#    2   3    <- Level 2
#   /     \
#  4       9  <- Level 3

# T.C=O(N) AND S.C=O(N)