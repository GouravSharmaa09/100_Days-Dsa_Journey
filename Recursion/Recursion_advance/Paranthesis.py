# DAY-36    GERNATE THE PARANTHESIS            LEATCODE-22
# Logic - Pick open and close accourding to index , n*2 no. of brackes hoge total dono ko milake 
# codnition , 1-- sum negative hote hi return 
# 2. sum half se jyda hote hi open ka return kro 
#3. last index pe total 0 milne pe append kro 



def solve (index,total,bracket,result):
    if index>=len(bracket): # LAST INDEX PE 
        if total==0: # 0 MILTE HI APPEND KRO 
            result.append("".join(bracket)) # JOIN KRKE STRINGS KO 
        return 
   
   # AGR TOTAL - ME HAI AND OPEN BRACTES HALF SE JYDA HAI TO RETURN KRO 
    if total<0 or total>len(bracket)//2:
        return 
   
    #PICK OPEN BRACKET 
    bracket[index]="(" # OPEN BRACKET SE START KRO VRNA NEGATIVE- VALI CONDITION AAJYEGI 
    solve(index+1,total+1,bracket,result) # FUNC CALL  RERCUSION   
    
    # PICK CLOSE ONE 
    bracket[index]=")"
    solve(index+1,total-1,bracket,result)

def PARANTHESIS(N):
    n=3
    bracket=[""]*(2*n) # FORMULLA NUMBER PTA KRNE KA brakcets ka 2n
    result=[]
    solve(0,0,bracket,result) 
    return result

print(PARANTHESIS(3))
#OUTPUT=['((()))', '(()())', '(())()', '()(())', '()()()']


# Time and complexcity = O(2N)
# S.C--O(2N)