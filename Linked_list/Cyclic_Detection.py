# DAY-28    FIND CYCLIC IN THE LIST AND RETURN TRUE AND FALSE    LEAT-CODE= 141 [Flodys Cyclic Detection]

# METHOD -1  BRUTE FORCE  Using set 

# Time and complexcity = O(N)
# SPACE .COMPLEXCITY = O(N)
class solution :
    def cyclic(self,head):
       
        temp=head
        my_set=set() 
        while temp is not None: 
            if temp in my_set: # temp store kr rhe hai pura object value nhi kyuki value krte to duplicates case me dikkt hoti  
                return True # cycle hai qki double miljayegi value 

            my_set.add(temp) 
            temp=temp.next
        return False      


# Method - 2  Optimal  [ Floyd’s Cycle-Finding Algorithm  (Tortoise Fast and slow)]
# Logic= Fast slow ke equal aajye to cyclic hai else Cyclic nhi hai 
# 
# Time and complexcity = O(n)  and S.C= O(1)

class solution :
    def has_cycle(self,head):
            fast =head # ye 2x iterate krega 
            slow=head # x bar iterate krega 
            while fast is not None and fast.next is not None :
                slow = slow.next  
                fast = fast.next.next
                if slow==fast:  # both are in same place 
                    return True # cycle hai 

            return False  # nhi hai qki equal nhi hua slow or fast 




# Question 2 - Find cycle Stating point  Leat code 142

# Brute -Force 
# 
#Logic- Jab hum ek-ek node ko set mein daalte hain, aur koi node dobara dikh jata hai, toh iska matlab hai ki hum usi circle mein wapas aa gaye hain
class solution :
    def starting_cycle(self,head):
       
        temp=head
        my_set=set() 
        while temp is not None: 
            if temp in my_set: # temp store kr rhe hai pura object value nhi kyuki value krte to duplicates case me dikkt hoti  
                return temp # cycle hai qki double miljayegi value 

            my_set.add(temp) 
            temp=temp.next
        
        return None # nhi hai to None do 




   # Optimal Solution 
              
#Logic- Solw and fast ke equal hone pe slow ko head pe send kro kyuki same distace hota hai 
# fast and slow me itertaion ka and boths ko single single iterate kro until dono  vps equal an ho jis point pe onge vo start hoga cycle ka 

class solution :
    
    def has_start_cycle(self, head):
       fast,slow=head,head

       while fast is not None and fast.next is not None : 
          fast= fast.next.next
          slow=slow.next
          
          if slow == fast :
             slow=head # slow ko head pe bhja 
             
             while slow !=fast: # loop jb tk not equal hai 
                 slow=slow.next  # +=1
                 fast=fast.next # +=1 iterate kro until both equal same point pe na aajye 
                 # same point pe aane ke bd loop se bhaar ksii ek ko retrun kro 
             return slow  # start point 
             
             # else None cycle nhi hai 
       return None        






