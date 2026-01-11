# Day11-  QUICK SORT (PARTITION AND CONQUER)  
# TIME COMPLEXCITY = O(nlog2n) -- Best and Avg case 
# Wrost case -- O(n2)
# output= [10, 11, 20, 23, 34, 55, 99]


# Partition function hai  ye Pivot bnake arr ko sort krne ka km krege pivot ke less than left side an greater right side 
def Partition(arr,low,high):
    #  partition krlege low and hight ka jidar j n-1 pe hoga (high) and i in low or arr(low ) ko pivot krdege 
   pivot=arr[low]
#     pivot the first element of arr
   i,j=low,high
   while i<j :
    #  condition for index of i and j ( i ka index j se greater hone pe (cross over pe)) True hogi 
       while arr[i]<= pivot and  i<=high-1:
        #  arr[i]agr greater hai pivot se 
           i+=1
        #     i ko badaho aage until condition fail na ho 
       while arr[j]> pivot and j>=low+1:
        #  agr j less than ho pivot se 
           j-=1
       if i<j:
        #  agr i greater j se  to swap it 
            arr[i],arr[j]=arr[j],arr[i]
   
#    index vali condition fail hoti hai to (i<j) cross over ki to swap pivot ko j se 
   arr[low],arr[j]= arr[j],arr[low]  
        
   return j
#    return j krega ye left side or right side ko sort krne ke liye 
    

    #  Quick sort function hai jo sorting krne ka km krege pivot index jo partition ne pivot ko sahi jgh sort kiya uske aage ka km krke puri array ko sort krege 
def quick_sort(arr, low , high):
     n=len(arr)
     if low<high:
        #  agr low less than hai high se to pivot index me partition fun call kro (recursion )
         pivot_index = Partition(arr,low,high)
        #   left ke liye qucik sort fun call kro 
         quick_sort(arr,low,pivot_index-1)
        #   right side ke liye quick sort fun call kro 
         quick_sort(arr,pivot_index+1,high)
arr=[23,34,11,10,20,99,55]         
quick_sort(arr,0,len(arr)-1)   
print(arr)