# DAY-52    JUMP GAME 1  ,  LEATCODE -55
# MAX_INDEX BTANA HAI KHA TK PHUCH SKTA HAI JUMP L K 
# 
# INSTITUION = WE take MAX_INDEX VAR AND STORE THE JUMP (MAX) BUT IF I GREATER THAN MAX_INDEX THAN RETURN FALSE BECASUE MAX INDEX BTANA HAI BUT AGR I GREATER HOGA TO MEANS MAX INDEX PICHE RH GYA IN CASE OF I PE 0 HAI TO 
# 
# Time and complexcity = o(n)    s.c = o(1)

def jump_game(nums):
    n=len(nums)
    max_index=0
    for i in range (0,n):
        if i > max_index: # agr i greater hai max se to false return kro 
            return False

        max_index=max(max_index,i+nums[i]) # max nikal index + val (jump)


    return True 



nums=[3,2,1,0,0,2,1,5]
print(jump_game(nums))  
 
