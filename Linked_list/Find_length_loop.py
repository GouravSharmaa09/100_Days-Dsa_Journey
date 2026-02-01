# DAY-28     FIND THE LENGTH OF LOOP 

# Method -1 Brute Force 

# Time and complexcity = O(N)   S.C=O(N)

class solution :
    
    def find_loop(self,head):
        temp = head
        count=0
        my_dict=dict() # use a dict for find the len 

        while temp is not None :
            if temp in my_dict:
                return  count-my_dict[temp]  #logic - agr temp mila dict me to temp ko - krdo jo count hai usse total length of loop miljyegi
            my_dict[temp]=count # count or temp ke key:val pair bna rhe hai kon kitni bar aaya 
            count+=1
            temp=temp.next

        return 0



#  Optimal Solution [Using - Floodys cyclic algo ortortoise method ]

# Logic - Slow and fast ke equal hone tk ek loop and uske bd slow ko single single iterate kravye count+=1 ke sth and vps fast pe aate hi count miljyega humko 

# Time and complexcity = O(N), S.C=O(1)
class solution:
    def len_loop(self,head):
        fast=head
        slow=head
    

        while fast is not None and fast.next is not None :
            slow = slow.next
            fast=fast.next.next
            
            if slow == fast: # gr ye euqal hote hai to 
                slow=slow.next # slow ko iterate kro 
                # count ko q1 krdo 
                count=1

                while slow!=fast: # loop tb tk chlao jb tk not equal hai ye 
                    slow=slow.next # slow ko x ar itertae kro 
                    count+=1 # count ko bhi +1 increase kro  
                
                return count    
        return 0             
