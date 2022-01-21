# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        start  = head
        while start and start.next:
            length += 1
            start = start.next
        j = 1
        if n == length:
            return head.next
        else:
            remove = head
            while (length - n) > j and remove.next:            
                remove = remove.next
                j += 1
            print(remove.val)
            remove.next = remove.next.next

            return head
