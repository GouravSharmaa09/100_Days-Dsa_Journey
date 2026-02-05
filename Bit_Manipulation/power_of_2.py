# DAY-32  FIND THE POWER OF 2
# Logic - N &(n-1)   --(n me se n-1 krke unka and kro result 0000 aayega )
# Power of 2: Hamesha ek '1' aur baaki saare '0' hote hain
# n-1 us 1 ko 0 bna dete hai 

def power_of_2(n):
    return n>0 and (n& (n-1)) ==0 # 

print(power_of_2(7))     #    O/p=False