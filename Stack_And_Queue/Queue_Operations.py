# DAY-42     QUEUE OPERATION [IMPLEMANTATION OF QUEUE USING ARR/LIST]  FIFO(FIST IN FIRST OUT )
# Queue perform 4 operations :
# 1. enqueue 
# 2. dequeue
# 3. front 
# 4. rear

# Note- Ye dono end se perform krskti hai 

class queue:
    def __init__(self):
        self.items = []

    def is_empty (self):
        return len(self.items)==0

    # PUSH VALA FUNCTION     T.C= O(1)
    def enqueue(self,item):
        self.items.append(item)
 
    # POP FUNCTION   T.C=O(N) --> pop krne pe shift hoge items 
    def dequeue(self):
        if len(self.items)==0:
            print("empty queue hai ")
            return
        x= self.items.pop(0) # pop 0 -->first item pop hoga 
        return x
    
    # first item func 
    def front(self):
        if len(self.items)==0:
            print("empty hai ")
            return 
        return self.items[0] # 0 th index pe hai first 
    
    # last item func
    def rear (self):
        if len(self.items)==0:
            print("empty hai ")
            return 
        return self.items[-1] # last -1 pe hoga (top)
    
    # size func
    def size (self):
        return len(self.items)
    
queue_obj = queue()

queue_obj.enqueue(20)
queue_obj.enqueue(300)
queue_obj.dequeue()
queue_obj.enqueue(6000)
queue_obj.enqueue(100)
queue_obj.dequeue()

print(queue_obj)
print("last item hai ",queue_obj.rear())
print("first item hai ",queue_obj.front())
print("queue mai item hai :",queue_obj.is_empty())
print("ye size hai ",queue_obj.size())

# Output :
# last item hai  100
# first item hai  6000
# queue mai item hai : False
# ye size hai  2

# Time and complexcity = O(N)
# S.C=O(1)
        

