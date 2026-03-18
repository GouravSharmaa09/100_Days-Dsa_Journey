# DAY-52 TRAIN AND PLATFORM    
# Maximum no. of platform btane hai train ke liye 

# instituion= sort the lists acoourding to arrival and dept time then increae count accourding to order

# Time and compelxcity = O(n log n + n + n )= o(n log n )
# S.C=O(1)


def max_platform(arr,dept):
    arr.sort()
    dept.sort()
    i=1
    j=0
    ans=1
    count=1

    while i<len(arr) and j< len(dept):
        if arr[i]<= dept[j]: # AGR ARRIVAL DEPT SE SMALL HAI TO COUNT KO INCREATE KRO OR i AAGE Bdhao next chk ke liye  
            count+=1
            i+=1
        else: # nhi hai to count mt bdhao or j ko aage bdhao 
            count-=1
            j+=1

        ans=max(ans,count)


    return ans 

arr=[900,940,950,1100,1500,1800]
dept=[910,1200,1120,1130,1900,2000]

print(max_platform(arr,dept))  

# O/P= 3