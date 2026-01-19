# DAY=17
# Problem - 48 = ROTATE MATRIX BY 90 IN PLACE 


# METHOD 1 - BRUTE FORCE (USING EXTRA SPACE (RESULT[]))
# Time and complexcity = O(N^2)
# SPACE COMPLEXCITY = O(N^2)--- result ke vhj se 


matrix= [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# Output= [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

n=len(matrix)
result=[[0 for _ in range (n)]for _ in range (n)]
#  result ko 4x4 ka bnane ke liye or 0 bhrne ke liye [list comperstion ka use kiya hai ]

for i in range (n):
    for j in range(n):
        result[j][(n-1)-i]= matrix[i][j]
        #  formula hai j to same hai logic ,me but i hrdm n-1-i  hora hai ye square matrix ke liye hai formulla means 2x2 ki 4x4 ki 8x8 ki etc 

print(result)    
                           
               # METHOD 2 - OPTIMAL SOLUTION (USING TRANSPOSE OF MATRIX AND REVERSE )
         # 1.1- TRANSPOSE KREGE MATRIX KA 
         # 1.2- MATRIX[I] PE LOOP CHLAKE EVERY LIST KO REVERSE KRDEGE (INPLACE KE LIYE O(1)KE LIYE )

                # TIME AND COMPLEXCITY =O(N^2) AND SPACE COMPLEXCITY =O(1)

#  First hum matrix ka Transpose kiya hai then Matrix[i] ko reverse 
        # i=0, j=1,2,3
        # i=1, j=2,3
        # i=2, j=3      Transpose ese hoga jo column hai vo row bnegi 

matrix= [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# Output = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

n=len(matrix)

for i in range (0,n-1):
    #  IN THIS LOOP I 0 SE START HOGA OR N-1 MEANS 2 TK HI JA RHA 4 KI MATRIX ME 
    for j in range (i+1,n):
        #  IN THIS LOOP J I+1 SE START HOTA HAI OR N MEANS 3 TK JATA HAI 4 KI MATRIX ME 
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #  SWAP THE ELEMENTS (TRANSPOSE THE MATRIX )

# THIS LOOP FOR MATRIX INNER LISTS 
for i in range (0,n):
    #  MATRIX KI ROWS KO REVRSE KRO 
    matrix[i].reverse()

print(matrix)            