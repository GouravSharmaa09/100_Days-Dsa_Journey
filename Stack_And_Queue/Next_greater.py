# DAY-46   NEXT GREATER Element     Monotonic Stack problem 

# 1. BRUTE FORCE USING TWO POINTER 
# right side me sbse phla greater element btana hai 

def next_greater(nums):
    n = len(nums)
    ans=[-1]*n # arr jo -1 honge n numebrs tk 

    for i in range (0,n):
        for j in range (i+1,n):
            if nums[j]>nums[i]: # agr j bda hai i se to 
                ans[i]= nums[j] # ans ke i'th element ko nums ke j 'th krdo 
                break 

    return ans      # -1    

    # Time and complexcity o(n^2)



# method - 2 optimal using stack approach 

# logic = back se iterate krege agr koi elemnt current se chota hai to current hi uska next greater hai cureent ko stck me aapend kro or aage vale ki value chnge kro 
# back se iterate krne se stck me hmesha next greater element store hoga 


class solution :
    def next_greater_stack(self,nums):
        n= len(nums)#
        result=[-1]*n # list -1 vli 
        stack=[] 

# loop reverse iterate krega jese hi elemnt se chota element milega append krdega i ko stack me 
        for i in range (n-1,-1,-1):
          # agr stack empty nhi hai and top elemnt i se chota hai to 
            while len(stack) !=0 and stack[-1]<=nums[i]:
                stack.pop()# pop it 
# agr stack empty nhi hai 
            if len(stack)!=0:
                # resutl ke i value ko stack ki top krdo 
                result[i]=stack[-1]
# and stck me current value append krte rho 
            stack.append(nums[i])
        
        return result        



# Time and coplexcity = O(n)
# s.c =   o(n)

sol = solution()
arr = [4, 12, 5, 3, 1, 2, 5, 3, 1, 2, 4, 6]
print(f"Array: {arr}")
print(f"NGE:   {sol.next_greater_stack(arr)}")

# Array: [4, 12, 5, 3, 1, 2, 5, 3, 1, 2, 4, 6]
# NGE:   [12, -1, 6, 5, 2, 5, 6, 4, 2, 4, 6, -1]