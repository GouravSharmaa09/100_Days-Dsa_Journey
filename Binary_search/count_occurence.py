# DAY-24      COUNT THE OCCURENCE THE NUMBERS 

# METHOD -1 BRUTE FORCE    COUNT KRNA HAI ARR ME ELEMENT KITNI BAAR AAYA 

# T.C= O(n)

nums=[1,1,1,1,1,1,2,2,2,3,3,3,4,5,6,7,7,7]
n=len(nums)
first=-1
last=-1
target=1

for i in range(0,n):
    if nums[i]==target:
        if first==-1:
            first=i
        last=i

if first == -1:
    print(0)
    # logic count ka 
print(last-first+1)    




# Method -2  Optimal using binary search 

# Time and complexcity = O(2log n )


def lower_bound(nums,target):  # lowwer bound ka function 
    n=len(nums)
    low=0
    high=n-1
    lb=-1
    
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            lb=mid  # mid ka index l liye lb me store kiya 
            high=mid-1
        else:
            low=mid+1
    return lb



def upper_bound(nums,target): # upper bound ka function bnaya isme last index ka logic ub-1 se hojyega 
    n=len(nums)
    low=0
    high=n-1
    ub=n
    
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:  # agr target se bda hai to 
            ub=mid   # mid ko ub me daaalo index ko 
            high=mid-1
        else:
            low=mid+1
    return ub



def search_range(nums,target):   # final fun jo range btyega dono fun call krva ke 
    n=len(nums)

    lb=lower_bound(nums,target) # lb ka fun call()
    if lb==-1 or nums[lb]!=target: # agr lb euqal hai -1 ke or lb ki value target ke not euqal hai return kro -1-1
        return 0 #  mtlb arr me element nhi hai to 

    ub=upper_bound(nums,target)  # uppper bound fun call()
    if ub==-1: # agr ub eual hai -1 ke 
        return[lb,n-1]  # return lb or last index means n-1 agr arr me element na ho or sbse bde element ke liye b

    return ub-lb # logic ub -1
    

nums=[1,2,3,3,3,3,4,4,4,5,5,6,6,7,9]

target=3

# O/p= 4

print(search_range(nums,target))

