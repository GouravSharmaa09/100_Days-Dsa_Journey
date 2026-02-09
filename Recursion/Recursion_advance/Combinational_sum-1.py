# DAY-36    COMBINATIONAL SUM -1    leat code= 39 

# logic - find sum and same index ko repeat kr skte hai unlimitied time tk 

def solve (index,total,subset,target,nums,result):
    if total == target :  # agr item milgya to append kro refence list me 
        result.append(subset.copy())
        return 

    if total>target or index>=len(nums):
        return     
    
    sum=total+nums[index]
    subset.append(nums[index])
    solve (index,sum,subset,target,nums,result) # index +1 nhi kiya kyuki same index ko unlimited basr chlaskte hai to try krte hai ky ans deta hai 

    sum =total
    subset.pop()

    solve(index+1,sum,subset,target,nums,result)

def COMBINATIONAL(nums,target):
    result=[]
    # target=4
    solve(0,0,[],target,nums,result)
    return result

print(COMBINATIONAL([1,2,3],4))

# output=[[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]]

# Time and complexciy= O(2^t * K )     ,  S.C= O(t)+O(k)