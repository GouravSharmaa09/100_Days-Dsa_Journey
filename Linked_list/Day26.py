# DAY-26    Linked list Introduction 

# node create krne ka basic tarika 
class node:
    def __init__(self,val): # dunder function/consturtor or ye node create krne ke km aata hai 
        self.val=val
        self.next=None

node1=node(5)
node2=node(10)
node3=node(12)
node4=node(14) 

node1.next=node2
node2.next=node3
node3.next=node4     

print(node1.next.val)





