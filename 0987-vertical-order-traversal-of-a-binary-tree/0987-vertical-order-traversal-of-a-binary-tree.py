# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = defaultdict(list)
        def traverse(node, row, col):
            if not node: return
            columns[col].append((row, node.val))
            traverse(node.left, row + 1, col - 1)
            traverse(node.right, row + 1, col + 1)
        
        traverse(root, 0, 0)
        i = min(columns)
        res = []
        
        while len(columns[i]) > 0:
            temp = columns[i]
            temp.sort()
            res.append([val for row,val in temp])
            i += 1
        
        return res
            
        