# DAY-47   SLIDING WINDOW (LONGEST SUBSTRING )  LEAT CODE - 3
# SUBSTRING = CONTINOUS JO AAYE REPEAT NHI HONE CHYIYE STRING 

# BRUTE FORCE = USING SET 

def longestsubstring(s):
    n=len(s)
    if len(s)==0:
        return 0 
    maxi=0

# pointer i ye set me value add krega 
    for i in range (0,n):
        my_set=set()

# ye pointer j value chk krega set me 
        for j in range (i,n):
            if s[j] in my_set:
                break

            maxi=max(maxi,j-i+1) 
            my_set.add(s[j])

    return maxi 

s= ["a","b","a","c","c","g","f"]   # 3 

print(longestsubstring(s))               

# Time and complexcity = O(N^2),   S.C= O(N)



# Method 2  optimal using sliding window (l,r) and hash_map 


def slidingwindow(s):
    hash_map=dict()
    left=0 
    right=0
    maxi=0

    n=len(s)
# right n ko cross nhi kre itne 
    while right < n :
        if s[right] in hash_map: # agr right dict me hai to 
            left=max(hash_map[s[right]]+1,left) # left ka max nikalo  (dulicate skip ke liye )

# amximum count nikalne ke liye 
        maxi=max(maxi,right-left+1)
# right se update krne ke liye value ko 
        hash_map[s[right]]=right

        right+=1

    return maxi 

s=["a","b","c","z","w","a","b","k","d"]   # 7

print(slidingwindow(s))

# T.C= O(N), S.C=O(N)