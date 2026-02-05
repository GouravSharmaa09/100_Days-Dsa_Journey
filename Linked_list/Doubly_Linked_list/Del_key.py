# DAY-31    DELETE ALL OCCURENCE KEY IN THE LIST (KEY KO LIST ME JHA JHA AARI HAI VAHA SE DEL KRO )
# Logic = prev or curr ko move kro agr value curr ke equal ho to node ko del kro by linking change 

class solution :
    def del_key(self,head,key):
        
        if head.next is not None and head.val == key :
               return None
        prev=None
        curr=head
        new_head=head # head isliye store kia kyu ki wrost case me head bhi duplicate key hua to 

        while curr is not None: 
            if curr.val == key : # codndition 
                if prev is not None: # agr prev none nhi hai to 
                    prev.next =curr.next # prev ke next ko curr ka next se link rko 
                                 
                if curr.next is not None: # curr ka next none nhi hai to 
                    curr.next.prev=prev  # next ke prev ko prev bnao 

                if curr == new_head: # agr head pe hai key to 
                    new_head = new_head.next  # head ke next ko new head bolo 
            prev=curr 
            curr=curr.next
        
        return new_head                      

# Time and complexciy- O(n)
# Space and complexcity= O(1)