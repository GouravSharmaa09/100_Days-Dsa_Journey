# DAY-52    JUMP GAME 2      LEATECODE-45  
# MINIMUM JUMP BTRANI HAI END TK JANE KE LIYE (LAST IND TK )

# BRUTE FORCE USING RECURSIVE SOLUTION 

def recursive(index,jump,last_ind,nums):
    if index>=last_ind:
        return jump

    mini_jump=float("inf")

    for i in range (1,nums[index]+1): # LOOP FOR JUMP JITNI JUMP HAI UNTE LOOP 
        mini_jump=min(mini_jump,recursive(index+i,jump+i,last_ind,nums)) # MINIMUM JUMP NIKALI 


    return mini_jump

nums=[2,3,1,4,1,1,1,2]
n=len(nums)
print(recursive(0,0,n-1,nums))





# Optimal (using greedy approach )    two pointer 

# T.C=O(N)  S.C=O(1)

def greedy_jump(nums):
    jump=0#
    left=0
    right=0
    n=len(nums)

    while right<n-1:  # LAST INDEX TK 
        farthest=0 # LAST TK FARTHEST BOLEGE LAST MAX JUMP KO 

        for i in range (left,right+1): # JUMP PE LOOP CHLAYEGE 
            farthest=max(farthest,i+nums[i]) # FARTEST AND INDEX ME SE MAX DEKHO 

        left=right+1
        right=farthest
        jump+=1

    return jump


nums=[2,1,3,4,3,2,5,6,7]  # 4 
print(greedy_jump(nums))