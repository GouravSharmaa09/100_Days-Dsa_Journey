# Problem= 485   FIND THE MAXIMUM CONSUTIVE ONES 
# TIME COMPLEXCITY= O(N)
# S.C=O(1)

def max_one(num):
    n=len(num)
    max_count=0
    count=0
    for i in range (0,n):
        if num[i]==1:
            count+=1
        else :
            max_count=max(max_count,count)
            count=0
    return max(max_count,count)  

num=[1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1]
print(max_one(num))


# output =15