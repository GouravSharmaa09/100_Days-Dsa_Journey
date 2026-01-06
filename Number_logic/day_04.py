# Problem 1= Palindrome / Reverse number logic

n= int(input("number bta na bhai kal subha Panvale niklna hai :"))
num=n
result=0
while num>0 :
    last_digit = num %10 
    result= (result*10) +last_digit
    num = num//10  
print(n==result)
print( "ye rha tera palindrome",  result)






# Problem 2 = Reverse number Adder 


n= int(input("nuber do sum check krvao :"))
num=n
total = 0
reverse=0
while num>0 :
    last_digit = num %10 
    reverse= (reverse*10) +last_digit
    num = num//10  
total = n+reverse    
if total >= 500 :
    print("vaild sum ", total)
else:
    print("sum is less than 500", total)




# Problem 3 = digits ka product but condition hai ki sirf odd ka hi product nikalna hai 


n= int(input("number bta na bhai product nikalna hai :"))
num = n 
product = 1
while num > 0:
  last_digit = num%10
  if last_digit%2!=0 :
      product = product* last_digit
      

  elif last_digit %2 ==0 :
       print("even hai koi digit odd nhi hai " )
  num = num//10   
print(product)      
  



# Problem 4= Factors of a number or a divisor of a number  solx.1.1  using Brute force method 
#  Time complexity = O(n)   
# Space complexity = O(k)  - because result list me kitne bhi aa skte hai constant


n= int(input("number bta na bhai factors nikalna hai brute force se :"))
num=n
result=[]
for i in range(1, num+1):
  if num %i==0 :
      result.append(i)          
      
print(result)    


#  Better Solution    ,   Time complexcity = O(n/2)  = O(n)
# output= [1, 2, 10] 

n = 10 
num=n
result= []
for i in range (1, num//2):
    if n%i ==0 :
       result.append(i)
result.append(num)
print(result)





# Optimal Solution , Time complexcity =
# output = [1, 2, 3, 4, 6, 9, 12, 18, 36]
from math import sqrt        
#  import kiya sqrt 
n = int(input("number btao bro me tuje divisor btauga :"))
num= n 
result=[]
for i in range (1,int(sqrt(num))+1):
    if num %1==0:
        result.append(i)
        if num // i !=i :
        #  6 do baar append nhi ho isliye 
        # Agar num = 36 hai aur i = 6 hai 36 / 6 = 6 hota hai.
          result.append(num//i)
# ye isliye because 36/1 hoga to ye 36 ko i equal nhi hai 36 ke to usko bhi append krege jese i 2 hai to 36/2 = 18 to upr vala if 2 ko append kr rha hai or ye vala 18 ko becuse vo i ke not equal hai 

result.sort()
print(result)