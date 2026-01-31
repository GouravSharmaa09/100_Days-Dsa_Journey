# Day-27     REVERSE A LINKED LIST 

# Method -1  Brute force [Using Stack memory space pop and append logic]

# Time and complexcity = O(2N)= O(n)
# S.C= O(n)

class Node:   # node creation class 
    def __init__(self, val):  
        self.val = val 
        self.next = None


class solution :
    def reverse_list(self,head):
        temp = head
        stack=[]  # Use stack for memo

        while temp is not None:
            stack.append(temp.val)   # append krege stack me all list ki value ek ek kreke 
            temp=temp.next

        temp = head

        while temp is not None:
            e=stack.pop() # pop the val using Lifo last vala sbse phle 
            temp.val = e # value change hori hai in this not proper reverse thats whywe use optimal 
            temp=temp.next

        return head      

head=Node(3)
head.next=Node(6)
head.next.next=Node(9)
head.next.next.next=Node(0)
head.next.next.next.next=Node(10)

sol=solution()

rev=sol.reverse_list(head)

print(rev.val)  #O/p=10





# Method-2    Optimal [ Using -- Prev,temp and front var ka use krke ]
# 
# logic - prev ko none rhkge ke and temp.next ko prev se change krdege and temp ko front se 


# Time and complecity = O(n), S.C - O(1)  

class Node:   # node creation class 
    def __init__(self, val):  
        self.val = val 
        self.next = None


class solution :
    def optimal_rev(self,head):
        temp = head
        prev=None # prev ko none rhka 

        while temp is not None:
            front=temp.next # temp ka next front hoga 
            temp.next=prev #jo prev hai usko temp ke next se change kro 
            prev=temp # prev ko temp bnaya 
            temp=front # temp ko front 
        
        return prev # prev ko return krege jo ki head bhi hoga 
        # puri chain reverse ho chuki hai 

# Note- Leat code ne proper reverse nhi reverse head managa return thats heads prev hoga  

head=Node(13)
head.next=Node(6)
head.next.next=Node(19)
head.next.next.next=Node(10)
head.next.next.next.next=Node(14)

sol=solution()

revv=sol.optimal_rev(head)

print(revv.val)  #O/P = 14

  