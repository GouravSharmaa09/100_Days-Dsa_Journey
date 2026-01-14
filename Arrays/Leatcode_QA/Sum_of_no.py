# Problem-- Sum of Two numbers and Return the index of Sum of no. is equal to target 

# Method --1 USING TWO POINTER   (Brute force )
# TIME AND COMPLEXCITY= O(N2)---[N(N+1)/2]
# S.C = O(1)

def Sum_number(num,target):
    for i in range (0,n-1):
        # iterate the i n-1 beacause j is iterate the n 
        for j in range (i+1,n):
            #  iterate the j 
            if num[i]+num[j]==target:
                #  add no. i+j and compare is equal to target or not 
                # return the i and j (index)
                return [i,j]
num=[5,2,3,1,5,6,9,2]
n=len(num)
target=15
print(Sum_number(num,target))      

# output = [5, 6] = 6+9          




# Method 2 --- USING HASHING (HASH_MAP)  / DICT()  ye optimal solution hai 
# TIME AND COMPLEXCITY = O(N)
# S.C= O(N) IN WROST CASE 

def sum_number(num,target):
    hash_map=dict()
    for i in range (0,n):
        remaining= target-num[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[num[i]]=i
num=[5,2,3,1,5,6,9,2,7,0]

n=len(num)
target=7
print(sum_number(num,target))   
# output = [0, 1]
# 5+2=7 jo ki 0 and 1 index pe hai           



# Method 3---- Using Two pointer but in sorted array / Better solution 
# TIEM AND COMPLEXCITY =O(N)

def sum_sorted(num,target):
    num.sort()
    n=len(num)
    left=0
    right=len(num)-1
    while left<right :
        #  iterate kro agr left right se km hai 
        current_sum= num[left] +num[right]
# cureentsum ,ko update kiya left or right ke addition se 
        if current_sum== target :
            #  agr cureent sum == hua target ke to left right ki index return kro 
             return[left,right]
        elif current_sum<target :
            #  sum small hai left se to left ka increment kro 
             left+=1
        else:
            right-=1
    return none 

num = [1, 2, 3, 4, 6, 9] # Pehle se sorted hai
target = 13
print(sum_sorted(num, target))


# output =[3, 5]