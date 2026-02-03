# DAY-30    DOUBLY LINKED LIST 
# NOTE- IT STORES PREVIOUS , DATA , OR NEXT ADDRESSS 

# CREATE A NODE :
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None


# doubly ll 
class doubly:
    def __init__(self):
        self.head=None

    # INSERT AT HEAD
    def insert_head(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
        else:
            new_node.next=self.head # new ke next ko head se link kiya 
            # head ke previous ko new node se connect kiya 
            self.head.prev=new_node
            # insert at head
            self.head=new_node    


# 2. APPEND 

    def append(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node 
        else:
            current= self.head
            while current.next is not None :
                  current=current.next    
            
            current.next=new_node
            new_node.prev=current 


# 3. Insert at mid/between
    
    def insert_mid(self,val,position):
        new_node=Node(val)
        if position==0:
            self.insert_head(val)

        curr=self.head 
        count=0
        while curr  and count <position-1: 
            curr=curr.next
            count+=1

        if curr is None: # agr position list me nhi hai to 
            print("position does not exits")
            return 

        new_node.next=curr.next 
        new_node.prev=curr

        if curr.next : # curr ka next none hai to means last me hai to 
            curr.next.prev=new_node # new node se change krege next ke pre ko 
            curr.next=new_node # curr ke next ko newnode bnayege 


# 4.Traverse 

    def traverse(self,val):
        new_node=Node(val)
        if self.head is None: # agr head none hai to 
            print("DLL is empty")

        else:
            temp=self.head
            # temp none tk ka loop 
            while temp is not None :
                print(temp.val, end=" ") # val print kro space ke sth 
                temp=temp.next
            
            print()



# 5. Delete head , end , and between :

    
    def delete_head(self,val):
        # case 0 list khali hai to 
        if not self.head:
            print("khali list hai ")
            return 

        temp = self.head 
        
        # case 1 head delete 
        if temp.val==val:
            self.head=temp.next # head ko agle box me shift kia 
            if self.head: # condition ki agla dabba exits krta hai to 
                self.head.prev=None # uska prev saaf kia means dlt 
            return 
        # target dhoondo 
        while temp and temp.val!=val :
            temp=temp.next
# value list me nhi mili to 
        if not temp :
            print("value nhi mili bhai list me ")
            return 

        # case 2 last (tail delete ke liye )
            

        if temp.next is None:
            if temp.prev:
               temp.prev.next=None # last vale ka next ko none se update kiya 
            return 
        
        # middle element delete 
        else:
            temp.prev.next=temp.next #  pichle vale ka next update kiya 
            temp.next.prev=temp.prev # agle vle ka prev update kiya  




