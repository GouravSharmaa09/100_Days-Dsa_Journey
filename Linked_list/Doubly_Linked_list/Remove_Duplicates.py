# DAY - 31   REMOVE THE DUPLICATES IN THE SORTED ARRAY 
# LOGIC = PREV AGR == CURR HAI TO DEL KRO (LINK TODO )

class solution:
    def remove_duplicate(self,head):
        prev=None
        curr=head

        while curr is not None:
            if curr.prev and curr.prev.val==curr.val: # curr prev hai and prev ki val or curr ki equal hai to 
                if curr.prev==head: # curr ka pre head hai to (duplicate head pe hai to )
                    # prev ko none kro 
                    curr.prev=None
                    # curr ko head bnao 
                    head=curr
                
                # mid ke liye 
                else:
                    # curr ke prev ke prev ka next ko curr link kro   
                    curr.prev.prev.next=curr
                    # curr ke prev ko curr ke prev ke prev se link kro 
                    curr.prev=curr.prev.prev

            curr= curr.next # find more duplicates in list 
        
        return head     

# Time and complexcity = O(N)
# S.C= O(1)        