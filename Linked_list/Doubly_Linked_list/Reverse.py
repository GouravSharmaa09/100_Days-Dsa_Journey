# DAY-31       REVERSE A LIST 
# logic = three pointer and (ulta chlao ) only swap the pointers 

class solution :
    def reverse_list(self,head):
        if head.next is not None :
            return head 
        curr = head
        prev= None

        while curr is not None :
            # Dll me ulta chlte hai to jo prev hoga vo next or next prev 
            front = curr.next # next ko front bola 
            curr.next=prev # next prev hoga kyuki Dll me ulta chlte hai 
            curr.prev=front # prev next hoga (front)
            prev=curr # prev curr hojyega ab 
            curr=front # or curr front 

        return prev 

# Time and complexcity = O(n)
# Space and complexcity = O(1)        

