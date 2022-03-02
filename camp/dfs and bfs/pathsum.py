# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def add(self,node, target, total):
        if not node:
            return
        if node.left == None and node.right == None and total == target:
            self.found_target = True
            return
        if node.left:
            self.add(node.left,target, total + node.left.val)
        if node.right:
            self.add(node.right,target, total + node.right.val)              
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.found_target = False
        if not root:
            return False
        self.add(root, targetSum, root.val)
        return self.found_target