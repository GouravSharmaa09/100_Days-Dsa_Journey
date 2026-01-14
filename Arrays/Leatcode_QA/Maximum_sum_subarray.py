# PROBLEM = FIND THE MAXIMUM SUM OF SUB_ARRAY
           

# method -1 = Brute force 
# TIME and complexcity= O(n(n+1)/2)=o(n)

def sub_arr(num):
    n=len(num)
    max_sum=float("-inf")
    
    for i in range (0,n):
        total=0
        for j in range (i,n):
            total= total+num[j]
            max_sum= max(max_sum,total)
    return max_sum

num=[-2,3,4,-6,7,8,9,5]

print (sub_arr(num))
# output= 30 


# Method 2 = OPTIMAL -  Kadane's Algorithm (NEGATIVE KO TOTAL ME NHI AANE DEGE IF NEGATIVE COMES TOTAL KO 0 KRDO )

# TIME AND COMPLEXCITY= O(N) AND S.C = O(1)

def sub_arr_2(num):
    n=len(num)
    total=0
    max_count=float("-inf")
    
    for i in range (0,n):
        # total ki value me num[i] add on kro 
        total=total+num[i]
        max_count=max(max_count,total)
        #  max or total me se max find kro 
        if total<0:
            # if total is less than 0 than total ko 0 kro 
            total=0
    return max_count

num=[-2,3,8,-9,7,8,2,4]
print(sub_arr_2(num))         
# output = 23 
