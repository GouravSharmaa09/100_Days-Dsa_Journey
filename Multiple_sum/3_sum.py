# DAY-19        [Problem-15  3 SUM IN ARRAY]
# FIND THE TRIPLET SUM IN THE ARR IS EQUAL TO 0 AND GIVE ONLY UNIQUE ELEMNTS DONT GIVE DUPLICATES 

#TIEM AND COMPLEXCITY = O(N^3) AND S.C= O(No. of sum) 

# METHOD - 1  BRUTE FORCE   [USING 3 POINTERS OR SET] 
arr=[-1,0,1,-2,-1,2,-4]
# Output = [[-1, 0, 1], [-2, 0, 2], [-1, -1, 2]]  ye sbka ka sum ==0 hai 
n=len(arr)
my_set=set()

# 3 loop iterate kre ge or comparision krege every items se == 0 hai ya nhi 
for i in range (0,n):
    for j in range (i+1,n):
        for k in range (j+1,n):

            if arr[i]+arr[j]+arr[k]==0:
                temp= [arr[i],arr[j],arr[k]]
                temp.sort() # duplicates ko remove krne ke liye taki set unhe na mane or unique list hi mile 

                my_set.add(tuple(temp))

print([list(ans) for ans in my_set])      # list comperstion hai list me convert ke liye 



# METHOD-2 BETTER SOLUTION  [USING TWO POINTER OR TWO SET LOGIC AND FORMULLA],,,Hashing Search
# formulla= arr[k]= -(arr[i]+arr[j])
# Time and complexcity=O(N^2) AND S.C= O(N)

arr=[-1,0,1,-2,-1,2,-4,3]
# Output= [[-1, 0, 1], [-4, 1, 3], [-1, -1, 2], [-2, -1, 3], [-2, 0, 2]]
n=len(arr)

result=set() # result ke liye set 

for i in range (0,n): # i ka loop chalane pe ek set bnao 
    
    my_set=set()
    
    # j ka loop run kro i+1 se or formulla lga ke dekho third ke liye 
    for j in range (i+1,n):
       
       third= -(arr[i]+arr[j]) # agr in dono ka sum vala element my_set me milta hai to 
       
       if third in my_set: # like - i fixed hai or j i+1 pe hai then formulla lgane pe set me chechk kro ki j jis pe hai vo element hai ya nhi if hai to arr[k] third milgya else j ko +1 kro
          
          temp= [arr[i],arr[j],third]
          
          temp.sort()  # sort the list 
          
          result.add(tuple(temp)) #  set me list nhi de skte to tuple dena pdega 

# j ko +=1 krne ke liye set me element nhi milta to 
       my_set.add(arr[j])

print([list(ans) for ans in result])  # ye list comperstion hai list chyiye ans me to list me convert kr rhe hai set ko       



# Method -3  Optimal solution [ USING TWO POINTER LOGIC AND REDUCE THE S.C,, SORTING IS NEEDED]

# Time and complecity= O(n log n )+ O(n^2) and S.c = O(1)

arr=[-2,-2,-2,-1,-1,-1,0,0,0,0,2,2,2,2]
# Output= [[-2, 0, 2], [-1, -1, 2], [0, 0, 0]]


n=len(arr)
#  Sort honi chyiye arr 
arr.sort()
ans=[]# result ans me store hoga 

for i in range(n):
    #  check krege ki i duplicate to nhi hai 
    if i!=0 and arr[i]==arr[i-1]:
        continue

    j=i+1# i+1 pe hoga j 
    k=n-1# k last me 
   
   # j and k ke cross over tk chlega loop 
    while j<k:
        total_sum= arr[i]+arr[j]+arr[k] # sum of triplet
        
        if total_sum<0: # agr total less hua 0 se to j ka increment 
            j+=1
        elif total_sum>0: # elif k ka decrement 
            k-=1
        else: # list mtlb element == 0 hai to element do vo 
            temp= [arr[i],arr[j],arr[k]]

            ans.append(temp) # ans me temp ko append krege 
            j+=1
            k-=1
            while j<k and arr[j]==arr[j-1]: # j ke duplicates ko skip kro 
                j+=1
            while j<k and arr[k]==arr[k+1]: # k ke duplicates ko skip krne ke liye 
                k-=1
print(ans)                



