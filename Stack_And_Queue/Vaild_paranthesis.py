# DAY-45    VAILD PARENTHISIS      leatcode-20
# LOGIC- all open brackets push and then pop or closing se compare kro /
# CONDITION 1 . Agr bracket does not match (compare ) false 
# 2.  stack is empty but closing bracket is still remain to false 
# 3.  stack not empty but closing bracket is not remain called false 



class Stack:

    def is_vaild ( self,s ):
        stack=[]

        # LOOP FOR ALL BRACKET CHK KRNE KE LIYE 
        for bracket in s:
            if bracket=="(" or bracket=="[" or bracket=="{" :

                stack.append(bracket)

            else:
                if len(stack)==0:
                    return False

                e= stack.pop()

                # COMPARE KREGA POP OR PUSH VALE KO (OPENING AND CLOSING KO )
                if (
                    (bracket==")" and e=="(") or 
                    (bracket=="]" and e=="[") or 
                    (bracket =="}" and e == "{")
                ):
                     continue 

                else:

                     return False 

        return len(stack)==0       


obj_stck= Stack()
result=obj_stck.is_vaild("{[]{}")
                     
                   
print(result) # False

# Time and complexcity = O(N) AND S.C=O(N)

