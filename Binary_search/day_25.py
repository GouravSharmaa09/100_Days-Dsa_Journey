#                       DAY-25- SEARCH IN  SORTED ROATATE ARRAY

# METHOD-1 BRUTE FORCE USING LINEAR SEARCH

nums=[8,7,1,2,3,3,3,4,5,6]   # o/p=3  , T.c= O(n)
n=len(nums)
target=2
index=-1
for i in range (0,n):
    if nums[i]==target:
        index=i
        break

    
print(index)



# Method-2 Binary search (optimal )   Leat code- 33 

# Logic - 1.Find the sorted part in the array 
#         2. then check in the sorted part target lies or not 


def search_index(nums,target): # Time and complexcity = O(logn)
    n=len(nums)
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target: # mid equal hai to mil gya return kro 
            return mid
        if nums[mid]<=nums[high]: # agr mid less thn hai to condition lgao kyuki arr sort hai yaha tk kyuki mid less than hai high se 
            if nums[mid]<=target<=nums[high]: # ki mid or high ke bich me target lie krta hai 
                low=mid+1
            else:
                high=mid-1
        else:
            if nums[low]<=target<=nums[mid]: # else low or mid ke bich me lie krta hai to target 
                high=mid-1
            else:
                low=mid+1
        
    return -1

nums=[11,9,8,7,1,1,1,2,2,3,4,5,6]

target=8 # o/p=2

print(search_index(nums,target))




# Q. Duplicates ke liye  binary search logic  Leatcode-81

# Note =  Dulicates huye to logic me change hai ek extra condition check krege low , high , or mid agr euqal hai to loop ko tb tk nhi chlayege jb tk koi single diff na hojye 

def search_dup_index(nums,target):  #Time and complexcity = Avg case -O(logn), Wrost case -O(n/2)
    n=len(nums)
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target: # mid equal hai to mil gya return kro 
            return True
        
        if nums[low]==nums[mid]==nums[high]: # duplicates ko remove kregi jb tk koi single diff na hojye 
            low+=1 # compare huye to low ko increane or high ko decrease krte jao 
            high-=1
            continue # continue isliye ki aage ka code jb tk run nhi hoga jb tk condition fail na ho 
        
        
        
        if nums[mid]<=nums[high]: # agr mid less thn hai to condition lgao kyuki arr sort hai yaha tk kyuki mid less than hai high se 
            if nums[mid]<=target<=nums[high]: # ki mid or high ke bich me target lie krta hai 
                low=mid+1
            else:
                high=mid-1
        else:
            if nums[low]<=target<=nums[mid]: # else low or mid ke bich me lie krta hai to target 
                high=mid-1
            else:
                low=mid+1
        
    return False

nums=[7,7,7,7,1,2,3,4,5,6,7,7]

target=2 # O/p=True

print(search_dup_index(nums,target))