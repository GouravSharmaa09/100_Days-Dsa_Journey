# DAY-34       GERNATE ALL THE SUBSEQUENCES (USING RECURSION)
# Logic - Pick And Non pick [Two choises we have pick the item or Non pick the item ]

def find_subsequnce(nums): 
    result=[]

    def recusrion_fun(index,subset): # subsequnce find krne ka function 
        
        # base condition list ki length ka lst index pe stop or append in result 
        if index>=len(nums):
            # append the refernce of list kyuki end me jo list hogi vo empty aayegi all possibple pick non pick action perform krne ke bd 
            # refrence list (duplicate) ye hi append hogi 
            result.append(subset.copy())
            return
        
        # pick kro element ko 
        subset.append(nums[index])
        recusrion_fun(index+1,subset)
        
        # backtrack element ko nikalo 
        subset.pop()
        
        # Non pick kro 
        recusrion_fun(index+1,subset)

    recusrion_fun(0,[])
    
    return result

print(find_subsequnce([1,2,3]))
#OUTPUT= [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]       
 
# Time and complexcity = O(2n),   S.C=O(n)
     