# DAY-48   MAX CONSECUTIVE ONES-3      LEAT CODE - 1004
# MAX NUNBER OF ONCE BTANA HAI ARR M SE MAX NO. OF "K" ZEROS KO ONE BNA SKTE 

# METHOD - 1   BRUTE FORCE USING  SUBSTRING LOGIC 

def max_one(nums,k):
    count=0
    n=len(nums)

    for i in range (0,n):
        zeros=0

        for j in range (i,n):
            if nums[j]==0: # AGR J 0 HAI TO USKO 1 KRDO 
                zeros+=1
            # AGR ZERO K SE JYDA HAI TO BREAK 
            if zeros > k:
                break
            count=max(count,j-i+1) # MAX NIKALO 
    return count 

print(max_one([1,1,1,0,0,0,1,0,1,0,1,1,1,1,1],2))   # 9 

# time and complexcity = O(N^2), S.C= O(1)





# METHOD - 2 OPTIMAL APPROACH USING SLIDING WINDOW LOGIC 
# k se jyda hote hi zeros milne pe left ko eliminate kro or 0 ko k ke equl kro  
# logic --> jitna count phle tha (maxi) usse jyda ka ouput (chk ) try kro 


def max_one_optimal(nums,k):
    L=0
    R=0
    n=len(nums)
    maxi=0
    zeros=0
    
    # right n ko cross krjyega tb tk 
    while R < n :
        # agr right me 0 mila to zero ko 1 krdo 
       if nums[R]==0:
        zeros+=1

# agr zero jyda hai k se to 
       if zeros > k :
        # and left == hai 0 ke to zeros jo 1 bnaya hai usko km kro vps 0 krdo 
        
         if nums[L]==0:

           zeros-=1
         L+=1
# agr zeros ke equal or greater hai k then max nikalna 
       if zeros<=k :
          maxi=max(maxi,R-L+1)
       R+=1
    
    return maxi          


print(max_one_optimal([1,0,0,0,1,0,1,1,1,1,1,0],1))   # 7 


# T.C= O(N), S.C-O(1)

