class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            first = cur.next
            second = first.next
            cur.next = second
            first.next = second.next
            second.next = first
            cur = cur.next.next
        return dummy.next
      
  class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        start  = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(start)
        return head
   
