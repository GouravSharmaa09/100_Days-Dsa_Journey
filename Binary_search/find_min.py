            #   DAY-25-  FIND MINIMUM IN SORTED ROTATED ARRAY 


# Method-1     Brute force 
# 
nums=[4,5,6,7,0,1,2]
n=len(nums)
mini=float("inf")

for i in range (0,n):
    mini=min(mini,nums[i])

print(mini)    # O/p=0,   T.C=O(N)




# Method -2  Optimal Using binary search 


def min_find(nums):   # T.C=O(logn)
    n=len(nums)
    mini=float("inf")
    low,high=0,n-1

    while low<=high:
        mid=(low+high)//2
        if nums[mid]<=nums[high]: # agr mid less than or euqal hai high ke to ye part sorted hai mini find krlo isme agr sorted hai to mid hi min hoga to mini ko mid ki value se update kro 
            mini=min(mini,nums[mid])
            high=mid-1    #or high ko mid -1 kro opposite side find krne ke liye or koi mini remaining hai to 
        else: # oppsite side ke liye low min hoga 
            mini=min(mini,nums[low])
            low=mid+1
# ek edge case bhi add kr skte hai agr puri array sorted hogi to usme low ko mini manege 
    return mini 

nums=[7,8,9,1,2,3,4,5,6]  #O/p=1

print(min_find(nums))
           