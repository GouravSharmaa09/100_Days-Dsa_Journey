# DAY-26            SINGLY LINKED LIST 

class node :
    def __init__(self,val):
        self.val=val
        self.next=None

class singlylinkedlist:
    def __init__(self):
        self.head=None

# Note- Index first ko Head se point krte hai 

# Method -1   APPEND(ADD KRNA NODE OR VALUES)

class node :     # node creation ki class 
    def __init__(self,val):
        self.val=val
        self.next=None

class singlylinkedlist: # singliy linked list ki class head bnana eke liye 
    def __init__(self):
        self.head=None

    # append method 
    def append(self,val):  
        new_node=node(val) # new node me node class se val daali 
        if self.head==None: # head none hai to 
            self.head=new_node # head ko new node bnao  
        else:
            current=self.head # else current bnao 
            while current.next is not None: # current none nhi hai to 
                current=current.next # cuurent ko next kro 
            # end me aate aate current .next = new node hojyega jb ye loop khatam hoga 
            current.next=new_node

    def display(self): # display fun hai o/p ke liye 
        current=self.head # current ko head bnao 
        while current is not None: # current none nhi hai to 
            print(current.val,end=" --->") # current ki value 
            current = current.next 
        print("None")            

my_list=singlylinkedlist()

my_list.append(46)
my_list.append(50)
my_list.display()

# O/P= 46 --->50 --->None






