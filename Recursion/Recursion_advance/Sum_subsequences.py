# DAY-37    GERNATE SUM OF SUBSEQUCENSES  [PROBELM-SUBSET_SUM-1 ]
# Logic -   In this hum subset use na krke direct sum hi list me append krdege 


# ISME HUMKO SUBSET SE KM NHI HAI KYUKI HUMKO SUBSET KE SUM BTANE HAI BS 
def solve (index,total,result,nums): 
    if index>=len(nums):
        result.append(total) # APPEND TOTAL IN LIST 
        return 


    # SUM NIKAL EVERY SUBSET KA 
    sum=total+nums[index]
    # RECURSION FOR PICK ONE 
    solve(index+1,sum,result,nums)
    
    # TOTAL KI VALUE RESET KI NOT PICK KE LIYE 
    sum=total
    solve(index+1,sum,result,nums)

def sum_total(nums):
    result=[]
    solve(0,0,result,nums)
    return result

print(sum_total([4,5,6]))
# Output = [15, 9, 10, 4, 11, 5, 6, 0]

# Time and complexcity = O(2N) AND S.C= O(N)
# 2N ISLIYE KYUKI EVERY ELEMENT KE PS 2 CHOICE HAI PICK OR NOT PICK KI 