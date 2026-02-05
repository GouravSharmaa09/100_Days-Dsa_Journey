# DAY-32    CHECK IF THE KTH BIT IS SET OR NOT (index pe 1 set hai ya nhi ck krna hai or true or flase return kro )


# USING LEFT SHIFT

def chk_bit_1(n,k):
    if n & (1<<k) !=0: #  1 ko k time left shift kro or compare kro ki not equal to 0 ho 
         return True
    

    return False     

print(chk_bit_1(4,1))
# O/P=False

# T.C=O(1)

# 2. USING RIGHT SHIFT 

def chk_bit_2(n,k):
    if (n>>k) & 1==1: # n ko hi right shift kro k time and last bit chk kro 1 ke equal hai to true 
        return True
    return False

print(chk_bit_2(6,2))        
#  O/p = True




# Set the Bit ka Code  set krne me or use hota hai kyuki ye 0 ,1 pe 1 deta hai 

def set_kth_bit(n, k):
    return n | (1 << k)

print(set_kth_bit(3,1))    