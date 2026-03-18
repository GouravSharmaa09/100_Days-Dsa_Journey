# DAY-53   Binary Tree   
# Topic= DFS (DEPTH FIRST SEARCH ) 

# T.C= O(N), S.C = O(H)

# 1. Preorder - [Root-left-right]
# [RLS]

class Node:

  def __init__(self,val):
     self.val=val
     self.left=None
     self.right=None

    


def Preorder(root):
    if root==None:
        return 

    print(root.val,end="  ")
    Preorder(root.left)
    Preorder(root.right)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
# --- Tree Structure ---
#      1
#     / \
#    2   3
#   /
#  4
Preorder(root)   # 1  2  4  3  


#2.POSTORDER [LEFT-RIGHT-ROOT] [LRR]


def postorder(root):
    if root==None:
        return 

    postorder(root.left)
    postorder(root.right)
    print(root.val)


root = Node(5)
root.left = Node(1)
root.right = Node(9)
root.left.left = Node(4)
# --- Tree Structure ---
#      4
#     / \
#    1   5
#   /
#  9
postorder(root)   # 4 1 9 5 


# 3. Inorder [left-root-right](lrr)

def inorder(root):
    if root==None:
        return 

    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)


root = Node(2)
root.left = Node(10)
root.right = Node(8)
root.left.left = Node(4)
# --- Tree Structure ---
#      4
#     / \
#    10   8
#   /
#  2


inorder(root)  # 4 10 2 8  


