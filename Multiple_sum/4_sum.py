# Day=20
#     4-SUM PROBLEM NO. 18

# Method 1- Brute force Using multiple loop 

nums= [1,0,-1,0,-2,2,5,9]      # Time and complexcity= O(n^4)

# Output=[[-2, -1, 1, 2], [-1, 0, 0, 1], [-2, 0, 0, 2]]

n=len(nums)
my_set=set() 
target=0

for i in range (0,n):
    for j in range (i+1,n):
        for k in range (j+1,n):
            for l in range (k+1,n):
                 total_sum= nums[i]+nums[j]+nums[k]+nums[l]
                 if total_sum==target: # agr sum == target hai to temp list me store krdo value 
                    temp=[nums[i],nums[j],nums[k],nums[l]]
                    temp.sort() # list ko sort kro 
                    my_set.add(tuple(temp)) # ye isliye qki set me list nhi bhj skte to tuple dena pdega 

result=[] # ek khali list bnayi or set ko iterate kiya 
for ans in my_set:
    result.append(list(ans)) # result me list append krdo 

print( result)



# Method -2  Better approch [using hash_map] or two set  (formulla= fourth= target-(n[i]+n[j]+n[k]) )

# Time and complexcity - O(n^3) and s.c= O(n)

nums= [1,0,-1,0,-2,5,9,7,3]  

# Output=[[-1, 0, 0, 1], [-2, -1, 0, 3]]

n=len(nums)
my_set=set() #set 

for i in range (0,n):
    for j in range (i+1,n):
        hash_set=set()
        # has_set vo set hai jo j ke iterate krne pe set me nhi milne vali value ko find krke fourth value bnayega j+1 hone pe set khali hai to new fill krne ke liye 
        for k in range (j+1,n):
            # foruth element ka formulla agr set me nhi milta to skip else milta hai to forut element milgya 
            fourth= target-(nums[i]+nums[j]+nums[k])
            if fourth in hash_set: #  agr foruth hash_set me milta hai to temp list bnao forth ke sth ki target milgya 
                temp=[nums[i],nums[j],nums[k],fourth]
                temp.sort() # temp ko sort kro 
                my_set.add(tuple(temp))# set me add kro list form of tuple 
            hash_set.add(nums[k]) # agr element nhi milta set me to j ko hash_set me apend krte jao 



result=[]

for ans in my_set:
    result.append(list(ans))

print(result)



# Method -3 [Using 4 pointer] with sorted arr
# 
# Time and complecity = o(n^3)
# 

nums=[1,1,1,1,2,2,2,2,3,3,3,4,4,4,5,5]

# output = [[1, 1, 1, 5], [1, 1, 2, 4], [1, 1, 3, 3], [1, 2, 2, 3], [2, 2, 2, 2]] 

n=len(nums)
nums.sort() # sort honi chyiye arr mandantory hai 
result=[]
target=8
for i in range (0,n):
    if i>0 and nums[i]==nums[i-1]:  # agr i 0 se less than and i i-1 ke == hai to continue means age ka loop mt chlao i ko badhao
        continue 

    for j in range (i+1,n):
        if j>i+1 and nums[j]==nums[j-1]:
            continue

        k=j+1
        l=n-1

        while k<l:   # k or l ke cross over hone tk 
            total= nums[i]+nums[j]+nums[k]+nums[l]
            if total==target:

                result.append([nums[i],nums[j],nums[k],nums[l]])

                k+=1
                l-=1
                
                # duplicates skip krne ke liye 
                while k<l and nums[k]==nums[k-1]:
                   k+=1
                while k<l and nums[l]==nums[l+1]:
                   l-=1

            elif target>total:
                k+=1
            else:
                l-=1


print(result)


