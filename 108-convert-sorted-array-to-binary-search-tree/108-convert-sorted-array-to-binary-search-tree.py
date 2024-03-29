# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recur(arr):
            if not arr: return None
            node = TreeNode(arr[len(arr)//2])
            node.left = recur(arr[:len(arr)//2])
            node.right = recur(arr[len(arr)//2 + 1: ])
            return node
        return recur(nums)