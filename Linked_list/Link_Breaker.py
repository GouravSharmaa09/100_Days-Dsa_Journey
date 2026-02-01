# DAY-28      LINK BREAKER (LIST KO X ME SE BREAK KRNI HAI )

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class singlylinkedlist:
    def __init__(self):
        self.head=None

    def append(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
           
        else :
            current=self.head
            while current.next is not None:
                current=current.next

            current.next=new_node    

# ye hai asli logic function for Link breaker 

    def link_breaker(self,x):   #
        temp=self.head

        while temp is not None :
            if temp.val == x : # agr x ke equal ho to aage ka k kro 
                break
            temp=temp.next

        if temp: # agter val equal ke 
            head_2=temp.next # temp ke next ko head 2 bnao 
            temp.next=None # jo next tha usko none kro or link todo phlevli list se 
            return head_2 # head 2 do jo ki gli list ka start bhi h 
        else:

            return None     

    def display(self):
        current=self.head
        while current is not None:
            print(current.val,end=" --->")
            current = current.next
        print("None!")


breaklink= singlylinkedlist()

for v in [20,34,56,65,32]:
    breaklink.append(v)

print("original")
breaklink.display()     
# O/P = original  20 --->34 --->56 --->65 --->32 --->None!


head2 = breaklink.link_breaker(56)
# break ke bd --20 --->34 --->56 --->None!

breaklink.display()



