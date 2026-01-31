# DAY-27     Leatcode Problem -876   [Find the mid in the list ]

# Method 1 - Brute force 
# logic = Using count //2 count nikal ke uska half 

# Time and complexcity = O(N+N/2)= O(n)

class Node:   # node creation class 
    def __init__(self, val):  
        self.val = val 
        self.next = None


class solution:
 # mid ka function    
    def mid_list(self,head):
       count=0
       temp=head
# phle iterate kro ek baar count krne ke liye 
       while temp is not None:
          temp=temp.next
          count+=1
       temp=head 
       # ab iterate kro count //2 tk mid nikl jyega 
       for i in range (0,count//2):
           temp=temp.next

       return temp

   
           
head=Node(1)
head.next =Node(3)
head.next.next=Node(5)
head.next.next.next=Node(7)
head.next.next.next.next=Node(9)


sol=solution()  # obj of class 
mid=sol.mid_list(head) 


print(mid.val)  # O/P= 5
       


# Method - 2   Using Tortoise Method 

# logic =  Fast and slow   
# Fast --- Iterated 2x  where slow--- iterated x times 
# Fast iterated like Fst !=none or fast.next !=none so end me slow jispe hoga vo mid hoga 

# Time and complexcity = O (n/2)

class Node:   # node creation class 
    def __init__(self, val):  
        self.val = val 
        self.next = None



class solution:
    def midnode(self,head):
        fast=head  # fast 2x ke liye 
        slow=head  # ye x bar iterate ke liye 
        while fast is not None and fast.next is not None : # condition loop fail hone ki 
           
            slow= slow.next # slow ek bar 
            fast = fast.next.next # ye 2 bar chlega 

        return slow  # slow return krege kyuki mid ye hi hai ab     


head = Node(4)
head.next = Node(6)
head.next.next = Node(8)
head.next.next.next = Node(10)
head.next.next.next.next = Node(12)
head.next.next.next.next.next = Node(14)
head.next.next.next.next.next.next = Node(16)

newsol=solution()
mid2=newsol.midnode(head)

print(mid2.val)  #O/P=10