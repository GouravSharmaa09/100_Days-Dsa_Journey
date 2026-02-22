# DAY-48   FRUITS INTO THE BASKETS    LEAT CODE = 904
# ONLY 2 TYPE FRUITS ARE ALLOW FROM THE LIST TO COUNT BTANA HAI CONSUCATIVE 2 TYPES OF FRUITS KA 

# [3,3,3,2,2,3,1,1,4,1,4,2,2,2]    == 3, 2 CONSUCATIVE HAI TO COUNT 6 HONA CHYIYE 1,4, CONUCATIVE HAI BD VALA 2 COUNT NHI HOGA KYUKI VO CONSUCEIVE NHI  ME NHI HAI 

# METHOD - 1 BRUTE FORCE USING SET :

def fruits(nums):
    n=len(nums)
    maxi=0

    for i in range (0,n):
        my_set=set()  # SET KA LOOP (CHK KRNE KA )

        for j in range (i,n): # ADD KRNE KA LOOP EK EK ELEMNT KO 
            my_set.add(nums[j])

            if len(my_set)>2: # AGR LENGTH 2 SE JYDA (2 TYPE SE JYDA FRUITS CONSUCATIVE NHI HAI TO BREK )
                break

            maxi=max(maxi,j-i+1)
    return maxi 

print (fruits([3,3,3,2,2,3,1,1,4,1,4,2,2,2]))             # 6 

# T.C= O(N^2), S.C=O(3)= O(1)


#Longest Subarray with at most 2 unique elements

# Method - 2 optimal APPROACH  USING HASH_MAP(DICT) sliding window 

def fruits_optimal(nums):
    maxi=0
    left=0
    right=0
    n=len(nums)
    my_dict=dict()

    while right<n: # CROSS HONE TK 
        
        # CHK KREGA CURRENT INDEX KITNI BR AAYA (COUNT KREGA   )
        my_dict[nums[right]]=my_dict.get(nums[right],0)+1

# DIC KI LENGTH 2 SE JYDA HAI TO 
        if len(my_dict)>2: # WINDOW KA SIZE MAINTAIN RHEGA ISS SE KM JYDA NHI HOGA 
            # USIN THIS IF JITNA PHLE OUTPUT THA USSE JYDA CHK KRTE HAI (COUNT SE JYDA )
            # LEFT KO KM KRO 
            my_dict[nums[left]]-=1

# AGR LEFT 0 HOGA 
            if my_dict[nums[left]]==0:
                # DEL KRDO LEFT KO 
                del my_dict[nums[left]]
             
            left+=1

        if len(my_dict)<=2: 
            maxi=max(maxi,right-left+1)

        right+=1

    return maxi 


print(fruits_optimal([3,3,3,2,1,1,4,4,1,1,4,1,4,2,2,2]))     # 9 

# T.C = O(N), S.C =O(3)= O(1)