# DAY-33   FIND THE POWER SUBSET OF ALL (ALL POSSIBLE SUBSET FIND KRO LIST KE ) LEATCODE= 78

# Method 1 Using Bit manipulation (WITHOUT RECURSION )
# logic - total max subset gernate = 2^n  
# BIT agr 1 hai to pick kro 0 hai to not pick  


def find_subset(num):
    n=len(num)
    result=[]
    # left shift
    total_subset=1<<n  # total possible subsets 2^n but hume bitwise me left shift kiya 
     
    for i in range (0,total_subset) : # loop total possible subsets create krne ke liye (8)hoge is case me 
        lst=[] # subset ko store krne ke liye lst
        
        for j in range (0,n): # loop for indexing and bit chk ke liye 
            
            if i & (1<<j)!=0: # check kiya ki last bit set hai ya nhi beacuase  left shift kr rhe hai to "1" pe pick and "0"pe not pick  
                
                lst.append(num[j]) # append subsets in the lst 

        result.append(lst) # result list me lst store ki 
    
    return result

print(find_subset([1,2,3]))

# O/P=[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# Time and complexcity = O(N*2N),  S.C=O(2N*N)


#Dry run
# 2^n== input num diye 3 bit ke to ----> 2^3=8 to 8 subset bne 
# Binary (i),"Bits (j=2, j=1, j=0)",Subset Elements
# 0 (000),Sab '0' hain,[] (Empty)
# 1 (001),Sirf 0th bit '1' hai,[1]
# 2 (010),Sirf 1st bit '1' hai,[2]
# 3 (011),0th aur 1st bit '1',"[1, 2]"
# 4 (100),Sirf 2nd bit '1' hai,[3]
# ...,...,...
# 7 (111),Saari bits '1' hain,"[1, 2, 3]"






