# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.vals = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.vals.append(node.val)
            dfs(node.right)
        dfs(root)
        min_val = 10**5 + 1
        for i in range(len(self.vals)-1):
            min_val = min(min_val, self.vals[i+1] - self.vals[i])
        return min_val

            