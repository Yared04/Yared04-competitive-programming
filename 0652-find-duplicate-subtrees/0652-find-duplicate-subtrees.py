# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtree = {}
        res = []
        
        def preorder(node):
            if not node:
                return "NULL"
            
            string = str(node.val) + ',' + preorder(node.left) + ',' + preorder(node.right)
            
            if string in subtree:
                if (subtree[string] + 1) == 2:
                    subtree[string] += 1
                    res.append(node)
            else:
                subtree[string] = 1
            
            return string
        
        preorder(root)
        return res