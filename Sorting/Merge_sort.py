# Day-09   Merge sort (divide and conquer)

# logic = Two function bnayege  first merge arr (jo two sorted arr ko merge krega )  and 2 function merge_divide jo divide krega
# ouput= [0, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9]
# time and complexcity = O(nlog n ) [ O(log2n) for divide fun and O(n*n) for merge fun  and when we add both]

#  merge the two sorted arrays 
def merge_arr( left , right ):
#  left and right two pointer lege merge krne ke liye two sorted arr ko 
      n,m= len(left), len(right)
      i,j=0,0
      result=[]
      while i<n and  j<m:
        #  condition chk for i and j ki len se jyda to nhi hai 
          if left[i]<= right[j]:
            #  agr i equal ya small hai j se to append i else j 
             result.append(left[i])
             i+=1
          else :
             result.append(right [j])
             j+=1 

      if i<n:
        result.extend(left[i:])
        #  bki bche huye elements ke liye jo bch gye arr me compare ke bd 
      if j<m:
        result.extend(right[j:])
      return result

#  divide the array 
def divide_arr(arr):
    #  divide ke liye 
    if len(arr)<=1:
        #  condintion for arr me single element bchne ke liye 
      return arr
    mid= len(arr)//2    
    #  mid nikanle ke liye  bich me se arry ko divide kiya 
    left= arr[:mid]
    # left ke liye slicing 
    right= arr [mid:]
    #  right slicing 
    left_divide= divide_arr(left)
    #  recursion chalaya until arr me single element na bche 
    right_divide= divide_arr(right)

    return merge_arr(left_divide, right_divide)
    #  merge vale fun ko call kiya  

num= [2,6,1,0,3,7,8,9,9,5,2,4,6]
print(divide_arr(num))    