# DAY 46    INFIX TO POSTFIX 
# operand = a to z , Ato Z , 0 to 9 
# operator = -+,*/, ^

# logic -  stack me push kro operands ko untinal low priorty opertor nhi milta 
# if low priority operator aata hai to pop kro until priority jyda na ho or unko add on kro operatore ke end me 


class solution :
    # priority set ki operators ki (priority func)

    def priority(self,ch):
        if ch =="-" or ch=="+":
            return 1
        if ch =="*" or ch=="/":
            return 2

        if ch =="^" :
            return 3
        return 0 

# main func 
    def infixtopostfix(self,s):
        stack=[] # stack hai append and pop operations perform honge 
        result=[]

#  iterate kre until stack me all operands na aaje 
        for char in s :
            if ("a" <= char <="z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
                result.append(char) # append all operands in result 

# agr char open bracket hua to stack me append krdo char            
            elif char =="(" :
                stack.append(char)

# agr char closing bracket hua to                 
            elif char == ")":
                # to tb tk pop kro elemnt jb tk opening na mile 
                while stack and stack[-1]!="(":
                    result.append(stack.pop()) # or result me append kro 
                stack.pop()

            else:
# else priority chk kro operator ki agr less hai to upr vala option perform kro else result me append kro pop krke 
                while stack and self.priority(stack[-1])>=self.priority(char):
                    result.append(stack.pop())

                stack.append(char)
        while stack:
            result.append (stack.pop())

        return  "".join(result)                        


# Time and complexcity --> O(N)



# dry run --> infix = a+b*c
# post fix = [a, b, c, *, +]  --> *abc+**