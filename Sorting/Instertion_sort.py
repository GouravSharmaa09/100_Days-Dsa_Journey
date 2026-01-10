# Day 09= Inserstion Sort 
# logic = i ko 1 se chalyege and j ko i-1 se 
# ek key bnayege jisko comapre kerge j+1 or j se agr j+1 small hai j se to duplicate krege or j-=1 krke compare krege until sorted 
# output =[2, 3, 4, 5, 6, 7]
# Time_complexcity= O(n(n+1)/2) = O(n2)

     

def insertion_sort(arr):
    n= len(arr)
    for i in range (1,n):
      key=arr[i]
    #    i ki value ko key me store krege 
      j=i-1
    #    j i-1 pr chelga mesns 0 se 
      while j>=0 and arr[j]>key:
        #  condition for j agr 0 se greater  ya 0 ke equal or j ki value key se jyda hai to - 
                arr[j+1]= arr[j]
                #  j+1 ki value ko j ki value ki copy bnao  ( but agr condition true hai to )
               
                j-=1
                #  j-=1  check kro ab loop ko 
                arr[j+1]=key
                #  j+1 ki value ko key me update kro agr condition satisfy nhi hoti to 
            
    return(arr)
print(insertion_sort([2,3,7,4,5,6]))    
