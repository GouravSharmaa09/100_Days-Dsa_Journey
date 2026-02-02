# DAY-29      Remove node from Nth place from end of list        leatcode-19


# Method - 1  Brute force (using- count and length logic )


class solution :
    def remove_Nth(self,head):
        length=0 # length ke liye 
        temp=head
        while temp is not None: # length count ke liye loop iterate kr rha hai 
            length+=1 
            temp=temp.next
        # Base case agr legth n ke eual hai to 0 positiion item ko del krna hai to head.next reurn krdo 
        if length ==n :
            return head.next

        stop = length - n # logic formulla len-n krne pe jo aayega vo Nth place hai 
        count=1
        temp=head

        while count<stop : # count less hai stop se t tk chlao loop ko 
            temp=temp.next
            count+=1 

        temp.next=temp.next.next  # delete hogya Nth item 
        return head       
# Time and complexcity = O(N+N)=O(N),   S.C=O(N)




# Method - 2  Optimal Solution 
# Logic - Two person ek person Nth bar ieterte krega then both person single time ieterte kree loop end tk and jo seondperson jidr hoga vo Nth place hoga 


class solution:
    def del_Nth(self, head):
        slow,fast=head,head

        for _ in range (n): # Nth tk ke liye loop 
            slow=slow.next

        if slow is None  : #Base case for agr nth kadam chlne ke bd node none hogya to head hi uthao 
            return head.next

        while  slow.next is not None : # None hone tk loop chlao 
            slow = slow.next # ek ek kreke iterate kro 
            fast=fast.next

        fast.next=fast.next.next # del the node ( by changing the link of node )
        
        return head

    # Time and complexcity = O(n) , S.C=O(1)    

# Note - Slow pointer ko phle N kadam aage bhja usin for loop 
# Ab slow and fast dono ko ek ek krke aage bhado jb tk slow None tk na phcuh jyega inke bich ka gap hmesha N rhega 
