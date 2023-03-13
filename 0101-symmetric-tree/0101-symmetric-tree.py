# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(arr):
            left = 0
            right = len(arr)-1
            while left < right:
                if arr[left] and arr[right]:
                    if arr[left].val != arr[right].val:
                        return False
                else:
                    if arr[left] != arr[right]:
                        return False
                left += 1
                right -= 1
            return True
        
        queue = [root]
        while queue:
            temp = []
            for i in range(len(queue)):
                if queue[i]:
                    temp.append(queue[i].left)
                    temp.append(queue[i].right)
            if not mirror(temp):
                return False
            queue = temp
        return True
            
            