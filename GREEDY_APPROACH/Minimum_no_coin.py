# DAY-50 MINIMUM NO. OF COINS 

# N? FIND KRNA HAI COIN ME SE NUMBER DUPLICATE BHI LE SKTE HAI 
# LOGIC = Revrse iterate krke compare krkege 


def MINIMUM_coin(coins,k):
    n=len(coins)
    result=[]

    for i in range (n-1,-1,-1): # REVERSE LOOP 
        
        while  k>=coins[i]: # AGR K GREATER HAI COINS I SE TO 
            result.append(coins[i]) # APEEND KRO 
            k-=coins[i] # OR K KI VAL K  KRO JO APPEND KI HAI US SE 
    return result 


coins=[1,2,4,5,6,77,88,43,55]
k=47 

print(MINIMUM_coin(coins,k))  # [43, 4] output 

# T.C= O(N)   S.C=O(1)


