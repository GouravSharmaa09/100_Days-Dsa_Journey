# DAY-29     Rearrange the nodes and Return Odd and even (index)   leat code - 328

# Method -1 Brute Force  Using (list - space )

# Time and complexcity = O(2n)=O(n) and SPACE AND COMPLEXCITY = O(n)
 
  #   o   e   o   e   o   e   o         o= odd and e = even 
# ll= 8-->7-->1-->5-->6-->4-->3-->None  

class solution:
    def oddeven(self,head):
        if head is None or head.next is None:
            return head # agr list me ek item hai to head return kro mtlb ek item hi 
        
        temp=head
        values=[] # extra space to store odd and even value in a sequence 

        while temp and temp.next:  # odd ke liye 
            values.append(temp.val)  # append kro values list ke andr temp ki values 
            temp=temp.next.next

        temp=head.next # even ke liye 
        while temp and temp.next : # ye even ke liye hai 
            values.append(temp.val)
            temp=temp.next.next # ek skip krke 

        temp = head 
        index=0 

        while temp is not None: # arrange krne ke liye list ko 
            temp.val=values[index] # values hai temp ki unko index ke accourding change kro 
            index+=1 
            temp=temp.next

        return head      


#Question = return odd even index but in sequence of same linst linke first return odd one and after that even 
# Method -2  Optimal Solution 
# using -->  two var  Odd and even where skip one node and break link and conncet to odd one for odd and even one for even  

# Time and complexcity = O(n/2)=O(n)  ,  S.C=O(1)

class solution:
    def oddeven_optimal(self,head):
          if head is None or head.next is None: # base case for list empty condition me 
            return head 
          
          odd=head 
          even=head.next
          even_head=even # store second head to even (for linking end with odd in last ) 

          while even is not None and even.next is not None :  # loop j tk chlao jb tk even none na ho ya uska next because even phle None hoga 
               
               odd.next=odd.next.next # odd ke next ko ek skip krke link kro 
               odd=odd.next # odd ko new odd next se link kro 
               even.next=even.next.next# same here for even 
               even = even.next

          odd.next=even_head # after loop over odd ke next ko even head se link krdo 
          
          return head      


  #   o   e   o   e   o   e   o         o= odd and e = even 
# ll= 8-->7-->1-->5-->6-->4-->3-->None  





