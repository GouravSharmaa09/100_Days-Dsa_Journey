# DAY-45   MIN STACK    LEAT CODE -->155
# LOGIC = GET MIN BTANA HAI O(1) ME 

# LOGIC -->  STACK ME PUSH LIST KREGE VAL KE STH AND 
# AGR STCK EMPTY HAI TO VAL KO MIN BNYEGE ELSE PREVIOUS OR NEXT KA MIN NIKALEGE 

class min_stack:
    def __init__ (self):
         self.stack=[]
   

   # push fun 
    def push(self,val):     #o(1)
        if len(self.stack)==0:
            # runing minimum store kr rha agr stck empty hai to jo val hai usko hi minim mano 
            self.stack.append([val,val])  # list append ki stack me 

        else:
           # minimum nikala -1 is top and 1 is last val 
            mini= min(self.stack[-1][1],val)

            self.stack.append([val,mini])

    def pop(self):  #o(1)
        if self.stack:
            
             self.stack.pop()

    
    def top(self):    #o(1)
        if not self.stack:
            return None
        return self.stack[-1][0]

    
    def gey_min(self):       # o(1)
        if not self.stack:
            return None
        return self.stack[-1][1]



    #   T.c=o(1)   s.c=O(N)  
