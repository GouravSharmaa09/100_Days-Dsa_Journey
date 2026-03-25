# DAY-56 RIGHT SIDE VIEW LEATCODE-199
# LEVEL SIZE JITNA LOOP ITERATED KREGE AND LAST JO ITERATE HOGA USKO PRINT KRGEGE 

# USING bfs

def bfs(node):
    queue=deque()
    result=[]
    queue.append(node)

    while len(queue)!=0:
        level_size=len(queue)

        for i in range (level_size): # LEVEL SIZE JITNA LOOP CHLAO 
            node = queue.popleft()

            if i==level_size-1: # AGR I LEVEL SIZE JITNA HOJYE TO APPEND KRDO result me node ki val 
                result.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
    
    return result





# USING DFS             

def dfs(node,level,ans):
    if node is None:
        return 
    
    if len(ans)==level: # agr ans and level size equal ho 
        ans.append(node.val)# append the val of node 

    if node.right:
        dfs(node.right,level+1,ans)

    if node.left:
        dfs(node.left,level+1,ans)

def rightSideViewDFS(root):    
    ans=[]
    return ans


    dfs(node,0,ans)
    

# T.C=O(N),S.C=O(N)                