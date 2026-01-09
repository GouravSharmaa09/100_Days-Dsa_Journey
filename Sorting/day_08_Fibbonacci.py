# Level 1: The "Zero-Hero" Challenge   
#  shift the all zeros at the end form list 

num= [0, 1, 0, 3, 12] 
pos=0
for i in range (len(num)):
    if num[i]!= 0 :
        # swap the 0 with number 
        num[i],num[pos]= num[pos],num[i]
        #  pos ki value increase krdo agr 0 na mile to     
        pos+=1
print(num)        




# Problem 2 = Fiboonacci number    ye vo no. hote hai jiske past 2 ka sum 3 vale ka ho 
# fibbonacci series = f : 0  1  1  2  3  5  8 13


def fibbonacci(num):
     if num ==0 or num==1: 
        # base condition agr 1 ya 0 hai to num retrun kro 
        return num 
     return fibbonacci(num-1) + fibbonacci(num-2)
    #   logic formulla ki pichle 2 number ka sum return kro 
print(fibbonacci(6))        
# fibbonacci no. in the series hai ye 








# problem 3 = The "Twin Finder"   check karo kiska count 1 hai.   

num =[2, 4, 7, 2, 7]

freq_map= dict()
for i in num:
    if i in freq_map:
        freq_map[i]+=1
    else:
        freq_map[i]=1
for key in freq_map:
    if freq_map[key]==1:
        print(key)            


