# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([root])
        q2 = []
        answer =  []
        level = 0
        if root:
            answer.append([root.val])
        while q or q2:
            if not q:
                level += 1
                q.extend(q2)
                for i in range(len(q2)):
                    if q2[i] ==  None:
                        continue
                    q2[i] = q2[i].val
                
                if level % 2 == 1:
                    q2.reverse()
                    answer.append(q2)
                else:
                    answer.append(q2)
                q2 = []

            current = q.popleft()
            if current and current.left:
                q2.append(current.left)
            if current and current.right:
                q2.append(current.right)
            
        return answer