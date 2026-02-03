# DAY-26 METHOD 3- DELETE
# T.C=O(N) 

class node :
    def __init__(self,val):
        self.val=val
        self.next=None

class singlylinkedlist:
    def __init__(self):
        self.head=None

    def delete (self,val):  # delte ka fun
        temp==self.head # temp (curr) me store krlege 

        if temp.next is not None:  # text ka next none ke euqal nhi tha ky 
            # temp val milgi 
            if temp.val==val:

                self.head==temp.next  #head ko temp ke next se   (del hojyega)
                return
            else:

                found=False # found isliye ki list me element nhi hua tio btyega 
                prev=None
                # Curr=self.head
                while temp is not None: # agr temp 
                    if temp.val==val: # val milgi to dound true hoga 
                        found=True
                        break
                    prev=temp # prev ko temp bnao 
                    temp=temp.next # or temp ko temp.next

                if found:  # found hone pe 
                    prev.next=temp.next  # prev ke next ko temp.next
                    return

                else:
                    print("not found ")
