# DAY-56 BOTTOM VIEW 
# SAME AS TOP VIEW 

from collections import deque

class solution :

    def bottom_view(node):
        if node is None:
            return 

        ans =[]
        result={}
        queue=deque
        queue=((node,0))

        while queue:

            e,line=queue.popleft()

            result[line]=e.val # only is line ka change hai and result me line chk nhi ki direct updte ki 

            if e.left:
                queue.append((e.left,line-1))

            if e.right:
                queue.append((e.right,line+1))

        for key,val in sorted(result.items()):
            ans.append(val)

        return ans                     



