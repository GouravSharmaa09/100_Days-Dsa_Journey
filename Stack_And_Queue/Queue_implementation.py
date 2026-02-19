# DAY-44 QUEUE IMPLEMENTATION USING 2 STACKS     leatcode-232
# USING 2 STACK QUEUE IMPLEMNT KRNI HAI LIFO -->FIFO

# # LOGIC -> THERE ARE 4 CONTION 
# 1.T/F  ALL ELEMENT FORM STACK 1 TO STACK 2 
# 2. INSERT ELEMNT IN TO STACK 2 
# 3. T/F STACK 2 TO STACK 1 
# 4. POP TOP ELEMNT FROM STACK 1
# 5. RETURN TOP ELEMENT FROM STACK 1


class stack_queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self,x):
        while self.stack1:
            self.stack2.append(self.stack1.pop()) # stack agr khali hai to a1 me se pop kro 2 me append kro 

        self.stack1.append(x)  # vps 1 me append kro pir 
        
        while self.stack2:
            self.stack1.append(self.stack2.pop()) # same for stck 2 

   
    def pop (self):

        if not self.stack1:
            print("empty stack hai ")

            return -1 
        top_element= self.stack1.pop() # last elemnt pop kro 
        return top_element 
    
    def top(self):
         if not self.stack1:
            print("empty stack hai ")

            return -1 
         return self.stack1[-1] # last element  hi top hai
    
    def is_empty(self):
        return not self.stack1
    

s = stack_queue()
s.push(10)
s.push(20)
s.push(30)
print("Top element:", s.top())    
print("Popped:", s.pop())        
print("New Top:", s.top())
     
# Top element: 10
# Popped: 10 
# New Top: 20

# Time and complexcity -o(2n)--> o(n)