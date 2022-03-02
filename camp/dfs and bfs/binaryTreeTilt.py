# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Tilt(self,node):
        if not node:
            return 0
        if node.left == None and node.right == None:
            return node.val
        left = self.Tilt(node.left)
        right = self.Tilt(node.right)
        self.difference += abs(left-right)
        return left + right + node.val
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.difference = 0
        self.Tilt(root)
        return self.difference