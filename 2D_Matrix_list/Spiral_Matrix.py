# DAY-18 SPIRAL MATRIX 
# PROBLEM ON LEATCODE -54

# USING HELP OF 4 POINTER 

# Time and complexcity = O(n*m)


def spiral_matrix(matrix):
    n=len(matrix)
    result=[]
#  4 pointer left , top , right and bottom where right and left for coloumns and top and bottom for rows 
    left,top=0,0
    bottom,right=len(matrix)-1, len(matrix[0])-1
#  condition chk for cross over between pointers 
    while top<=bottom and left<=right :
        # Step-1   left to right   wheree top is constant amd i is not (chnage hora hai )
        for i in range (left,right+1):
            result.append(matrix[top][i])
            # top ne phli row print krvayi ab usko next pe behja +1
        top+=1
        # STEP-2 top to bottom where rigjht is constant 
        for i in range (top,bottom+1):
            result.append(matrix[i][right])
            #  right se reverse jyege right to left scan krne ke liyte isliye -=1
        right-=1
       
    #     ye condition chk krna jruri hai ye rows ki cross overs ko chk kregi ki single row to nhi thi or 
    # duplicates print nhi hone dete 
        if top<=bottom:
            #  loop for right to left but reverse isliye left-1 or -1 reverse ke liye 
            for i in range (right,left-1,-1):
                result.append(matrix[bottom][i])
                #  bottom constant hai idr or bottom km hota jyege top pe jane k liye 
            bottom-=1
#  ye condition  coloumns ko chk krege cross over to nhi huye or single col to nhi hai 
        if left<=right:
            #  loop bottom to top reverse 
            for i in range (bottom,top-1,-1):
                result.append(matrix[i][left])
                #  left increase hota rhega or left constant hai idr 
            left+=1

    return result

matrix=[[1,2,3],[4,5,6],[7,8,9]]
#  Output= [1,2,3,6,9,8,7,4,5]
print(spiral_matrix(matrix))                            



