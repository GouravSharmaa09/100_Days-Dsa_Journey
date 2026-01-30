# DAY-26      INSERT AT SPECIFIC POSITION 

# Logic = privious val, count, current --> previous node , current or count leke chlege  


class node :
    def __init__(self,val):
        self.val=val
        self.next=None

class singlylinkedlist:
    def __init__(self):
        self.head=None


    def insert (self,val,position):   # INSERT FUN 
        new_node=node(val)  # NDOE ME VAL DAALO 
        if position == 0: # AGR POSITION 0 HAI TO NEW NODE KO HEAD BNAO 
            new_node.next=self.head 
            self.head=new_node # OR OLD HEAD KO NEW NODE SE REPLACE KRO 

        else:

            current=self.head   
            prev=None
            count=0
            while current is not None and count<position: #Jab tak position nahi milti ya list khatam nahi hoti
                prev=current
                current=current.next
                count+=1
            if prev is not None: #agar position valid hai (matlab prev None nahi hona chahiye)
                  prev.next=new_node
                  new_node.next=current #Naye ka hath agle (current) se jodo
    
    
    def display(self):
        temp = self.head  # DISPLY FUN DATA SHOW KRNE KE LIYE 
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")        


my_list=singlylinkedlist()


my_list.insert(10, 0)  # List: 10 -> None
my_list.insert(20, 1)  # List: 10 -> 20 -> None
my_list.insert(30, 2)


my_list.insert(100,1)

# O/P= 10 -> 100 -> 20 -> 30 -> None
my_list.display()



