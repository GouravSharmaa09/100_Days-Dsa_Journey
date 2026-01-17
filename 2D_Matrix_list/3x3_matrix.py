# Day_15   2d matrix / 2d lists 

# 3X3 matrix   

nums = [[5,20,3],[7,-10,9],[1,-52,6]] 
# output =  20 3 
# 7 -10 9 
# 1 -52 6 
rows = len(nums)
cols= len(nums[0])

for i in range (0,rows):
    for j in range (0,cols):
        print(nums[i][j], end=" ")
    print()        




