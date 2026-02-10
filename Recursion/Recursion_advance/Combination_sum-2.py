# DAY-37     COMBINATIONAL SUM -2  LEATCODE-39  
# (DUPLICATES NOT ALLOWED AND ALSO NOT PICK SINGLE INDEX ELEMENT unlimited  JUST LIKE 1 ONE )

# LOGIC = Duplicates ko remove krne ke bajaye unko skip krege 
#1. sorting the list first 
# 2. compare index ko ki i se jyda hai or previous number (i) present ke equal to nhi hai then flow ko aage bdhao 
# 3. total nhi target ko (-) krte chlege 0 milne pe ans bhi milega and target - hogya to return and i jyda hu target se to bhi return 

def solve (index,nums,target,subset,result):
    if target==0: # Target milte hi append kro 
        result.append(subset.copy()) # refrence 
        return 

    if target < 0 or index>=len(nums):  # agr target - hai and last index pe hum to return kro 
        return 

   # every number ko current index ke liye try kro (kitne combination bnskte hai )
    for i in range (index,len(nums)):
        # skip duplicates compare krke previous or present ko 
        if i>index and  nums[i]==nums[i-1]:
            continue
        # number bhi target se greater hai to loop roko 
        if nums[i]>target:
            break 
        
        # append the number (i)
        subset.append(nums[i])
        # (recursin-func call)   numbe rko increase kro nd target ko ek km krte rho 
        solve(i+1,nums,target-nums[i],subset,result)
        
        # backtrack -pop kro dusre item ke liye chk kro ab  
        subset.pop()

def sum_2(nums,target):
    nums.sort() # sort kro phle list ko 
    result=[]
    solve(0,nums,target,[],result)
    return result

print(sum_2([9,2,9,5,4],13))   # Output =[[4, 9]]

# Time and complexcity = O(2^N) --> KYUKI EVERY ELEMENT KE PSS 2 COHICE HAI PICK OR NON PICK 
#   S.C= O(K)

# BRUTE FORCE ISKA SET USE KRKE KR SKTE HAI 





