# Day 15 
# PROBLEM Diagonal of triangle in 2d matrix 

# 1 Diagonal form left to right 

nums = [[5,20,3],[2,-9,0],[1,-52,6]] 
# O/P=   5 * * 
#        * -9 * 
#        * * 6 
rows =len(nums)
cols= len(nums[0])

for i in range (0,rows):
    for j in range (0,cols):
        if j==i :
            #  j==i beacuse in diagonal index of j and i are equal 
            print(nums[i][j],    end=" ")
        else:
            print("*",  end=" ")
    print()   




# 2. Diagonal form right to left              
nums = [[5,20,3],[2,-9,0],[1,-52,6]] 

# Output= * * 3 
#         * -9 * 
#         1 * * 

rows =len(nums)
cols= len(nums[0])

for i in range (0,rows):
    for j in range (0,cols):
        #  ye logic isliye hai kyuki i+j ka sum hmesha constant hai i increase hora hai j decrease but i+j ka sum always 2 hai jo ki matrix ke size ka -1 hai (rows-1)
        if i+j==rows-1:
            print(nums[i][j], end=" ")
        else :
            print ("*", end=" ")
    print()           



# using single loop sirf Diagonal print krne ke liye 
# 
#      

nums = [[5,20,3],[2,-9,0],[1,-52,6]] 

# output = 3 -9 1 

rows =len(nums)
cols=len(nums[0])

for i in range (rows):
    # smae formulla hai upr vala i+j==num-1   bs i ko = ke is trf likha hai 
    j=(rows-1)-i
    print(nums[i][j])
