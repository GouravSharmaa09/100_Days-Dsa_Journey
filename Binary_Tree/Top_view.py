# DAY-56 TOP VIEW OF BINARY Tree
# institution = sepration krlege jo cut hora hai hai vo hi node top view hoga 


from collections import deque 

class solution :
    def bfs(node):

        if not node :
            return None 

        ans= []
        result={} # LINE NO. AND NODE VALUE STORE KE LIYE 
        queue=deque()
        queue.append((node,0)) # 0 LINE NO. HAI AND NODE -- ROOT 

        while queue:
            e,line= queue.popleft() 

            if line not in result: # LINE SE PHLE KOI NODE NHI MILTA TO ADD KRO 
                result[line]=e.val 

            if e.left: # LEFT SIDE - ME JYEGI 
                queue.append((e.left,line-1)) 

            if e.right: # RIGHT SIDE + HOGI
                queue.append((e.right,line+1))

        for key,val in sorted(result.items()): # LINES KO SORT KREGA AND TUP[ES ME BHJEGA ]
            ans.append(val)


        return ans 


#  T.C=O(N LOG N )
# S.C=O(N)       


