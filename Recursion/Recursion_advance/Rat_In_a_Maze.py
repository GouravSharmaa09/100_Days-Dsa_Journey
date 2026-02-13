# DAY-41   RAT IN MAZE PROBLEM  
# RAT KO EK NxN board me n-1,n-1 tk phuchana hai all possible rotes btane hai -(0 hai to rasta block hai )1 pe move kro 
# Rat hamesh  4 dircetion me move krega (Down, Left,Right,Up) ye hi lexigeogical order follow krega 


# Brute force logic using Every possibles dirction 

# path finding function (chk krega 4 dircetions me )
def find_path (row,col,a,n,vis,move,ans):
    #Base case 
    if row == n-1 and col==n-1: # agr rat destination pe phuch gya (n=4 to n-1=3   to 3,3 pe phuch gya )
        ans.append(move) # append kro dirction ko 
        return 
    
    
    # Downward try going downward (row+1)
    if row+1 <n and not  vis[row+1][col] and a[row+1][col]==1:
        # row n se greater na ho , vistied na ho , or route block na ho 
        
        vis[row][col]=1 # mark as visit 
        
        # call function for (recursion )
        find_path(row+1,col,a,n,vis,move+"D",ans)
        
        # bcktrack
        vis[row][col]=0 # mark as unvisited 

    
    # left ( try find routes via left move (col-1)) 
    if col-1>=0 and not vis[row][col-1] and a[row][col-1]==1:
        vis[row][col]=1

        find_path(row,col-1,a,n,vis,move+"L",ans)
        vis[row][col]=0  
 
    # right ( right move (col +1))
    if col+1<n and not vis[row][col+1] and a[row][col+1]==1:
        vis[row][col]=1

        find_path(row,col+1,a,n,vis,move+"R",ans)
        vis[row][col]=0      

    # upward  ( up move (row-1))
    if row-1>=0 and not vis[row-1][col] and a[row-1][col]==1:
        vis[row][col]=1

        find_path(row-1,col,a,n,vis,move+"U",ans)
        vis[row][col]=0  

# main fun 
def maze_fun(matrix):
    n=len(matrix)
    ans=[]
    vis=[[0 for _ in range (n)]for _ in range(n)] # visited (0) mark krne ke liye board bnana 

    if matrix[0][0]==1: #agr 0,0 pe 1 hai to rat aage nhi ja skta 
        find_path(0,0,matrix,n,vis,"",ans)
    
    return ans 

matrix=[
    [1,0,0,0],
    [1,1,0,0],
    [1,1,1,0],
    [0,1,1,1]
]

print(maze_fun(matrix))

# Output # ['DDRDRR', 'DDRRDR', 'DRDDRR', 'DRDRDR']

# Time and complexcity = O(4^m*n) --> 4 DIRC KE LIYE ALG ALG 
# S.C= O(N^2)





# Method - 2 (Optimal solution [using - directions arr me save krke ])
# LOGIC= Phle save krlo dirc ko then visit kro 


def find_Path2(row,col,maze,n,move,ans,vis):
    if row==n-1 and col==n-1: # base case destination mil gyi to 
        ans.append(move)
        return 
    
    # STORE THE DIRCETION 
    dirc=[
        (1,0,"D"), # DOWN WARD KE LIYE DIRC STORE KI TUPELS ME (ROW+1,COL,DIRC)
        (0,-1,"L"),# LEFT KE LIYE (ROW,COL-1,DIRC)
        (0,1,"R"), # RIGHT KE LIYE (ROW,COL+1,DIRC) 
        (-1,0,"U") # UP KE LIYE (ROW-1,COL,DIRC)
    ]

    #every row and col an move ke liye if condition lgane ki need nhi bdegi sbke liye chk rkega 
    for dr ,dc,  current in dirc:
        next_row,next_col = row+dr,col+dc

        if 0<=next_row<n and 0 <=next_col<n and maze[next_row][next_col]==1 and not vis[next_row][next_col]:
            #  boundary mai hai ya nhi , visit to nhi hai , and route to bnd nhi hai chk kro 

            vis[row][col]=True # mark visit
            find_Path2(next_row,next_col,maze,n,move+current,ans,vis) # maove + curret isliye ki dirc loop ke acc change hogi to parameter ka move an loop ka current dirc 
            
            # bcktrck   
            vis[row][col]=False # mark unvisited 

# maze func
def maze_fun(maze):
    n=len(maze)
    ans=[]
    vis=[[False for _ in range(n)]for _ in range (n)]   # NxN ka board bnaya 
    if maze[0][0]==0 or maze[n-1][n-1]==0: # agr 0,0 pe 0 hai or last 3,3 pe hai 
        return ans  # ans return kro 

    find_Path2(0,0,maze,n,"",ans,vis)
    return ans 
maze=[
    [1,0,1,1],
    [1,1,1,0],
    [1,1,1,0],
    [0,1,1,1]
]

print(maze_fun(maze))          

# ['DDRDRR', 'DDRRDR', 'DDRURDDR', 'DRDDRR', 'DRDRDR', 'DRRDDR', 'DRRDLDRR']

# Time and complexcity = O(3N^2)
# S.C- O(N^2)