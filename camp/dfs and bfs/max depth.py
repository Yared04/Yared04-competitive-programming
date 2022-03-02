"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def depth(self,node, depth):
        if not node:
            return
        self.max_depth = max(depth,self.max_depth)
        for child in node.children:
            self.depth(child, depth +1)
    def maxDepth(self, root: 'Node') -> int:
        self.max_depth = 0
        self.depth(root, 1)
        return self.max_depth
        

    