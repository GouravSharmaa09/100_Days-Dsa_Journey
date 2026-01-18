# Problem -73 = SET MATRIX ZERO  (IN THE MATRIX AGR KISI BHI ROW YA COLUMN ME ZERO AATA HAI TO US ROW AND COLOUM KO ZERO KRDO )

# METHOD 1 - BRUTE FORCE (USING INFINITY LOGIC )
# TIME AND COMPLEXCITY = 0(N+M)*(N*M)+O(N*M)= O(N*M)

# # This Function for infinity krne ke liye 0 vali row or colms ko 
def matrix_infinity(matrix,rows,cols):
    r=len(matrix)
    c=len(matrix[0])
    
    #  IS VALE NE O(N+M) DI HAI 
    for i in range (0,r):# 0(N)
        # loop for rows in this cols are constant and loop are iterated on rows 
        if matrix[i][cols]!=0:
            #  matrix row ke col index ko infinity kro agr 0ke equal nhi hai to 
            matrix[i][cols]=float("inf")
    
    for j in range (0,c):#O(M)
        #  loop for column in this row are constant 
        if matrix[rows][j]!=0:
            matrix[rows][j]=float("inf")
            
            # function for convert infinity to zeros 
def set_zero(matrix):
    r=len(matrix)
    c=len(matrix[0])
    
    for i in range (0,r):# O(N*M)
        for j in range (0,c):
            #  agr row or column ka index equal hai zero ke to infinity vale func(call) kro 
            if matrix[i][j]==0:
                matrix_infinity(matrix,i,j)
                #  infinty fun call 
                
                
    for i in range (0,r):#O(N*M)
        for j in range (0,c):
            #  agr euqal hai infinty ke to !
            if matrix[i][j]==float("inf"):
                matrix[i][j]=0
                #  0 krdo values ko row and col ki 
                
                
my_matrix = [[1,1,1], [1,0,1], [1,1,1]]
# Output = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
set_zero(my_matrix)
print(my_matrix)          
                
        
             



# OPTIMAL SOLUTION  - (USING ROW_TRACKER AN COLUMN_TRACKER)
# Time and complexcity = O(n*m)(n*m)= 0(N*M)
# S.C= O(1)

matrix= [[1,1,0,2],[2,2,3,0],[1,1,1,1],[0,1,0,9]]

# Output=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
r=len(matrix)
c=len(matrix[0])

row_track=[[0] for _ in range(r)]
#  Row tracker and column tracker bnaya jisme 0 elements add kiya then loop chlaya 
col_track=[[0] for _ in range(c)]

for i in range (0,r):
    for j in range(0,c):
        #  agr matrix me 0 mile to 
        if matrix[i][j]==0:
            row_track[i]=-1
            #  row track or col track ke us hi index pe -1 kro 
            col_track[j]=-1

#ye loop Row track ko col track ke -1 ko 0 me convert krega  
for i in range (0,r):
    for j in range (0,c):
        if row_track[i]==-1 or col_track[j]==-1:
            matrix[i][j]=0 

print(matrix)            






