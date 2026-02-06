# DAY-33    FIND THE SINGLE NUMBER WITHOUT DUPLICATES      LEATCODE-136

# Method-1 Brute force (using hash_map)

# Logic- hash_map lo or usme values store kro dekho kon kitni baar aaya hai 

nums=[5,4,1,3,3,2,1,2,6,6]  # O/P--> 5 ,4


n=len(nums)
hash_map=dict()
for i in nums :
    hash_map[i]=hash_map.get(i,0)+1      # insert krega dic me values ko with frequency  


for key in hash_map:  # check krega jo 1  bar aaya usko return kro 
    if hash_map[key]==1:
        print( key)

    # Time and complexcity = O(N), S.C=O(N)    




# Method - 2 Optimal approach using Xor operation 
# logic - agr same ka xor kro to result 0 hota hai to list me unique item hi found hoga 

def xor(nums):
    ans = 0
    for i in nums:
        ans=ans^i # perticular item ka xor krege baar baar to duplicates jo honge vo zero hojyege and end me unique mila 
    return ans 

print(xor([2,3,3,2,4]))     #  O/P--> 4 

# Time and Complexcity = O(1),S.C=O(1)

#Dry-run = xor op 
# 1. 0^2=2
# 2. 2^3==2^3
# 3. (2^3)^3 = 2^(3^3)= 2
# 4. 2^2 = 0 
# 5. 0^4=4 --> 4 is ans 
