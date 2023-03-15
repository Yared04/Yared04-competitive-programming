# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            i = 0
            while i < len(queue):
                cur = queue.popleft()
                if cur == None:
                    while queue:
                        temp = queue.popleft()
                        if temp:
                            return False
                        i += 1
                else:
                    queue.append(cur.left)
                    queue.append(cur.right)
                i += 1
        return True

        