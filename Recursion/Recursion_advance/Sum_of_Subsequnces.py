# DAY-34   GERNATE THE ALL SUBSEQUENCES WITH SUM=K 
# Logic - Same recursion (pick or non pick ) but in case of target sum i take total as to chk sum if target == or not 
# backtracking  (pop)

def find_sum(nums):
    result=[]
    total=0

    # Subsequcne find krne ke liye or sum chk krne ke liye 
    def chk_sum_subsequnces(index,total,subset):
        # 3 base case 
        
        # case 1. agr target milgya then append in refrence list 
        if total==k:
            result.append(subset.copy())
            

        # case 2 - agr taotal target se greater hai to retrun aage jaane ki need nhi hai because aage bhi greater hi milege 
        elif total> k :
            return
 
        # agr index last pe aagya to 
        elif index>=len(nums):
            return 
        
        # pick the element 
        subset.append(nums[index])
        # calulate the sum of element 
        sum= total+nums[index]


        chk_sum_subsequnces(index+1,sum,subset)

       # backtrack element  nikalo  
        e=subset.pop()             
        # sum me se sutract kro agr jyda hai to 
        sum-=e
        
        # Non pick valo ke liye fun call 
        chk_sum_subsequnces(index+1,sum,subset)

    chk_sum_subsequnces(0,0,[])
    
    return result    
k=4

print(find_sum([2,3,4,1]))
#Output=[[3, 1], [4]]

# Time and complecity = O(2N)   S.C= O(N)
