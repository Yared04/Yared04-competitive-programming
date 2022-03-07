# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        def dfs(node):
            if not node: return
            if node.val % 2 == 0: 
                if node.left:
                    self.total += node.left.left.val if node.left.left else 0
                    self.total += node.left.right.val if node.left.right else 0
                    dfs(node.left)
                if node.right:
                    self.total += node.right.left.val if node.right.left else 0
                    self.total += node.right.right.val if node.right.right else 0
                    dfs(node.right)
            else:
                dfs(node.left)
                dfs(node.right)
            return self.total
        result = dfs(root) 
        return result