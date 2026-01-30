# Day-26       Method 2- Traversal  
# 




class node :     # node creation ki class 
    def __init__(self,val):
        self.val=val
        self.next=None

class singlylinkedlist: # singliy linked list ki class head bnana eke liye 
    def __init__(self):
        self.head=None

    def travesal(self):  # Travesal 
        if not self.head : # agr list empty hai to 
             print("sll is empty")

        else: 
            current = self.head
            while current is not None:  # curr none nhi hai to 
                print(current.val,end=" -->") # value print kro 
                current=current.next # or aage chlte jao 
            print()         
