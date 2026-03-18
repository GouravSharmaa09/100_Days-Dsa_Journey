# DAY-51  N meetings In a room (job secduling) 
# Maximum meetings in a room 
# logic - using Two pointer 

class meeting :

    def __init__(self,start,end,pos):
        self.start=start
        self.end=end
        self.pos=pos
    
def maxmeeting(start,end):
    n=len(start)

    meet=[meeting(start[i],end[i],i+1)for i in range (n)]  # creating a obj list for both end and start 

    meet.sort(key=lambda x:(x.end,x.start)) # end time ke basis pe list ko sort kiya 

    result=[]
    count=1

    last_time=meet[0].end  # last time ko update kro like (pehli meeting to hogi )

    for i in range (1,n):
        if meet[i].start>last_time: # agr start last time se greater hai to 

           count+=1 # increase count 
           result.append(meet[i].pos) # result me pos append kro 

           last_time=meet[i].end

    return count 


start=[1,3,0,5,8,5]
end=[2,4,6,7,9,9]

print(maxmeeting(start,end))


# T.C=O(N)    S.C=O(N)