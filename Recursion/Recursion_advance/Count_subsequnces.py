# DAY-35    COUNT ALL THE SUBSEQUNCES WITH SUM KO K 
# kitne sum contain krta hai list vo btana hai k ke equal 
# Logic -- O, or 1 leke chlege only means--> milta hai to retrun 1 and nhi milne pe 0 and and me sum of both pick and not pick   (index,total)

def solve (nums):
   
# ISME HUM INDEX OR TOTAL HI PASS KREGE SUBSET KA KM NHI HAI  
    def count_subsequcnes(index,total):
        if total==k: # AGR MILA TO 1 RETURN KRO 
            return 1

        elif total>k: 
            return 0 

        elif index>=len(nums):
            return 0         

        sum = total+nums[index] 
        
        pick = count_subsequcnes(index+1,sum) 

        sum=total # RESET KRDEGA (NOT KA SUM COUNT NHI KREGA) 

        not_pick = count_subsequcnes(index+1,sum)

        return pick + not_pick

    return count_subsequcnes(0,0)
k=2
print(solve([1,2,2,2,2,2,2,2,3]))  #O/P=7

# Time and complexcity = O(2N)     S.C=O(N)
