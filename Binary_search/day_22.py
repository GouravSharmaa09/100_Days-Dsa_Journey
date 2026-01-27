# DAY-22         LOWER BOUND AND UPPER BOUND 

# 1.LOWER BOUND    [small index dhund te hai array ka like nums[i]>=target  ]

# time and complexcity = o(log2n)

def lower_bound(nums,target):
    n=len(nums)
    low=0
    high=n-1
    lb=n    #  only for array me sabse bada element target me ho or arr me na ho to ye n retrun krega means last index 

    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:    # lower bound ka asli logic taregt se chota ya equal hai to in lower bound 
            lb=mid
            high=mid-1
        else:
            low=mid+1

    return lb

nums=[1,1,1,2,2,3,3,4,5,6,9]
# output = 11   beacasue ye n dega agr array me elements nhi hai to 

target=15

print(lower_bound(nums,target))




# 2. Upper bound [small index for nums[mid]>target   lower bound jha khatam hota hai ]
# 
#  

def Upper_bound(nums,target):
    n=len(nums)
    low=0
    high=n-1
    ub=n

    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:  #lower bound khtm hora hai vha se upper bound start hai 
            ub=mid
            high=mid-1

        else:
            low=mid+1

    return ub

nums=[1,1,1,2,2,3,3,4,5,6,7,8,9]    

target= 2
# output=5

print(Upper_bound(nums,target))


