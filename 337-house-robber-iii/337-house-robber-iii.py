# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        lru_cache(maxsize = None)
        def recur(root):
            if not root:
                return 0,0
            
            with_l, without_l = recur(root.left)
            with_r, without_r = recur(root.right)
            return (root.val + without_l + without_r, max(with_l, without_l) + max(with_r, without_r))
        
        return max(recur(root))