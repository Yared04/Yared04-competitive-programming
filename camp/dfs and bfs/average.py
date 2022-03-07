# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q1 = collections.deque([root])
        q2 = collections.deque()
        result = [root.val/1]
        while q1:
            current = q1.popleft()
            if current:
                q2.append(current.left)
                q2.append(current.right)
            if not q1:
                total = 0
                count = 0
                for i in range(len(q2)):
                    if q2[i]:
                        total += q2[i].val
                        count += 1
                if count:
                    result.append(total/count)

                q1.extend(q2)
                q2.clear()
        return result
        