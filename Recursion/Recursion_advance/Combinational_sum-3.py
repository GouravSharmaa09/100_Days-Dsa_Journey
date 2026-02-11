# DAY-39     COMBINATIONAL SUM -3    leat code - 216
# IN THIS K AND N ARE GIVEN SO WE CAN CALCULATE THE SUM ACCOURDING TO K 
# k= len of digits and n = target(sum )


# Logic-- Ek for loop chlayege jo ki current index ke saare combination find krta hai 


# last yani 1 se hai kyuki question me given hai 1 to 9 tk ke sum find krne hai index ke jgh last bolege 
def solve(last,total,subset,k,n,result):
    if total==n and len(subset)==k: # AGR TARGET TOTAL KE EQUAL HAI AND SUBSET KI LENGTH BHI K KE EQUAL HAI TO APPEND KRDO ANS MILYA 
        result.append(subset.copy())
        return 
    
    # TOTAL TARGET SE JYDA HAI OR LEN BI JYDA HAI SUBSET KI K SE TO RETURN 
    if total > n or len(subset) > k :
        return 

    
    # LOOP FOR INCULE EVERY COMBINATION ON CURRENT INDEX 
    for i in range (last,10): # 10 ISLIYE QKI QUESTION ME 1 tO 9 NUMBERS KE LIYE KRNA HAI 
        sum=total+i # TOTAL KE I JOD DO 
        subset.append(i) # APPEND KRTE JANA HAI 
        
        solve(i+1,sum,subset,k,n,result) 

        # BACKTRACK 
        subset.pop()

def COMBINATIONAL_sum_3(k,n):
    result=[]
    solve(1,0,[],k,n,result)
    return result 


# NUMS KI JRURT NHI HAI KYUKI SEPCIFIC 1 TO 9 NUMBER KE LIYE KRNA HAI 
print(COMBINATIONAL_sum_3(2,7))

# Output = [[1, 6], [2, 5], [3, 4]]

# Time and complexcity = O(k *9k)
# S.C = O(k)
 
