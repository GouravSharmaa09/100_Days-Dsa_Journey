# DAY--47   ASTROID COLLSION    LEAT CODE -735 
# (+)Number---> <---(-)NUMBER  is trh collopased krege agr negative number digit me bda hua positive se to pop krdege abs bolte hi - number ko  


# logic using stack positive ko push krege and negative milter hi compare krege if small then pop 


def astroid(nums):
    n=len(nums)
    stack=[]

# iterate the numbers 
    for i in range (0,n):
        if nums[i]>0:
            # agr number positive hai 
            stack.append(nums[i]) # append in stack 

        else:
# chk stck empty na ho , top element negative na ho(TOP 0 SE BDA HO ) , top se bda hai negative then 
            while len(stack)!=0 and stack[-1]>0 and stack[-1]<abs(nums[i]):
                # pop elemnt 
                stack.pop()
# agr stck empty hai and top negative n0. ke  ke equal hai 
            if len(stack)!=0 and stack[-1]==abs(nums[i]):
                stack.pop() # pop krdo 
# agr stck me elemnt nhi hai or neagtive numbe rhai 
            elif not stack or stack[-1]<0 :
                stack.append(nums[i])
                # append krdo negative stck me 

    return stack      

print(astroid([5, 10, -5]))    
# [5, 10]


    # Time and complexcity = O(2N),     S.C  = O(N)                 