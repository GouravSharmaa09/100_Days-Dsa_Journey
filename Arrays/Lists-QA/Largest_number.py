# Day-11   Problem - Find the largest number in the array
# TIME_COPLEXCITY= O(N)

num= [2,5,3,1,6,5,7,8,9,0]
n=len(num)
largest= float("-inf")
#  INFINITE NO. LENE KE LITYE ISSE BHOT KM ERR AATI HAI LARGEST YA SECOND LARGEST KE LIYE HR DM VARIABLLE ME YE STORE KRNA CHYIYE 
for i in range (0,n):
    largest= max(largest,num[i])
print(largest)
