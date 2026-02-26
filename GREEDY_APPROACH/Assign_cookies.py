# DAY-49   ASSIGN THE COOKIES  USING GREEDY APPROACH    LEAT CODE - 455 

# LOGIC = USING TWO POINTERS ( FULFIL THE ALL COOKIES USING GREEDY )
# sort jruri hai without sort nhi hoga 


def assign_cookies(g,c):
    n=len(g)
    m=len(c)

    g.sort() # sort the list 
    c.sort()

    left=0
    right=0
    count=0

    while left<n and right<m: 
           if g[left]<=c[right]: # agr left greater ya equal hai to count ko increase kro 
                count+=1
                left+=1
           right+=1 # move to next cookies 

    return count

g=[1,2,4,6,8]  # grredy members jinko cookie chyiye 
c=[1,2,2,3,7,0] # ye cookies hai 

print(assign_cookies(g,c))


# Time and complexcity = O(nlog n) + O(m log n )+O(N) ,  S.C- O(1)

