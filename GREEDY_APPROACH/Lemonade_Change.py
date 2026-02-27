# DAY-50   LEMONADE CHANGE    LEATCODE-860
# 5 RUPYE KA LEMON HAI TRUE FALSE RETURN KRNA HAI CUSTUMER SATISFY HAI YA NHI 

def lemonade(bills):
    n=len(bills)
    five =0
    ten= 0

    for i in range (0,n): 
        if bills[i]==5:  # AGR 5 HAI TO FIVE +1 KRO 
            five+=1
        # AGR 10 HAI  TO 
        elif bills[i]==10:
        # FIVE CHK KRO PHLE DENE KE LIYE 
            if five>=1:

                five-=1
                # 10 KO + KRO 
                ten+=1
            else:
                 return False
        
        else:
         # 20 KE LIYE FIVE CHK KRO 1 OR 10 
            if five>=1 and ten>=1:
                five-=1
                ten-=1
            # YA PIR 3 5 CHK KRO 
            elif five>=3 :
                five-=3

            else:
                return False 

    return True 

print (lemonade([5,5,10,20]))                     #O/P=True

# T.C= O(N)   S.C=O(1)

    