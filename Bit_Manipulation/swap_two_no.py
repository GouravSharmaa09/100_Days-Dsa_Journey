# DAY-32     SWAP THE TWO NUMBER (LOGIC- USING XOR )

def swap_number(a,b):
    # xor me same ka xor same se kro to zero hojata hai 
    a=a^b # a ka xor b se kiya 
    b=a^b # isme bhi same a ka xor b se kia to b b dono me comman cut jyega means 0 hojyega 
    a=a^b # and isme a zero hojyega b ki jgh a rhkege to 
    return [a,b] # swap hojyegi values 

print(swap_number(4,10))    
