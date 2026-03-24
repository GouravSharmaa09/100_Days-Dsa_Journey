# DAY-54   DIMAETER OF BINARY TREE (FIND THE MAX PATH )   LEATCODE= 543

#INSTITUTION = HIGHEST PATH BTANA HAI LIKE [ LH + RH ]

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class solution:
 def dia(self,node): # GLOBAL FUN FOR DIAMETER 
    self.diameter=0
   
    def dfs (node):
    
        if node==None:
            return 0

        left_height=dfs(node.left)    
        right_height=dfs(node.right)
            #            
            #  Diameter update karo (LH + RH)
            # Hum check kar rahe hain: Kya is node se guzarta hua path sabse bada hai
        self.diameter=max(self.diameter,left_height+right_height) #MAX DIAMETER NIKALNA HAI  

        return 1+max(left_height,right_height) # RETURN HEIGHT 

    dfs(node)
    return self.diameter

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.right.right=Node(5)

sol=solution()
print(sol.dia(node))

# Output: 4 (Path: 4 -> 2 -> 1 -> 3 -> 5)

# T.C=O(N)   S.C=O(H)