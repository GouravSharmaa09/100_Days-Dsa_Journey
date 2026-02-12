# DAY-39  LETTER COMBINATION OF A PHONE NUMBER            leat code - 17
# LIke Input "46" hai to iske all possible aplhabet combination bnanae hai jo keypad phone me hote hai 



def solve (index, digits,subset,result):
    phone_map={                   # dict jo values ko store kr rha hai
            "2": "abc",
            "3": "def",
            
            "4": "ghi",
            "5": "jkl",
            
            "6": "mno",
            "7": "pqrs",
            
            "8": "tuv",
            "9": "wxyz",
        }

    if index>=len(digits): # last index tk 
            result.append("".join(subset))    # joinkrge strings ko 
            return 

    # loop jo dict me se string ka combination krega one by one 
    for ch in phone_map[digits[index]]:
        # append aplha in list 
        subset.append(ch)
        solve(index+1,digits,subset,result)  #recursion krte jao 
        
        # bcktrack 
        subset.pop()

def phone_alpha(digits):
    result=[]
    solve(0,digits,[],result)
    return result

digits="23"    


print(phone_alpha(digits))

# output = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

# Time and complexcity = O(4n * n) -->worst case me 4 aplha hoskte hai koi koi keyword me  and n digit ki len 
# S.C= O(N) 