# DAY-49   MAXIMUM POINT   LEAT CODE -1423 
# FIND THE MAIXMUM POINT (COUNT) FORM FRONT THREE ELSE LAST THREE 

# LOGIC --> YA TO AAAGE KE K KA SUM YA END SE OR YA AAGE KA EK BKI END ME SE LE LEO 

# USING DICT()

def max_point(nums,k):
    n=len(nums)
    left_sum=0
    right_sum=0

    if n==k: # agr k n ke equla hua to whole arr ka sum dena hoga 
        return sum(nums)

# loop front ko ck krne ke liye 
    for i in range (0,k):
        left_sum+=nums[i]

    maxi=left_sum # left ke sum ko hi max man lege phle 


    right_index=n-1 # right index n -1 se start 

# loop for right (end vale ke liye reverse loop )
    for i in range (k-1,-1,-1):
        left_sum-=nums[i]
        right_sum+=nums[right_index]
        maxi=max(maxi,left_sum+right_sum)

        right_index-=1
    return maxi 



nums=[1,2,3,4,5,6,7,1]
k=3

print(max_point(nums,k))   #o/p= 14         

# Time and complexcity = O(N)    S.C=O(1)