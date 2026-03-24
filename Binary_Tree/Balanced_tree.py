# DAY-54  CHECK BINARY TREE HEIGHT  IS BALANCED OR NOT[RETURN TRUE /FLASE ]

# IF [LH - RH] INKA DIFF KRNE PE (1) SE JYDA AATA HAI TO UNBALNCED HAI TREE KI HEIGHT 
# SEND -1 TO ROOT IF UNBALNCED    

class Node:
    def __init__(self,val):
        self.val=val
        self.left= None
        self.right=None

def solve(node):
    if node==None:
        return 0

    LH= solve(node.left) # left subtree ki height chk ki 
    if LH ==-1:
        return -1 # -1 send krdege upr if subtree me -1 mila to 

    RH= solve(node.right) # right subtree ki height chk ki 
    if RH ==-1:
        return -1

    if abs(LH-RH)>1: # balanced conition chk ki Difference 1 se zyada nahi hona chahiye 
        return -1# diff ek se jyda aane pe unblanced krdege 
    return 1+max(LH,RH)




node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.right.right=Node(5)

x=solve(node)

if x==-1:
    print( "False")

else:
    print("TRUE")     


# output =TRUE

# T.C=O(N)   AND S.C = O(H) -> H is the height of tree 