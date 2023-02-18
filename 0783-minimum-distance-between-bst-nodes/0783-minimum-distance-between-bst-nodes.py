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
            self.vals.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        min_val = 10**5 + 1
        for i in range(len(self.vals)):
            for j in range(i+1, len(self.vals)):
                min_val = min(min_val, abs(self.vals[i] - self.vals[j]))
        return min_val
            
            