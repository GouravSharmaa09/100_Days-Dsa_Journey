# DAY-24        Ciel and floor Problem 
# ciel = smallest no. in arr >=target
#floor = largest no. in array <=target

# Time and complexcity= O(log n)

def floor_ciel(nums,target):
    n=len(nums)
    floor=-1
    ciel=-1
    low=0
    high=n-1

    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return [nums[mid],nums[mid]]
        elif nums[mid]>target:
            ciel=nums[mid]
            high=mid-1
        else:
            floor=nums[mid]
            low=mid+1

    return [ciel,floor]

nums=[1,1,1,2,2,3,3,4,4,5,5,5,6,7,8,10]

# o/p= [6, 6]

target=6

print(floor_ciel(nums,target))






