# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        def inorder(node):
            if node:
                inorder(node.left)
                arr.append(node.val)
                inorder(node.right)
        inorder(root)
        ptr1 , ptr2 = 0, 1
        to_be_swapped1 = arr[0]
        while ptr2 < len(arr):
            if arr[ptr1] > arr[ptr2]:
                to_be_swapped1 = arr[ptr1]
                to_be_swapped2 = arr[ptr2]
                ptr2 += 1
                while ptr2 < len(arr):
                    if arr[ptr2] < to_be_swapped2 :
                        to_be_swapped2 = arr[ptr2]
                    ptr2 += 1
                break
            else:
                ptr1 += 1
                ptr2 += 1
        def swap(node):
            if node:
                if node.val == to_be_swapped1:
                    node.val = to_be_swapped2
                elif node.val == to_be_swapped2:
                    node.val = to_be_swapped1
                swap(node.left)
                swap(node.right)
            return
        swap(root)
                
            
                
                
                
