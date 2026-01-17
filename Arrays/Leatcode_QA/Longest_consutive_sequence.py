# DAY-15   
# Problem -128 = Longest Consecutive Sequcence 

# Method 1 Brute Force   (Find the longest sequcence in the list )

# Time and complexcity=O(n^2)
 

nums=[1,99,101,98,2,5,3,100,1,1]
# Output= 4
n=len(nums)
count=0
max_count=0

for i in range (0,n):
    #  num var me nums[i] ki value update ki and count ko 1 kiya 
   num= nums[i]
   count=1
#  loop chlaya num+1 hai nums list me to count ko or num ko +=1 kro 
   while num+1 in nums :
      count+=1
      num+=1

    #    max find krne ke liye count and max_count me 
   max_count=max(max_count,count)    
print(max_count)





# Method 2 -- Better solution  using sorting 

# Time and complexcity =O(nlogn+n) (sorting ke vhj se nlogn and n loop ka )

def sequcence(nums):
    n=len(nums)
    longest=0
    last_smaller=float("-inf")
    count=0
    for i in range (0,n):
        # O(n)

        num=nums[i]
        if num-1== last_smaller:
            #  num-1 agr equal hai last_smaller ke to count ko increment kro and last_smaller ko num se updte krdo 
            count+=1
            last_smaller=num
        elif num != last_smaller:
            #  agr num not equal hai lst_smaller ke to count ko 1 kro or vps new sequence bnao 
            count=1
            last_smaller=num
        longest= max(longest,count)
    return longest

nums=  [1,2,6,4,5,99,97,100,98]
# output = 4 (97,98,99,100)
nums.sort()
#   O(nlog n )   
print (sequcence(nums))          






# Method 3 -- Using Set logic 

# Time and complexcity = O(3N) --- O(N+N+N)

def set_seq(nums):
    n=len(nums)
    my_set=set()
    #  SET BNAYA EMPY THEN LOOP CHLAKE ADD KRI NUM[I] KE VALUES 
    
    for i in range (0,n):
        # O(N)
        my_set.add(nums[i])
    
    longest=0    

    for num in my_set:
        # O(N)
        # AGR NUM-1 SET ME NHI HAI TO COUNT KO 1 KRKE NUM KO J ME UPDATE KRDO OR WHILE LOOP CHLAO 
        if num-1 not in my_set:
            j= num 
            count=1
        while j+1 in my_set:
            #  AGR J+1 SET ME HAI TO COUNT OR J KA INCREMENT KRO OR SEQUENCE FIND KRTE RHO 
            # O(N)
            count+=1
            j+=1 

        longest=max(longest,count)
    
    return longest      

nums=[1,99,98,2,3,6,7,97,100,101,4,5,6,0]

# output = 8 (0,1,2,3,4,5,6,7)
print(set_seq(nums))    