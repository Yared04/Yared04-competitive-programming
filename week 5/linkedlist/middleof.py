class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution():
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one = two = head
        while two and two.next:
            one = one.next
            two = two.next.next
        return one