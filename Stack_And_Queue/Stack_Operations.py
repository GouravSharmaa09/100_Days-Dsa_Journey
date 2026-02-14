# DAY-42    STACK OPERATIONS [IMPLEMENTATION USING ARR/LIST]
# Stack = Work on LIFO[last in first out ] item can append or delete form one end only 

# operations --> there are 4 operations 
# 1. push
# 2. pop
# 3. size
# 4. top


class stack:

    def __init__(self):
        self.items=[] # ITEM NAM KI LIST BNAYI STORE KRNE KE LIYE 

    # EMPTY FUN CHK KREGA TRUE YA FALSE KI STCK EMPTY HAI YA NHI   gives O(1)
    def is_empty(self):
        return len(self.items)==0

    # APPEND KRTA HAI (PUSH )   gives O(1)
    def push(self,item):
        self.items.append(item)

    # POP FUNCTION gives O(1)
    def pop(self):
        if len(self.items)==0:
            return "cannot pop empty hai stack"
        x= self.items.pop()
        return x

    # TOP FUNCTION  gives O(1)
    def top(self):
         if len(self.items)==0:
            return "cannot find empty hai stack"
         
         return self.items[-1]

    # SIZE FUN      gives, O(1)
    def size(self):
        return len(self.items)


stack_obj = stack()
stack_obj.push(5)
stack_obj.push(10)
stack_obj.push(20)
print(stack_obj)
print("bhai ye item pop hogya stack me se :",stack_obj.pop())
print("Stack empty  :",stack_obj.is_empty())
print("bhai ye item Top pe hai  stack me  :",stack_obj.top()) 

# Output:
# bhai ye item pop hogya stack me se : 20
# Stack empty  : False
# bhai ye item Top pe hai  stack me  : 10

# Time and Complexcity = O(1), S.C = O(1)