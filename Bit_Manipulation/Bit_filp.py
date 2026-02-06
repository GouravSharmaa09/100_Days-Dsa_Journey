# DAY=33    COUNT MINIMUM BITS FLIP 

# LOGIC = XOR KRDO 2 BITS KA AND UNKA AND then jo set bit hogi vo hi count hoga flip ka 
#  USING XOR AND DECIMAL APPROACH


def count_flip(start,goal):
    ans = start ^goal  # XOR OF TWO NUMBERS 
    count=0

    while ans>0: # JB TK 0 NA AAYE REMINDER KRTE JAAO 
        if ans%2==1: # 1 HAI REMINDER TO 
            count+=1 # COUNT KO 1 KRO 
        ans=ans//2  # OR DIVIDE 2 KRTE JAO 

    return count     

print(count_flip(4,2))      #O/P=  2 --> BIT FLIP 

# Time and complexcity = O(log2N)


# Mehtod -2 Using left shift 

def count_flip2(start,goal):
    ans = start ^goal  # XOR OF TWO NUMBERS 
    count=0

    for i in range (0,32):  # total 32 bits hoti hai 
        if ans &(1<<i)!=0: # left shift and last vali bit chk krete agr 0 ke not equalhai to 
            count+=1 # count ko increase kro mtlb set hai bit 

        return count    

print(count_flip2(5,6))# ----> 1   bit flip 


# Time and complexcity = O(32)= o(1)  



