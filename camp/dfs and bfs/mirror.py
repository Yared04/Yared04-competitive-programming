# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque([root])
        q = collections.deque()

        while queue:
            current = queue.popleft()
            if current:
                q.append(current.left)
                q.append(current.right)
            
            if not queue and q:
                i = 0
                j = len(q)-1
                while i < j:
                    if ((q[i] == None and q[j] == None) or (q[i]  and q[j] and q[i].val == q[j].val)):
                        i += 1
                        j -= 1    
                    else: 
                            return False

                    
                queue.extend(q)
                q = []
          
        return True
                
            
                