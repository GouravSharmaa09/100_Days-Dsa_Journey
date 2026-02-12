# DAY-40      N-QUEEN PROBLEM [BACKTRACKING]
# NxN KE BOARD PE QUESSN KO PLACE KRO ESE KI DUSRI QUEEN DONT CUT SAME ROW , DIAGONALLY AND SAME COLUMN 

# Logic - Using safe functionn(phle chk kre ge ki ky possiblity hai queen place hai ya nhi (back me hi chk krege kyuki aage to queen phuchi nhi hogi ))

# Method -1   Brute force (Safe function (while loop lga k sbke ke liye chk krna ))


# recursion call fun 
def solve (col,board,result,n):
    if col == n : # agr hr column me queen aagyi to 
        result.append(["".join(row)for row in board]) # append in list all row s 
        return 
    
    # loop every row ke liye queeen chk krega
    for row in range (n):
        # safe function ko call kiya 
        if safe(col,row,board,n):
            # board me row or col me queen daalo 
            board[row][col]="Q"
            # backtrack 
            solve(col+1,board,result,n)
            # remove hogi queen or . lga di 
            board[row][col]="."

# chk krega fun queen ko 
# row , upper diagonal , lower diagonal 
def safe(col,row,board,n):
    temp_row,temp_col=row,col # duplication var bnaya 
    
    # dir to row 
    while temp_col >=0:
        # agr queen mili to false bolo else - krte jao 0 tk keliye 
        if board[temp_row][temp_col]=="Q":
            return False
        temp_col -=1

    temp_row,temp_col=row,col    
    
    # dirc upper diaganoal 
    while temp_col>=0 and temp_row>=0 :
        if board[temp_row][temp_col]=="Q":
            return False
        temp_col-=1
        temp_row-=1

    temp_row,temp_col=row,col    
   
    # dirc lower left diaggonal 
    while temp_col >=0 and temp_row <n :
        if board[temp_row][temp_col]=="Q":
            return False
        temp_row +=1 # isme row bdegi or col decreasee hoge 
        temp_col-=1        

    
    return True                         


def N_queen(n):
    board=[["." for _ in range(n)] for _ in range (n)]   # board bnaya NxN ka . se bhr ke 
    result=[]

    solve(0,board,result,n)

    return result



print(N_queen(4))


# Output=[['..Q.', 'Q...', '...Q', '.Q..'], ['.Q..', '...Q', 'Q...', '..Q.']]


# Time and complecity = O(N! * N) --> N! isliye ki  hr queen ke liye solution hai  and N while loops ka jo ek ek krke sbse ke liye safe fun chk kr rha hai 
# S.C = O(N^2)




# Method - 2 Optimal  (Using Hash_map )




def N_queen_optimal(n):
    result=[]
    board=[["." for _ in range (n) ] for _ in range (n)]
    
    #Hashing arrays (pre store krli inki values hashing krke )
    left_row = [0]*n
    lower_diagonal=[0]*(2*n-1)
    upper_diagonal=[0]*(2*n-1)


   
    def solve(col):
     if col==n : # sab col me queen hai to append kro 
        result.append(["".join (row)for row in board])
        return 

    # try each row at every current index  
     for row in range (n):
        # every ke liye chk kro safe hai ya nhi attck kr rhi ahi quee ya nhi 
        if left_row[row]==0 and lower_diagonal[row+col]==0 and upper_diagonal[(n-1)+(col-row)]==0:
           
           # queen rhko hash_mark kro update kro =1
            board[row][col]="Q"
            
            left_row[row]=1 # row number chk krta hai isme 1 kr rhe hai 
            
            lower_diagonal[row+col]=1 # lower diagonal on board hmesha ro+col cnstant hota hai 
            
            upper_diagonal[(n-1)+(col-row)]=1 # Diagonals jo upar se niche jate hain, unka col - row constant rehta hai. hume positive index chyiye to n-1 

            solve(col+1)

            # bcktrack 
            board[row][col]="."
            left_row[row]=0
            lower_diagonal[row+col]=0
            upper_diagonal[(n-1)+(col-row)]=0
    
    solve(0)
    return result

print(N_queen_optimal(5))

# Output=[['Q....', '...Q.', '.Q...', '....Q', '..Q..'], ['Q....', '..Q..', '....Q', '.Q...', '...Q.'], ['..Q..', 'Q....', '...Q.', '.Q...', '....Q'], ['...Q.', 'Q....', '..Q..', '....Q', '.Q...'], ['.Q...', '...Q.', 'Q....', '..Q..', '....Q'], ['....Q', '..Q..', 'Q....', '...Q.', '.Q...'], ['.Q...', '....Q', '..Q..', 'Q....', '...Q.'], ['....Q', '.Q...', '...Q.', 'Q....', '..Q..'], ['...Q.', '.Q...', '....Q', '..Q..', 'Q....'], ['..Q..', '....Q', '.Q...', '...Q.', 'Q....']]

# Time and complexcity = O(N! * 1)
# S.C= O(N)