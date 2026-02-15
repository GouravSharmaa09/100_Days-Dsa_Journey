# DAY-44   STACK IMPLEMANTATION USING QUEUES (DEQUE)
# QUEUE KA USE KRNA HAI BUT  STACK IMPLEMNT KRNA HAI QUEUE OPERATIONS SE ---> FIFO TO LIFO 

# USE DEQUE --> BOTH END SE OPERATION PERSOM KR SKTE HAI BUT USING DEQUE O(1) ME OPERATIONS PERFORM KRTE HAI 
# --> N-1 ROTATE KRNI HAI LIST KO THEN USING N-1 ROTATE POPLEFT()


from collections import deque 

class stack_deque:

    def __init__(self):

        self.queue=deque() # BOTH END PE OPERATION PERFORM KRTI HAI O(1)ME 

    def push(self,x):
       
        self.queue.append(x)

        for _ in range (len(self.queue)-1): # n-1  kro 
            self.queue.append(self.queue.popleft()) # left ko pop krke end me laao 

    def pop(self):

        if len(self.queue)==0:
            return "empty stck hai "
        return self.queue.popleft() # last item 

    def top(self):

        if len(self.queue)==0:
            return "empty stck hai "
        return self.queue[0]  # top item 

    def is_empty(self):
        return len(self.queue)==0 # true false 


s= stack_deque()
s.push(100)
s.push(200)
s.push(300)
s.pop()

print("Top element:", s.top())    
print("Popped:", s.pop())        # Output: Top element: 200
                                 # Popped: 200 
                                 # New Top: 100
print("New Top:", s.top())

# Time and complexcity = O(1)
