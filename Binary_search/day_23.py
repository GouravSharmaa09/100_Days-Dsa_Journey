# DAY-23     
# SEARCH INSERT POSITION-- ARRAY ME TARGET FIND KRO OR USKA INDEX RETURN KRO ELSE RIGHT JGH LGAO 

# Method 1 - Brute force using linear search
 
#time and complexcity = O(n)

nums=[1,1,2,2,2,2,3,3,3,4,6,7,8,9]
n=len(nums)
target= 2

ans=n

for i in range (0,n):
    if nums[i]>=target:
        ans=i
        break  # break isliye ki aage loop na chle taregt milte hi bhar aajao 

print(ans)  #  ye kam krega arry me sbse bda element agr nhi hai to btyega index n 





# Method -2 Using binary search(lower bound logic )

# Time and complexcity =O(log2n)

#  same lower bound vala logic 
def search_insert(nums,target):
    n=len(nums)

    low=0
    high=n-1
    ans=n

    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            ans=mid
            high=mid-1
        else:

            low=mid+1
    return ans

nums=[1,2,4,4,4,4,5,6,8,8,8]
target=4

print(search_insert(nums,target))






