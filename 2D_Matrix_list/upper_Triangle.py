# Pattern - Upper triangle using 2d matrix 



nums = [[5,20,3],[7,-10,9],[1,-52,6]] 

# Output= 5 20 3 
#         * -10 9 
#         * * 6 


rows = len(nums)
cols= len(nums[0])

for i in range (0,rows):
    for j in range (0,cols):
        if j>=i:
            # Upper triangle logic me colum ka index j hmesh i se greather than ya equal hota hai isliye ye logic lgya 
            print(nums[i][j], end=" ")
            
        else:
            print("*",  end=" ")
    print()  



# Lower Triangle 

nums = [[5,20,3],[2,-9,0],[1,-52,6]] 

# Output =5 * * 
#         2 -9 * 
#         1 -52 6 


rows = len(nums)
cols= len(nums[0])

for i in range (0,rows):
    for j in range (0,cols):
        if j<=i:
            # Lower triangle  logic me colum ka index j hmesh i se less than ya equal hota hai isliye ye logic lgya 
            print(nums[i][j], end=" ")
            
        else:
            print("*",  end=" ")
    print()  

    
