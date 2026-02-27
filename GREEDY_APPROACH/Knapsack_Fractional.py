# DAY-50    KNAPSACK FRACTIONAL   USING GREEDY 
# INSTITUION --> WEIGHT KO MAXIMUM PROFIT KE ACCORUDING PICK KRO 
# FIRST FIND THE RATIO OF ARR AND ARRANGE WITH MAXIMUM FIRST IN THE STRT THEN COMPARE OR IF  W < AND CURR_W IS SMALL THEN WE ALSO PUT FRACTIONAL OF IT 

class Item:
    def __init__(self,val,weight):
        self.val=val
        self.weight=weight




class solution:
    def knapsack(self,val,weight,capacity):
        
        n=len(val)
        items = [Item(val[i], weight[i]) for i in range(n)]  #Objects ki list banayi

# lambda function sort krne ke liye ration nikanle ke liye or revrse true isliye ki arr ko sort hone ke bd sort krna hai kyuki descending order me chyiye 
        items.sort(key=lambda x: x.val/x.weight,reverse =True) # ratio find kiya 

        curr_w=0
        final_val=0
        

        for i in items:
            if curr_w + i.weight<=capacity: # afr curr weight less hai capacity to 
                curr_w=curr_w+i.weight  # curr weight me weight add kro  
                final_val+=i.val # final me val ad kro uski 

            else: # agr capacity less than ho weight se to reamin fraction do 
                remain= capacity-curr_w 
                cost=i.val/i.weight * remain # divide or remain ka multiply krke 

                final_val+=cost
                break
    
        return final_val      


   



# T.C= O(N LOG N )+O(N)   S.C= O(1)

v = [60, 100, 120]
w = [10, 20, 30]
cap = 50
sol=solution()

print(sol.knapsack(v,w,cap))      #    O/P # 240.0 