# Day-15  Transpose of Matrix   -[Row ka column me convert hona hi hai iska mtlb ]

# I have and (2x3) Matrix  After the transpose of matrix it will (3x2) matrix 


nums= [[5,9,1],[2,3,7]]

# output = [[5, 2], [9, 3], [1, 7]] 


rows=len(nums)
cols=len(nums[0])
result=[[0]*rows for _ in range (cols)]
#  list comperstion hai ye  ye line 2 khali rows bnyegi or usko 3 baar repeate krege (0,0), (0,0)

for i in range (0,rows):
    for j in range (0,cols):
        result[j][i]= nums[i][j]
print(result)         