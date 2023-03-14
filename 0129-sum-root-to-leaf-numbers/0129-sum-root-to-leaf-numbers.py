# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        all_numbers = []
        def dfs(node, number):
            if not node.left and not node.right:
                number += str(node.val)
                all_numbers.append(int(number))
                return
            node.left and dfs(node.left, number + str(node.val))
            node.right and dfs(node.right, number  + str(node.val))
            
        dfs(root, '')
        return sum(all_numbers)
        