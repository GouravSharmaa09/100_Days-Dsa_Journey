# DAY-31   FIND THE PAIRS AND GIVEN SUM IN THE SORTED LIST :

# Method - 1 Brute force 
# logic -  Ek ko fix krke dusre se compare krte chlo (temp 1 ko head pe rhk ke temp 2 ko loop kro or compare kro baari baari )

class solution :
    def find_pair1(self,head,target):
        temp1=head 
        result=[]

        while temp1 is not None:
            temp2=temp1.next  # temp ke next ko temp 2 maana 
                                     
            while temp2 is not None: 
                  if temp1.val + temp2.val == target: # agr dono ka sum equal hai target ke to 
                      result.append([temp1.val,temp2.val]) # append in list 
                #   else agle se compare kro 
                  temp2=temp2.next
            temp1=temp1.next  # 1 ko change kro or same process flow kro 

        return result        
# T.C = O(N+(N+1)/2) = O(N^2)
# S.C = O(1)


# Method -2 Better approach 
# USING - HASH MAP (SET ) formulla -(remaining = target - val)

class solution :
    def find_pair2(self,head,target):
        my_set=set()
        temp=head
        result=[]

        while temp is not None :
            remaining = target-temp.val # formulla agr remaining set me milta hai to 
            if remaining in my_set :
                result.apped([remaining,temp.val])

            my_set.add(temp.val) # set me add krte rho val ko 
            temp=temp.next

        return result

    # T.C = O(n),    S.C= O(N)-EXTRA VAR KE LIYE 
                 
# Method-3    Optimal (Using Two pointer)

class solution :
    def find_pair3(self,head,target):
        right=head  
        left=head 
        result=[]
       
        # right end me phuchaya pointer ko
        while right.next is not None: 
            right = right.next 
        
        # agr left and right none nhi ho or left ki val less ho right ki se to 
        while left is not None and right is not None and left.val<right.val:
            # left.val<right.val sirf unquine numbers in a list ke liye hai but 
            # agr duplicates huye to left!=right nd right.next!=left condition chk krni pdegi 
            
            # sum nikala
            total = left.val+right.val
            # agr pair mila 
            if total == target :
                # append kro list me or agla pair dundo 
                result.append([left.val,right.val])
                # dono ko aage bhao right prev side or left next side 
                left=left.next
                right= right.prev
            # agr taotal bda ho target se to 
            elif total>target:
                # right ko prev side decrease kro 
                right = right.prev
            
            else:
                 left = left.next

        return result                 


# T.C= O(N+N)=O(2N)=O(N)
# S.C= O(1)



