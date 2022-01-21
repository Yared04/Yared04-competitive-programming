# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m = head
        while head and head.next:
            if head.val == head.next.val:
                s = head
                while s.next and s.val == s.next.val:
                    s = s.next
                head.next = s.next
                
            else:
                head = head.next
        return m
       