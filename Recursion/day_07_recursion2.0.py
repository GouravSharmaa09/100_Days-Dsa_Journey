# Problem 1 - Reverse a Array using A recursing 
 #  arr= [2 3 4 5 6 7 8 9 0]
  # left- 0 1 2 3 4 5 6 7 8 - right
#   ouput - [0, 9, 8, 7, 6, 5, 4, 3, 2]
def reverse(arr , left, right):
#    left or right isliye hai ki inko compare krna hai swapping ke liye left se 0 utaya or right ka len(num)-1 
    
    if left>=right :
        # agr left right se greater hai to return kro kyuki swap hogye hoge ese hoga to
        return
    arr[left],arr[right]= arr[right],arr[left]
    # swap ke liye 
    reverse(arr,left+1,right-1)
    # fun call hai left ki value ko increase kro 1 swap hojye to or right ko decrease -1 
arr= list(map(int,(input("Bol bhai ky arr btayega aj reverse krvane ke liye :").split())))
reverse(arr,0,len(arr)-1)
print(arr)  


# using while loop same question 

n = [0, 9, 8, 7, 6, 5, 4, 3, 2]
num=n
left = 0 
right = len(num)-1
while left < right:
    num[left],num[right]= num[right],num[left]
    left+=1
    right-=1

print(num)        





# problem - 2 Palindrome check using Recursion 



def func(num,left,right):
    if left>= right :
        return True
    if num[left] != num[right]:
        return False 
    return func(num,left+1,right-1)    
num = input("btayega tere string to me check krluga palindrome hai ky :")
result = func(num, 0 , len(num)-1)
print("dek le ab tu khud hi :", result )      






# Using While loop Palindrome 

n= input()
num=n 
left= 0 
right = len(num)-1
is_palindrome = False

while left<right:
    if num[left]!= num[right]:
        is_palindrome= False
        break
    left+=1
    right-=1
print(is_palindrome)        








# problem =Array (Half-Reverse) using recursion 

def func(num, left , right ):
    if left>=right :
        return 
    num[left],num[right]= num[right],num[left]
    func(num, left+1, right-1)
num= [2,3,4,5,8,6,7]
func(num,0, (len(num//2))-1)    
     # num//2 isliye kyuki half reverse krni hai to len(num//2)-1 se back side se right ka half 
print(num)