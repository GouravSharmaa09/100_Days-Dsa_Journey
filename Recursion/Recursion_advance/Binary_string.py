# DAY-35    GERNATE "Binary Strings with no consecutive 1s"
# ASSENDING ORDER AND SEQUNCE ME BINARY STRING PRINT KRNE HAI ( "1" ke left ya right me "1"nhi hona chyiye )
# 2^n total subsets bnege 

# logic = strin me return krna hai (ya to "0", pick kro ya "1" kro , ek flag leke chelge "0" milne pe true retun krega and "1" milne pe false agr true hota hai to 1 print kr skte hai flase me nhi )

# flag_function jo string dega 
def binarystrings (index,flag,num,result):
    if index>=len(num):# last index base case 
        # string me chyiye ans and me ("0","1","0") type ans aayega to usko join krne ke liye ("010")
        result.append("".join(num)) 
        return
     
    # pick 0 first 
    num[index]="0" # 0 se start krege kyuki sequnce me chyiye ans 0 ko pick krege phle 
   # backtracking 
    binarystrings(index+1,True,num,result)
    
    # flag true hai to choice hai 1/0 ko  pick kro kyuki pichla charcter 0 tha 
    if flag==True:
        # pick 1 
        num[index]="1"
        # backtracking
        binarystrings(index+1,False,num,result) 
        # flase hai to choice nhi hai 0 hi pick krna pdega 
        num[index]="0"

def final_ans(n):  # ans fun cll 
    num=["0"]*n # num ki list ko string bnaya jitne n hai unse 
    result=[]
    binarystrings(0,True,num,result) # func cll 
    return result

print(final_ans(4))

#O/P= ['0000', '0001', '0010', '0100', '0101', '1000', '1001', '1010']


# Time and complexcity = O(2N),  S.C=O(N)