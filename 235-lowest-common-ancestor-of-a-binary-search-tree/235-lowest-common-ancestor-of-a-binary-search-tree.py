# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def helper(root): 
            if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
                return root
            return None
        while res == None:        
            if p.val < root.val and q.val < root.val:
                root = root.left
                res = helper(root)
            elif p.val > root.val and q.val > root.val:
                root = root.right
                res = helper(root)
            else: 
                return root
        return res