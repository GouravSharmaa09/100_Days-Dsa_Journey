# DAY-53  BFS (LEVEL BY LEVEL )


from collections import deque # DEQUE IMPORT KRNE KE LIYE
class Node:

  def __init__(self,val): # NODE CREATE KIYA 
     self.val=val
     self.left=None
     self.right=None



def levelorder(root): 
    result=[]
    queue=deque()  # EK HI JGH SE PUSH POP KRNE KE LIYE 
    queue.append(root) # QUEUE ME ROOT NODE DAALA 

    while len(queue)!=0: # QUEUE  EMPTY HONE TK 
        e=queue.popleft() # POP KRO 
        result.append(e.val) # RESULT ME E KI VAL INSERT KRO 

        if e.left is not None: # AGR LEFT HAI TO APPEND IN QUEUE 
            queue.append(e.left)

        if e.right is not None:
            queue.append(e.right)

    return result

root = Node(5)
root.left = Node(1)
root.right = Node(9)
root.left.left = Node(4)    

print(levelorder(root))   # [5, 1, 9, 4] 


# T.C=O(N)  AND S.C=O(N)
