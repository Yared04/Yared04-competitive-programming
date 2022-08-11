# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, smaller, larger):
            if not root:
                return True
            if root.val >= smaller or root.val <= larger:
                return False
            right = helper(root.right,smaller, max(root.val,larger))
            left = helper(root.left, min(root.val, smaller), larger)

            return right and left
         
        return helper(root, inf, -inf)
            