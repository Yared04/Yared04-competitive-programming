# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        size = 0
        stack = []
        nod = head
        while head:
            size += 1
            head = head.next
        
        ctr = 0
        while ctr < (size // 2):
            stack.append(nod.val)
            ctr += 1
            nod = nod.next
        if size % 2 != 0:
            nod = nod.next
        while nod:
            if nod.val == stack[-1]:
                stack.pop()
                nod = nod.next
            else:
                return False
        return not(stack)
            