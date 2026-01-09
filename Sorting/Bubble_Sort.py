# # Bubble Sort/ Adjacent Swaps ( Neighbhours ko swap kro )
# input = [3,5,2,6,1,7]
# output=[1, 2, 3, 5, 6, 7]

# Time complexcity = O(n2)

def bubble ( arr):
    n= len(arr)
    for i in range ( n-2, -1,-1):
#  range (n-2    isliye hai kyuki i ko len-1 pe rhkna pdega qki j+1 itertion krege jb end me aayega to index err aayega 
# isliye n-2 range set krni pdi hai  n-2 rhkne se J or j+1 end m,e swap kr pyege ek -1 0 tk ke liye and second reverse ke liye )
        for j in range (0,i+1):
            #  range 0 se start hogi or i+1 krke aage jayega means j+1 
            if arr[j]>arr[j+1]:
                #  agr j greater hai j+1 ke to swap kro 
                arr[j],arr[j+1]= arr[j+1],arr[j]
    return arr
print(bubble([3,5,2,6,1,7]))                