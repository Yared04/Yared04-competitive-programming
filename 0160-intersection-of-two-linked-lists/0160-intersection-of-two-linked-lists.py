# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        node = headA
        while node:
            seen.add(node)
            node =  node.next
        node2 = headB
        while node2:
            if node2 in seen:
                return node2
            node2 = node2.next
        return None
        