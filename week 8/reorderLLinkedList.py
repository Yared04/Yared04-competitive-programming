# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        pt1 = 0
        pt2 = len(nodes) - 1
        
        while pt1 < pt2:
            nodes[pt1].next = nodes[pt2]
            pt1 += 1
            nodes[pt2].next = nodes[pt1]
            pt2 -= 1
        nodes[pt1].next = None
        