# DAY-55 MAXIMUM PATH SUM (LEAT CODE -124)
#Instituiton = Max variable leke chlege globally -recusively height chk krege kiski max hai
class Node:
    # Node intialize 
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class solution:
    def maxi_sum(self,node): # global maxi variable jo count trak krega 

        self.maxi=float("-inf")

        def dfs(node):
            if node is None:
                return 0

            LH=dfs(node.left) # left subtree 
            if LH<0: # agr negative milta hai then 0 return kro 
                LH=0
            
            RH=dfs(node.right)
            if RH<0:
                RH=0

            self.maxi=max(self.maxi,LH+node.value+RH) # maximum btao left + right + root 
            return node.value+max(LH,RH) 

        dfs(node)
        return self.maxi

node = Node(1)
node.left = Node(8)
node.right = Node(10)
node.left.left = Node(4)
node.right.right=Node(6)
sol=solution()
print(f"ye rha max sum :{sol.maxi_sum(node)}")  # ye rha max sum :29

# T.C= O(N),  S.C=O(H)


