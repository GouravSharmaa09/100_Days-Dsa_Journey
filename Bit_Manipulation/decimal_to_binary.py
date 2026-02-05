# DAY-32           Bit manipulation     


# 1- CONVERT DECIMAL  IN TO BINARY
# LOGIC - 2 SE DIVIDED KRTE CHLO REMINDER BCHE TO 1 ELSE 0 AND END ME REVERSE KRO OUTPUT KO 

# Time and complexcity = O(log2N) , S.C=O(log2N)

def convertbinary(num:int)->str:
    result=""  # ans string me chyiye 

    while num >0: # agr number 0 se bda ho tb tk 
        if num%2==1: # agr reminder 1 hai to 
            result +='1' # result me 1 add kro 
        else: # else 0 add kro 
            result+='0' 
        # 2 ka divide krte chlo 
        num=num//2           
    result=result[::-1] # end me result ko reverse krne pe binaray mil jyega 
    return result

print(convertbinary(14))    # O/P=1110




# 2.-- Convert binary in to decimal 

# logic = indexing kro right side se and power nikalo (2**1 hai to 1 0 hai to 0 )

def convertdecimal(num:str)->int:
    resultdecimal=0 
    power=0 # power hai 2 ki 
    index=len(num)-1 # index jo ki lst pe hoga 

    while index>=0: # 0 ya uske equal hai tb tk chlao 
        if num[index]=="1": # agr index 1 ke equal hai to 
              resultdecimal+=(2**power) # 2 ki power add kro ans me 

        index-=1 # index ko km krte jao 
        power+=1 # or power increase 
       
    return resultdecimal

print(convertdecimal("10111"))  # O/P=23
