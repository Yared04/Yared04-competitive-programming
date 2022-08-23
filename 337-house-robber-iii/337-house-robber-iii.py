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
            
            left = recur(root.left)
            right = recur(root.right)
            with_ = root.val + left[1] + right[1]
            
            ## with_out
            inc_left = left[0] + max(right[0], right[1])
            inc_right = right[0] + max(left[0], left[1])
            both = left[1] + right[1]
            return with_, max(inc_left, inc_right, both)
        
        return max(recur(root))