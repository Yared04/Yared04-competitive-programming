# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.depth = 0
        def dfs(node,count):
            if node:
                self.depth = max(count,self.depth)
                dfs(node.left,count+1)
                dfs(node.right, count+1)
            return self.depth
        left = dfs(root.left,1)
        self.depth = 0
        right = dfs(root.right,1)    
        if left == right:  
            return root
        elif left > right:
            return self.lcaDeepestLeaves(root.left)
        else:
            return self.lcaDeepestLeaves(root.right)
    