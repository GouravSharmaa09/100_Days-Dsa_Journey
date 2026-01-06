# Problem 1 = Character Frequency (The ASCII Logic) using Frequency_map / dict / hash_list or hash_map
# Input: s = "programming"
# output := le bhai tere frequency dekh le : {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
# Time_complexcity - O(n)



s = "programming"
freq_map = dict()
for i in range(len(s)) :
    if s[i] in freq_map:
       freq_map [s[i]]+=1
    else:
        freq_map[s[i]]=1   
print("le bhai tere frequency dekh le :",freq_map)    



# Problem 2: The "Range" Challenge (List Hashing) 
# Timecomplexcity- O(n)
# In this  hash_list ka use kiya kyuki ye question humko ko given thae ki num me 1 to 10 ke mid me hi hai value  and is question pe count btana tha with respectiviley index 


num = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
hash_list= [0]*11
for i in num:
     hash_list[i]+=1
print(hash_list)    



# Problem 3: The Unique Element Finder (batana hai kaunse numbers list mein sirf 1 baar aaye hain.)
# Timecompexcity = O(n+k) = O(n)   k for second loop jo only freq map ke liye chla limited no ke liye 
# output = {1: 2, 2: 2, 3: 1, 4: 2, 5: 1}
# 3
# 5

arr = [1, 2, 3, 2, 1, 4, 5, 4]
freq_map = dict()
for i in range(len(arr)):

    if arr[i] in freq_map:
        freq_map[arr[i]]+=1
    else:
        freq_map[arr[i]]=1    
print(freq_map)
    #    ye loop freq map ko scan krega or jo 1 bar aaya usko retrun krega unique no. 
for key in freq_map:
   if  freq_map[key]==1:
      print(key)


# METHOD 2 OPTIMAL SOLUTION for count the no. of indexing in list or dict
# OUTPUT={1: 2, 4: 3, 6: 1, 7: 1, 8: 1, 9: 1, 5: 2, 2: 2, 3: 1}
# 6
# 7
# 8
# 9
# 3

arr = [1,4,6,7,8,9,5, 2, 3, 2, 1, 4, 5, 4] 
hash_map= dict()
for i in range(len(arr)):
    hash_map[arr[i]]= hash_map.get(arr[i],0)+1
print(hash_map)    
for key in hash_map:
    if hash_map[key]==1:
        print(key)


# Problem 4=  [m] list ke item [num]  me hai ya nhi or hai toi kitni baar hai using dict / frequency map  

num = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 9, 2, 5, 6, 10, 67, 2]

freq_map = dict()
for i in range (len(num)):
    if num[i] in freq_map:
        freq_map[num[i]]+=1
    else:
        freq_map[num[i]]=1
        
for j in range (len(m)):
    if m[j] in freq_map:
        print("milgya bhai ", freq_map)
    else:
        print("bhai hai hi nhi" ,m[j])


print("final bta de ab ", freq_map.get(5,0))  






# Problem =5 Charcter Hashing Using Ascii code formulla ascii_val-97  for small charcter a to z
# output= 0
# 6
# 4
# 3
# 0
# Timecomplexcity = O(m+n) 


s= "azyzxytuvwaaaaabbbbcccg"
q=["q","a","b","c","k"]

hash_list= [0]*26
for ch in s:
    ascii_val= ord(ch)
    index= ascii_val-97
    hash_list[index]+=1
for ch in q :
    ascii_val= ord(ch)
    index= ascii_val-97
    print(hash_list[index])