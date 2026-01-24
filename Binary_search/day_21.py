# DAY-21     BINARY SEARCH 

# Binary search = List me mid find krke agr target small hai to left side iterate krgee else right side but condition hai arr sort ho 

# 1. using Iterated method 

# Time and complexcity = O(log2n) 

def binarysearch(nums,target):
    n=len(nums)

    low =0 # ek low pointer  start me 
    high=n-1 # high last me 

    while low<=high: # loop iterate kro high or low ke cross over hone tk 
        mid=(low+high)//2 # mid nikalo 

        if nums[mid]==target: # agr mid target ke == hai to mid ko return kro 
            return mid

        elif nums[mid]<target:
            low=mid+1  # else low = mid +1 hojyega agr mid target se chota hai to left side search krege 

        else:
            high= mid-1

    return -1         # agr target nhi mile to -1 return kro 

nums =[2,4,6,7,9,11,18,19]

# ans =4  9 4 index pe hai 

target=9            
print(binarysearch(nums,target))




# Method 2 -- Recursive method    Time and complexciy = O(log2n) and s.c = o(1)

def binarysearch_recursion (nums,low,high,target):
  # base case = agr low high se aage nikl gya to , mtlb target arr me hai hi nhi 
    if low>high:
        return -1

    mid=(low+high)//2  # mid nikalo 

    if nums[mid]==target:
        return mid # mil gya 

    elif nums[mid]<target:   #right side me find kro 
        return binarysearch_recursion(nums,mid+1,high,target)

    else:  # left me find kro 
        return binarysearch_recursion(nums,low,mid-1,target)


nums =[2,4,6,7,9,11,18,19]
# ans= 6     18- 6 index pe hai 
target=18
n=len(nums)

print(binarysearch_recursion(nums,0,n-1,target))
