# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = []
        q = deque([])
        if root:
            q.append(root)
        while q:
            single_level = []
            for i in range(len(q)):
                cur = q.popleft()
                single_level.append(cur.val)
                cur.left and q.append(cur.left)
                cur.right and q.append(cur.right)
            level_order.append(single_level)
        return level_order
                
                
                
        