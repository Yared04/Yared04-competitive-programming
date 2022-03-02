# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head 
        head = ListNode(0)
        new = head
        lis = []
        while node:
            heapq.heappush(lis, node.val)
            node = node.next
        for i in range(len(lis)):
            new.next = ListNode(heapq.heappop(lis))
            new = new.next
        return head.next
            
        
        
        