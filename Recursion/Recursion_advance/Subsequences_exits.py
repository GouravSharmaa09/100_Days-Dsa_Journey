# DAY-35      IF THERE EXITS sum of SUBSEQUNCES == K THEN RETURN TRUE AND FLASE 

# Logic =  same sum of subsequnces like in this we only return if there are any of one exits 
def solve(nums):
   result=[]
   total=0

   def sum_sequnces(index,total,subset):
     if total==k:
        result.append(list(subset))
        return True  # value exits krti hai to true return hoga 
    
     elif total>k:
        return False

     elif index>=len(nums):
        return False

     subset.append(nums[index])
     sum=total+nums[index]

     pick=sum_sequnces(index+1,sum,subset) 
     # agr pick true hai to idr se hi true return kro aage dekhne ki need nhi hai 
     if pick ==True:
        return True

     subset.pop() # pop kro non pick dekhne  ke liye 
     sum=total  # total ko reset krdo 
     # not pick hai to false do 
     not_pick=sum_sequnces(index+1,sum,subset)    
    
     return not_pick 

   
   return sum_sequnces(0,0,[])
   

k=4
print(solve([1,2,3,4]))  # True

# Time and complexcity =O(2N)  AD SPACE = O(N)